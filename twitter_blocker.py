from typing import Generator
import twitter
from twitter import TwitterError
from datetime import datetime
from PIL import Image
import requests
import sqlite3


class UserSuspendedError(Exception):
    def __init__(self, user_id, screen_name, message=None):
        self.user_id = user_id
        self.screen_name = screen_name
        self.message = message if message is not None else f"User id: {user_id}, screen_name: {screen_name}, was suspended."

    @staticmethod
    def is_this_error(twitter_error):
        return twitter_error.args[0][0]['code'] == 63


class UserWrapper:
    def __init__(self, twitter_user):
        # normal image is too small and looks ugly
        url = twitter_user.profile_image_url_https.replace('_normal.', '_400x400.')
        self.profile_pic = Image.open(requests.get(url, stream=True).raw)

        self.display_name = twitter_user.name
        self.screen_name = twitter_user.screen_name
        self.description = twitter_user.description
        self.twitter_id = twitter_user.id
        self.follower_count = twitter_user.followers_count


def result_or_none(r):
    return r if r is None else r[0]


class Blocker:
    def __init__(self):
        self.api = None
        self.authenticated_user = None

    def __enter__(self):
        self._db_connection = sqlite3.connect("twitter_blocker.sqlite3", check_same_thread=False)
        self._cursor = self._db_connection.cursor()
        self._cursor.execute(
            """create table if not exists blocked_users (
                user_id integer, 
                user_name, 
                parent_id integer, 
                reason, 
                block_date datetime,
                PRIMARY KEY(user_id, parent_id)
            );""")
        self._cursor.execute(
            """create table if not exists current_block_run (
                user_id integer,  
                parent_id integer, 
                reason, 
                PRIMARY KEY(user_id, parent_id)
            );""")
        self._cursor.execute("create table if not exists user_data (key text primary key, value);")
        self._db_connection.commit()

        self.authenticate()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db_connection.close()

    def authenticate(self):
        credentials = self.get_account_settings()
        try:
            self.api = twitter.Api(**credentials, sleep_on_rate_limit=True)
            self.authenticated_user = UserWrapper(self.api.VerifyCredentials())
            #print(self.api.rate_limit.resources.get('blocks'))
        except TwitterError as e:
            print(e)
            pass

    def get_block_count(self):
        return result_or_none(self._cursor.execute("select count(distinct user_id) from blocked_users;").fetchone())

    def get_sync_date(self):
        return result_or_none(self._cursor.execute("select value from user_data where key sync_date;").fetchone())

    def save_sync_date(self):
        self._cursor.execute(
            "insert into user_data (key, value) values (sync_date, ?) on conflict(key) do update set value=excluded.value;",
            (datetime.utcnow(),))
        self._db_connection.commit()

    def get_account_settings(self):
        consumer_key = result_or_none(self._cursor.execute("select value from user_data where key='consumer_key';").fetchone())
        consumer_secret = result_or_none(self._cursor.execute("select value from user_data where key='consumer_secret';").fetchone())
        access_token_key = result_or_none(self._cursor.execute("select value from user_data where key='access_token_key';").fetchone())
        access_token_secret = result_or_none(self._cursor.execute("select value from user_data where key='access_token_secret';").fetchone())

        return {
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret,
            'access_token_key': access_token_key,
            'access_token_secret': access_token_secret
        }

    def save_account_settings(self, consumer_key, consumer_secret, access_token_key, access_token_secret):
        values = [
            ('consumer_key', consumer_key),
            ('consumer_secret', consumer_secret),
            ('access_token_key', access_token_key),
            ('access_token_secret', access_token_secret)
        ]
        self._cursor.executemany(
            "insert into user_data (key, value) values (?, ?) "
            "on conflict(key) do update set value=excluded.value;", values)
        self._db_connection.commit()

    def _block_users(self, parent_id, user_ids: list, reason: str) -> Generator[int, None, None]:
        """Blocks users by their ID"""
        successful_blocks = 0
        # it can take some time to create block if they are many so they could get different time stamps
        # as the program runs but I think its better to have the same timestamp for each batch
        date = datetime.utcnow()
        user_ids.insert(0, parent_id)
        for id in user_ids:
            if self._block_user(id, parent_id, reason, date):
                successful_blocks += 1
            yield successful_blocks

    def get_follower_ids(self, user_id) -> Generator[list[int], None, None]:
        next_cursor = -1
        previous_cursor = None
        while next_cursor != 0 and next_cursor != previous_cursor:
            next_cursor, previous_cursor, data = self.api.GetFollowerIDsPaged(user_id=user_id, cursor=next_cursor)
            yield data

    def _block_user(self, user_id, parent_id, reason, date):
        error = False
        try:
            blocked_user = self.get_blocked_user(user_id)
            if not blocked_user:
                tu = self.api.CreateBlock(user_id=user_id, include_entities=False, skip_status=True)
                blocked_user = {'user_id': tu.id, 'user_name': tu.screen_name}

        except TwitterError as e:
            print(e)
            error = True
        else:
            self._cursor.execute(
                """
                insert into blocked_users (
                    user_id, 
                    user_name, 
                    parent_id, 
                    reason, 
                    block_date
                ) 
                values (?, ?, ?, ?, ?) 
                on conflict(user_id, parent_id) do 
                    update set user_name=excluded.user_name""",
                (blocked_user['user_id'], blocked_user['user_name'], parent_id if blocked_user['user_id'] != parent_id else None, reason,
                 date))

        if parent_id == user_id:
            # TODO check if this can actually happen the way the table is filled
            self._cursor.execute(
                """
                delete from current_block_run where user_id = ? and parent_id is null
                """, [user_id])
        else:
            self._cursor.execute(
                """
                delete from current_block_run where user_id = ? and parent_id = ?
                """, [user_id, parent_id])

        # do some commits so the collected data is not lost in case the thing breaks
        self._db_connection.commit()
        return not error

    def block_users(self, parent_id, user_ids, reason):
        """Will block all users in user_ids."""
        self._save_to_current_block_run(parent_id, user_ids, reason)

        return self._block_users(parent_id, user_ids, reason)

    def block_followers(self, user_id, reason):
        """Will fetch the followers of user_id directly from twitter and then block them"""
        try:
            follower_ids = self.api.GetFollowerIDs(user_id=user_id)
            self._save_to_current_block_run(user_id, follower_ids, reason)
        except TwitterError as e:
            print(e)
            return None
        return self._block_users(user_id, follower_ids, reason)

    def _save_to_current_block_run(self, parent_id, user_ids, reason):
        # saving accounts to block so they don't have to be requested again in case something happens
        batch = [[user_id, parent_id, reason] for user_id in user_ids]
        batch.append([parent_id, None, reason])
        self._cursor.execute("delete from current_block_run;")
        self._cursor.executemany("""
                       insert into current_block_run (
                           user_id, 
                           parent_id, 
                           reason
                       ) 
                       values (?, ?, ?) on conflict(user_id, parent_id) do 
                           update set reason=excluded.reason;""", batch)
        self._db_connection.commit()

    def get_last_run_info(self):
        c = result_or_none(self._cursor.execute("select count(*) from current_block_run;").fetchone())
        if c is not None and c > 0:
            r = result_or_none(self._cursor.execute("select reason from current_block_run limit 1;").fetchone())
        else:
            r = None
        return c, r

    def get_last_run_target_id(self):
        self._cursor.execute("select distinct(parent_id) from current_block_run")
        res = self._cursor.fetchall()
        if len(res) > 1:
            raise Exception("There shouldn't be more than one distinct parent_id in current_block_run table")
        return res[0][0]

    def continue_blocking(self):
        self._cursor.execute(
            """
            select user_id, parent_id, reason from current_block_run;
            """)
        result = self._cursor.fetchall()
        date = datetime.utcnow()

        id_ = result[0][1]
        count = self._cursor.execute("select count(*) from blocked_users where parent_id = ? or user_id = ?;", [id_, id_]).fetchone()[0]

        successful_blocks = count
        for row in result:
            if self._block_user(row[0], row[1], row[2], date):
                successful_blocks += 1
            yield successful_blocks

    def get_user(self, screen_name=None, user_id=None):
        """Retrieve a user via Twitter API"""
        try:
            if user_id:
                user = self.api.GetUser(user_id=user_id)
            elif screen_name:
                user = self.api.GetUser(screen_name=screen_name)
            else:
                raise ValueError("Either screen_name or user_id must be given")
        except TwitterError as e:
            if UserSuspendedError.is_this_error(e):
                raise UserSuspendedError(user_id, screen_name) from e
            print(e.message)
            return None

        return UserWrapper(user)

    def get_blocked_user(self, user_id):
        """Get user from local block database"""
        r = self._cursor.execute(
            "select user_id, parent_id, user_name, reason "
            "from blocked_users where user_id = ?", [user_id]).fetchone()
        if r is not None:
            return {'user_id': r[0], 'parent_id': r[1], 'user_name': r[2], 'reason': r[3]}

