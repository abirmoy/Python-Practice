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
#find_body = html_soup.select('body', class_="date-20190731")
find_link = html_soup.find('a', attrs={'class':'ytp-title-link yt-uix-sessionlink'}).get('href')
print(find_link.text)




















