# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:39:19 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
'?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
url = 'https://cn.wikipedia.org'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# FIND THE FIRST H1 TAG
first_h1 = html_soup.find('h1')
#print(first_h1.name) # h1
#print(first_h1.contents) #['List of ', [...], ' episodes']
#
#print(str(first_h1))
## Prints out: <h1 class="firstHeading" id="firstHeading" lang="en">List of
## <i>Game of Thrones</i> episodes</h1>
#
#print(first_h1.text) # List of Game of Thrones episodes

#print(first_h1.get_text()) # Does the same
#
#print(first_h1.attrs)
## Prints out: {'id': 'firstHeading', 'class': ['firstHeading'], 'lang': 'en'}
#print(first_h1.attrs['id'])  # firstHeading
#print(first_h1.get('id')) # DOES THE SAME
print('--------------------CITATIONS---------------------')

# Find the first five cite elements with a citation class
#cites = html_soup.find_all('cite', class_ = 'citation', limit = 5)
#for citation in cites:
#    print(citation.get_text())
#    # INSIDE THIS CITE ELEMENT, FIND THE FIRST A TAG
#    link = citation.find('a')
#    # AND ...SHOWS ITS URL
#    print(link.get('href'))
#    print()
#

























