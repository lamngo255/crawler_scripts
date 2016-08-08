import requests
from bs4 import *


lookup_word = 'cold'
data = requests.get("http://www.synonym.com/antonyms/" + lookup_word)
soup = BeautifulSoup(data.text, "html.parser")

for item in soup.find_all("ul", {"class": "synonyms"}):
   words = item.find_all("a")
   for synonym in words:
       print(synonym.string)
