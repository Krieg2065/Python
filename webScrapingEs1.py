# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

html_txt = requests.get('https://www.wikihow.com/Breathe-Deeply#Video')
# = BeautifulSoup(html_txt,'lxml')
#passi = soup.find_all('li',class_ = 'b')
#print(passi)
#print(html_txt)
#print(html_txt.text)
soup = BeautifulSoup(html_txt.content,'html.parser')
#print(soup)
#passi = soup.find_all('div',class_ = 'step')
#print(passi)
#c = soup.find_all('b',class_ = 'whb')
#print(c)
c = soup.find_all("div",class_ =re.compile('mf-section-\d+'))
#print(c)
for i in c:
    d = i.find_all('div', class_ = 'step')
    #print(d)
    name = i.find('span', class_ = 'mw-headline')
    for z in d:
        if z :
            stepTitle = z.find('b',class_ = 'whb')
            print(stepTitle)
