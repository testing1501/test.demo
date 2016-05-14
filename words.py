import requests
from bs4 import BeautifulSoup

def get_words_from_url(url):
    list_of_words = []
    obj_html = requests.get(url)
    text_html = obj_html.text
    bs = BeautifulSoup(text_html)
    for link in bs.findAll('a', {'class':'marginright5 link linkWithHash detailsLink'}):
        words = link.strong.string
        list_of_words += words.split()
    print(list_of_words)


get_words_from_url('http://olx.ua/nedvizhimost/arenda-kvartir/')

