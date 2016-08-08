import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

PLAYLIST = 'https://www.youtube.com/watch?v=FNQxxpM1yOs&list=PLQVvvaa0QuDeA05ZouE4OzDYLHY-XH-Nd'
TITLE_START = 0
DOMAIN = 'https://www.youtube.com/'
titles = []
links = []


def crawl(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    for playlist in soup.findAll('div', {'class': 'playlist-videos-container'}):
        for link in playlist.findAll('a'):
            results = urljoin(DOMAIN, link.get('href'))
            # links.append(results)
            print (results)
        for title in playlist.findAll('h4'):
            title = title.string.strip()
            title = title.replace("'", "")
            title = title[TITLE_START:].strip()
            # titles.append(title)
            print (title)


crawl(PLAYLIST)
