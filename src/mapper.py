import sys
import requests
from bs4 import BeautifulSoup

import re
def is_url(url):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    return len(re.findall(regex, url)) > 0

def scrape_urls(page):
    try:
        reqs = requests.get(page)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            temp_url = link.get('href')
            if temp_url[0] == ".":
                temp_url = page + temp_url[1:]
            elif temp_url[0] == "#":
                temp_url = page
            if is_url(temp_url):
                urls.append(temp_url if temp_url[-1] != "/" else temp_url[:-1])
        return list(set(urls))
    except:
        return []

for line in sys.stdin:
    line = line.strip()
    page, state = line.split()
    if page[-1] == '/':
        page = page[:-1]
    state = int(state)
    if state == 0:
        print(page, state)
        urls = scrape_urls(page)
        if len(urls) == 0:
            print(page, -1)
        else:
            print(page, *urls)
            for url in urls:
                print(url, 0)
    else:
        print(page, 1)