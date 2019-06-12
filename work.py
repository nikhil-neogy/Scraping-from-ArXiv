import requests
from lxml import html
from helper import download

url = "https://arxiv.org/search/advanced?advanced=1&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=announced_date_first&abstracts=hide&size=50&order=-announced_date_first"

response = requests.get(url)

tree = html.fromstring(response.content)

filenames = tree.xpath('/html/body/main/div[2]/ol/li[position()<=3]/div/p/a')
elements = tree.xpath('/html/body/main/div[2]/ol/li[position()<=3]/div/p/span/a[1]')

for filename, element in zip(filenames, elements):
    pdf_file_name = filename.text
    pdf_file_name = pdf_file_name.replace(':', '_')
    pdf_file_name = pdf_file_name.replace('.', '_')
    pdf_file_name += ".pdf"

    pdf_file_link = element.attrib['href']
    pdf_file_link += ".pdf"

    download(pdf_file_link, pdf_file_name)


