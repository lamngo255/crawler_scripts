import requests
from bs4 import BeautifulSoup
from urlparse import urljoin

url = 'https://thenewboston.com/'
content = requests.get(url)


soup = BeautifulSoup(content.text, 'html.parser')

for elem in soup.find_all("a", href=True):
    print elem.string
    print urljoin(url, elem['href']) 
