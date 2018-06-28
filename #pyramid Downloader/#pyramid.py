from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
from glob import glob
import os
import requests

today = date.today()
day = timedelta(1)
try:
    target_day = datetime.strptime(sorted(glob("#pyramid/20*.html"))[-1][9:-5], '%Y-%m-%d').date() + day
except IndexError:
    # I'm going to just assume this means that we have no logs downloaded yet
    target_day = date(2014, 11, 19)

if not os.path.exists('#pyramid'):
    os.mkdir('#pyramid')

# Doesn't download logs from today because today is unfinished (and easily accessible)
while target_day < today:
    # Download the first page to use as a skeleton
    response = requests.get('https://botbot.me/freenode/pyramid/%s?tz=America%%2FChicago'
        % (target_day.__str__()))
    log = BeautifulSoup(response.text, 'lxml')
    print("Downloaded " + response.url)
    
    # Remove Font Awesome icons because they're blocked by CORS policy and therefore look ugly
    # Has to happen before the while loop for reasons I do not know (possible bug?)
    for i in log('i'):
        i.decompose()

    # Append additional pages to the log
    page_number = 2
    while True:
        response = requests.get('https://botbot.me/freenode/pyramid/%s?tz=America%%2FChicago&page=%d'
            % (target_day.__str__(), page_number),
            headers={'X-Requested-With': 'XMLHttpRequest'})
        if response.status_code is not 200:
            break
        print("Downloaded " + response.url)
        page = BeautifulSoup(response.text, 'lxml')
        log.find(id="Log").append(page)
        page_number += 1

    # Cheap way to convert relative URLs to absolute
    log.head.insert(0, log.new_tag("base", href="https://botbot.me"))

    # Write to file
    with open("#pyramid/" + target_day.__str__() + '.html', 'w+') as logfile:
        logfile.write(log.prettify())
    
    target_day += day