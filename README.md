# twitter-blocker

Simple Python program that blocks a Twitter account and all of its followers.


## About this application

This once was a small script I made quickly, mostly to block racist accounts and all their followers since these type of accounts often send their whole crowd after you. Now I use it mostly to block crypto/nft promoters. 

Despite there being other applications now that do the same, I continued to improve this whenever I found the time in the last years. This application can not be considered finished and probably never will be. It's a pet project, but I put it on GitHub because it may be of use for someone else, too.

The advantage this application has over others is that you don't have to create any other accounts or link your twitter to a third party. All data remains on your system.


## Installation

To run this Python program you need Python in version 3.8 or newer. On Linux or Mac systems you probably have it installed already. If you are on Windows you have to install it manually. You can get it from [the official website](https://www.python.org/downloads/)

You can check your Python version by opening a command line and enter `python --version`. On some Linux systems there are more than one python versions installed simultaneously and by default it uses older versions for legacy reasons. Then you have to explicitly type the version e.g. `python3.8`.

Python usually comes with the package manager PIP. Open a command line and use `pip install -r requirements.txt` to install the required dependencies. You may want to use a virtual environment too.


## Configuration

Start the application by running `twitter_blocker_gui`. Here you can connect your account by opening the Settings menu and click on Account entry. Enter your credential, [here is a Guide on how to get them.](https://python-twitter.readthedocs.io/en/latest/getting_started.html).

Save the changes by clicking OK. Now the main window should show some information about your connected account, so you can make sure you are connected to the right one.

When you never used the application before, the application will show 0 blocks because it only counts blocks created with this application.


## Blocking

After filling in your Twitter-API details you can block any user and their followers by simply entering their username into the input field with the `@` label (dont type the @ itself.

Optionally you can add a blocking reason, this can be helpful if you later want to know why someone got blocked, especially when the where a follower of another account you blocked.

There is a limit for how many requests per hour can be sent to Twitter. When the limit is reached, the program will wait until it can send requests again. In that case it can look like the program is freezing, the status should show that it's currently waiting.

If the program was closed during the blocking process, you can continue the last block run by pressing the continue button.

Sometimes an account can't be blocked. This is usually the case when you are blocked by them already or the account is protected and not visible to you.


## Beware of Overblocking

When you use this program it will block every twitter account without any further checks. The Program is not "smart". There is a good chance you will **overblock**. For example: When you block `@realDonaldTrump` you will probably block several newspapers and journalists too, since they are probably following for research reasons and not necessarily because they are fans. **Only use this program, when overblocking is not an issue for you.**


## Does not keep your block-list up to date

The program blocks only the users that are following the target account at the moment it is running. Perhaps you want to run it again now and then, to block new followers of the target accounts.


## Where stuff is stored

The Application creates a file `twitter_blocker.sqlite3` on your file system where all the blocks and your account data are stored. This file should be backed up if you want to later know your blocks you did with this application.