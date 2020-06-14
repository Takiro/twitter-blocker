# install twitter api wrapper with `pip install python-twitter`
import twitter
from datetime import datetime
from sys import version_info

if version_info.major < 3 and version_info.minor < 6:
    print("Python version to low. Must be 3.6 or newer.")
    exit(1)

# Putt your Twitter API credentials here. If you want to know how to get them,
# check out this link
# https://python-twitter.readthedocs.io/en/latest/getting_started.html
api = twitter.Api(
    consumer_key='0000000000000000000000000',
    consumer_secret='00000000000000000000000000000000000000000000000000',
    access_token_key='000000000000000000-0000000000000000000000000000000',
    access_token_secret='000000000000000000000000000000000000000000000',
    sleep_on_rate_limit=True
)

blocks = api.GetBlocksIDs()
print("This program will block a user account and all of its followers. Does not work if the target account is "
      "protected.")
print(f"You currently block {len(blocks)} accounts.")
user_handle = ""
while user_handle.isspace() or not user_handle:
    print("Enter Twitter user Screen Name: @", end='')
    user_handle = input()

root_user = api.GetUser(screen_name=user_handle)

print('Is this the correct user to block?')
print()
print(f'Name:       {root_user.name}')
print(f'Created at: {root_user.created_at}')
print(f'Tweets:     {root_user.statuses_count}')
print(f'Following:  {root_user.friends_count}')
print(f'Followers:  {root_user.followers_count}')
print(f'Likes:      {root_user.favourites_count}')
print(f'Lists:      {root_user.favourites_count}')
print()

# +1 since we also block the root user
print(f'You are about to block {root_user.followers_count + 1} user accounts.')
print('Do you really want to proceed? Then type YES: ', end='')
do_block = input()
if do_block != 'YES':
    exit()

print(f'Getting {root_user.screen_name} followers...')
try:
    followers_ids = api.GetFollowerIDs(user_id=root_user.id)
except Exception as e:
    print("Could not get followers. Is the user's account protected?")
    print(e)
    exit()
else:
    followers_ids.append(root_user.id)

not_blocked = 0
filename = f'blocklist_{datetime.now().isoformat()}_{root_user.screen_name}.csv'

print(f"Blocked User-IDs will be saved to file {filename}")
with open(filename, 'w') as f:
    for fo_id in followers_ids:

        try:
            # Sometimes an account cannot be blocked, e.g. when it is protected
            blocked = api.CreateBlock(user_id=fo_id, include_entities=False, skip_status=True)
            print(f"Blocked @{blocked.screen_name}")
        except Exception as e:
            print(f"Error wile blocking user id {fo_id}")
            print(e)
            print('Skipping.')
            not_blocked += 1
        else:
            f.write(f'{blocked.id};"{blocked.screen_name}";"{blocked.name}"\n')

if not_blocked > 0:
    print(f'{not_blocked} accounts were not blocked due to errors')
    
new_blocks = api.GetBlocksIDs()
print(f'{len(new_blocks) - len(blocks)} new accounts were blocked.')
