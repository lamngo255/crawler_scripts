import re
import urllib.request
import requests
from bs4 import BeautifulSoup

content = requests.get('https://mocmeodx.wordpress.com/')
html = BeautifulSoup(content.text, 'html.parser')
images = html.find_all('img', {'src': True})


def download_image(image_url):
    image_name = re.search('.*\/(.*)\?.*', image_url).group(1)
    # image_name = re.search('.*\/(.*)', image_url).group(1)

    try:
        urllib.request.urlretrieve(image_url, 'img/' + image_name)
        print('Downloaded ' + image_name)
    except:
        print('Error: ' + image_name)


for image in images:
    download_image(image['src'])
