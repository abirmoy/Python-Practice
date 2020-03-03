# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:21:28 2019

@author: Abirmoy
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:39:19 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup

url = 'https://nptel.ac.in/courses/106105182/1'

r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

# FIND THE FIRST H1 TAG
#find_a = html_soup.find_all('a', class_="ytp-title-text")
find_a = html_soup.find('a')
print(find_a.text)




















