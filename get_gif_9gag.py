import requests
from bs4 import BeautifulSoup


def get_home_page():
    # get articles
    try:
        body = requests.get("http://9gag.com/gif")
        if body.status_code == 200:
            html = BeautifulSoup(body.text, 'html.parser')
            articles = html.find_all('article')
            return articles
    except:
        print('Error!')
    return False


def parse_data(original_data):
    list_parsed_data = []

    for value in original_data:
        object_save = {
            'name': '',
            'slug': '',
            'webm': '',
            'mp4': '',
            'image': '',
        }

        html = BeautifulSoup(str(value), 'html.parser')
        try:
            object_save['name'] = html.find(
                'h2', {'class': 'badge-item-title'}).text.strip()
            object_save['img'] = html.find(
                'img', {'class': 'badge-item-img'}).attrs['src'].strip()

            sources = html.find_all('source')
            for source in sources:
                src = source.attrs['src']
                if 'mp4' in src:
                    object_save['mp4'] = src
                if 'webm' in src:
                    object_save['webm'] = src

            list_parsed_data.append(source)
        except:
            print('Data error!')

    return list_parsed_data

print(parse_data(get_home_page()))
