# twitter-blocker
Simple Python program that blocks a Twitter account and all of its followers.


## Installation

To run this Python program you need Python in version 3.6 or newer. On Linux or Mac systems you probably have it installed already. If you are on Windows you probably have to install it. You can get it from [the official website](https://www.python.org/downloads/)

You can check your Python version by opening a command line and enter `python --version`. On some Linux systems there are more than one python versions installed simultaneously and by default it uses older versions for legacy reasons. Then you have to explicitly type the version e.g. `python3.8`.

Python usually comes with the package manager PIP. Open a command line and use `pip install python-twitter` to install the Twitter-API wrapper that is used by the program. You can find out more about it [here](https://python-twitter.readthedocs.io/en/latest/installation.html)

## Configuration

Open the file `twitter-blocker.py` with a text editor and replace the placeholders of `consumer_key`, `consumer_secret`, `access_token_key`, `access_token_secret` with your actual data. [Here is a Guide on how to get these.](https://python-twitter.readthedocs.io/en/latest/getting_started.html)
Save the changes and now you can run the program.

## Run the program

After filling in your Twitter-API details you can run the program from a command line with `python twitter-blocker.py`.

The Program will ask you for a Twitter account name, just type it in without the `@`. It will output some informations from the target account so you can make sure you got the right one. After confirming by typing `YES` (Yes, you have to type it literally like that since this is a potentially dangerous operation that can block thousands of accounts), it will start to block all the followers of the target account and the account itself.

Sometimes an account can't be blocked. This is usually the case when you are blocked by them already or the account is protected and not visible to you.

The program will write all blocked accounts to a CSV-File. You can share this with others so they can import your block-list to twitter or use it as an archive or backup in case you want to undo the operation some day.

There is a limit for how many requests per hour can be send to Twitter. When the limit is reached, the program will wait untill it can send requests again. In that case it can look like the program hang itself, just give it an hour and it should continue. You probaly are blocking a load of accounts for it to happen.

## Beware of overblocking

When you use this program it will block every twitter account without any further checks. The Program is not "smart". There is a good chance you will **overblock**. For example: When you block `@realDonaldTrump` you will probably block several newspapers and journalists too, since they are probably following for research reasons and not necessarily because they are fans. **Only use this program, when overblocking is not an issue for you.**
