# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:34:33 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup


url = 'https://nptel.ac.in/courses/106105182/'
#url = 'https://en.wikipedia.org/wiki/Dark_web'
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

#print(html_contents,  file=open('log.html', 'w'))
print(r.request.url)
x = []
for a in html_soup.find_all('iframe', src=True):
    x.append(a)

print(x, file=open('log.txt', 'w'))















# FIND THE FIRST H1 TAG
#first_h1 = html_soup.find_all('id')
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
#print('--------------------CITATIONS---------------------')

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

























