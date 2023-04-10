import os
from bs4 import BeautifulSoup
import requests


class Network():
    def __init__(self):
        self.styles = ['kubizm']
        self.url = ['https://www.wikiart.org/ru/paintings-by-style/',
                    '?select=featured&json=2&layout=new&page=', 
                    '&resultType=masonry']

    def get_page(self, style, pagenum):
        page = requests.get(self.url[0] + style +
                            self.url[1] + str(pagenum) + self.url[2])
        return page

    def make_soup(self, page):
        soup = BeautifulSoup(page.text, 'html5lib')
        return soup

    def make_dir(self, name, s):
        path = os.getcwd() + '/' + s + '/' + name
        os.mkdir(path)
