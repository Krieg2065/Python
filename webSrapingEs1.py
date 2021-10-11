# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

html_txt = requests.get('https://www.wikihow.it/Creare-un-Blog-Personale').text
soup = BeautifulSoup(html_txt,'lxml')
passi = soup.find('li',class_ = 'whb')
print(passi)