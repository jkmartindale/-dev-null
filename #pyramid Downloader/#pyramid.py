from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
from glob import glob
import requests

today = date.today()
day = timedelta(1)
# target_day = date(2014, 11, 19)
target_day = datetime.strptime(sorted(glob("#pyramid/20*.html"))[-1][9:-5], '%Y-%m-%d').date() + day

# Doesn't download logs from today because today is unfinished (and easily accessible)
while target_day < today:
    with open("#pyramid/" + target_day.__str__() + '.html', 'w+') as logfile:
        # Download the first page to use as a skeleton
        response = requests.get('https://botbot.me/freenode/pyramid/%s?tz=America%%2FChicago'
            % (target_day.__str__()))
        log = BeautifulSoup(response.text, 'html.parser')
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
            page = BeautifulSoup(response.text, 'html.parser')
            log.find(id="Log").append(page)
            page_number += 1

        # I'm too lazy to convert relative URLs myself
        log.head.insert(0, log.new_tag("base", href="https://botbot.me"))

        # Write to file
        logfile.write(log.prettify())
    target_day += day