import requests
from bs4 import BeautifulSoup


city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = requests.get(url)


soup = BeautifulSoup(data.text, 'html.parser')
print(soup.find('span', {'class': 'phrase'}).string)
