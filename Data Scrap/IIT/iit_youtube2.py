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
#find_body = html_soup.find_all('body', class_="date-20190731 en_US ltr  exp-invert-logo exp-kevlar-settings exp-responsive exp-search-big-thumbs   site-center-aligned site-as-giant-card  webkit webkit-537")
find_body = html_soup.find('body')
print(find_body.text)




















