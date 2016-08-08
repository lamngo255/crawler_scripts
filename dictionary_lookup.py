import requests
from bs4 import BeautifulSoup

try:
    word = input("Enter your word: ")
    url = "http://dictionary.cambridge.org/dictionary/english/" + word
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')

    meanings = soup.findAll('meta', {'name': 'description'})
    for meaning in meanings:
        print(meaning['content'])
except:
    print("Sorry, your word is not in the dictionary.")
