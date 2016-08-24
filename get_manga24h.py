import urllib.request
import re
import requests
from bs4 import BeautifulSoup

# response = requests.get(
#     'http://2.bp.blogspot.com/-PKjrCSv8URU/VPMdQL0IlkI/AAAAAAAChMQ/2IafCHJaWAQ/s0/Love-Riron-Chap-43-trang-1-Manga24h.jpg',
#     {'stream': True})

# filedata = open('img/img.jpg', 'wb')
# for block in response.iter_content(1024):
#     if not block:
#         break
#     filedata.write(block)


def download_image(image_url):
    image_name = re.search('.*\/(.*)', image_url).group(1)

    try:
        urllib.request.urlretrieve(image_url, 'img/' + image_name)
        print('Downloaded ' + image_name)
    except:
        print('Error: ' + image_name)


def parse_main_page(mainpageUrl):
    chapter_list = []

    try:
        body = requests.get(mainpageUrl)
        html = BeautifulSoup(body.text, 'html.parser')
        option_select = html.find('select', {'class': 'form-control'})

        if option_select is not None:
            parsed_chapters = option_select.find_all('option', limit=2000)

            for chapter in parsed_chapters:
                for attr, val in chapter.attrs.items():
                    if attr == 'value':
                        chapter_list.append(val)

            return chapter_list
    except:
        print('Cannot find manga list!')


def parse_chapter_page(chapterURL):
    imageList = []
    body = requests.get(chapterURL)
    parsed_html = BeautifulSoup(body.text, 'html.parser')
    data_script = parsed_html.find_all('script')

    # get images data among the script
    for script in data_script:
        if script.getText().find('images = new Array();') != -1:
            text_data = script.getText()
            data_value = re.search("\w*data=('.*').*", text_data)
            imageList = data_value.group(1).strip("'").split("|")
    return imageList


mainpageUrl = 'http://manga24h.me/Love-Riron.htm'
# print(parse_main_page(mainpageUrl))
imageurls = parse_chapter_page('http://manga24h.me/Love-Riron/Chap-22/')
for url in imageurls:
    download_image(url)
