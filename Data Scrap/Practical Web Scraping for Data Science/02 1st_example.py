# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:34:28 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
'?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
url = 'https://en.wikipedia.org/wiki/Dark_web'


r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

### #FIND ELEMENTS INSIDE HTML TREE

print('\nfind: \n',html_soup.find('h1'))
print('\nfind dict: \n',html_soup.find('',{'id': 'p-logo'}))

print('\n \n')
for found in html_soup.find_all(['h1','h2']):
    print(found)