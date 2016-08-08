# find all links using regex
import requests
import re

url = raw_input("Enter a URL: ")

website = requests.get(url)
content = website.text
links = re.findall('"((http|ftp)s?://.*?)"', content)

for link in links:
    print link[0]
