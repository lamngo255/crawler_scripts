import requests
import sys
from bs4 import BeautifulSoup
from urlparse import urljoin


reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.youtube.com/'
content = requests.get(url)
soup = BeautifulSoup(content.text, 'html.parser')

for elem in soup.find_all("a", href=True):
    print elem.string
    print urljoin(url, elem['href'])
