import requests
from lxml import html

url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"
response = requests.get(url)

tree = html.fromstring(response.content)

elements = tree.xpath('//*[@id="mw-content-text"]/div/table[position()>2 and position()<12]/tbody/tr[*]/td[2]')

print(elements[0].attrib)
print(elements[0].text)
