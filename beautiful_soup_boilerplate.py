import requests
from helper import download
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html5lib')

outer_div = soup.find('div', {'class': 'thumb tright'})
img_tag = outer_div.find('img')
img_url = 'https:'+img_tag['src']

print(img_url)
download(img_url, "Goku.jpg")
