from bs4 import BeautifulSoup
import requests

for year in range(2005, 2019):
    # Having everything in one file overloads Pocket, so let's separate files by year
    with open('%s.html' % year, 'w+') as output:
        # Header needed for Pocket to recognize the file
        output.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        # (note that newlines are required for everything)

        page_number = 1
        while True:
            response = requests.get('http://www.yankodesign.com/%s/page/%s/' % (year, page_number))
            
            if response.status_code is not 200:
                break
            
            print('%s: %s' % (year, page_number))

            page = BeautifulSoup(response.text, 'lxml')
            for headline in page.find_all(itemprop="headline"):
                output.write('<a href="%s"></a>\n' % headline.find('a')['href'])
            
            page_number += 1