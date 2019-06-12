import requests
from lxml import html
from helper import download

for i in range(2):

    url = "https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=title&classification-computer_science=y&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=announced_date_first&abstracts=hide&size=50&order=-announced_date_first&start={page_num}"
    url = url.format(page_num=i*50)

    response = requests.get(url)

    tree = html.fromstring(response.content)

    range_of_files_per_page = "position()<=2"

    filename_xpath = '/html/body/main/div[2]/ol/li[{range_files}]/div/p/a'
    element_xpath = '/html/body/main/div[2]/ol/li[{range_files}]/div/p/span/a[1]'

    filename_xpath = filename_xpath.format(range_files=range_of_files_per_page)
    element_xpath = element_xpath.format(range_files=range_of_files_per_page)

    filenames = tree.xpath(filename_xpath)
    elements = tree.xpath(element_xpath)

    for filename, element in zip(filenames, elements):
        pdf_file_name = filename.text
        pdf_file_name = pdf_file_name.replace(':', '_')
        pdf_file_name = pdf_file_name.replace('.', '_')
        pdf_file_name += ".pdf"

        pdf_file_link = element.attrib['href']
        pdf_file_link += ".pdf"

        download(pdf_file_link, pdf_file_name)


