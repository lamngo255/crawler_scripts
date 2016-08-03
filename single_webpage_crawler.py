# return links content and the link itself
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://www.youtube.com/'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

for elem in soup.find_all("a", href=True):
    print (elem.string)
    print (urljoin(url, elem['href']))

