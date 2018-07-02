# #pyramid Downloader

#pyramid on Freenode uses BotBot.me for logging, which was cool until BotBot.me disabled log searching

## Task
Download all the logs, with one file per day, preferably starting off from wherever downloads left off last time. Run wget to grab logs of #zope and #zope3-dev as well.

## Learning Outcomes
- BeautifulSoup basics
- Python's `datetime` module
- Python's `glob` module
- Working with files in Python
- Basic use of launchd

## Code Considerations
- Shove `com.jkmartindale.download-irc-logs.plist` into `~/Library/LaunchAgents/`
- If you actually need to use this, I am so, so sorry