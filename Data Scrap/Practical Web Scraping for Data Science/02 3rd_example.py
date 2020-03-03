# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:14:08 2019

@author: Abirmoy
"""

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
r= requests.get(url)
html_content = r.text
html_soup = BeautifulSoup(html_content, 'html.parser')

# USE A LIST TO STORE EPISODE LIST
episodes = []
ep_tables = html_soup.find_all('table', class_ = 'wikiepisodetable')

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')
    # START BY FETCHING THE HEADER CELLS FROM THE FIRST ROW TO DETERMINE
    # THE FIELD NAMES
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    # THEN GO THROUGH ALL ROW EXCEPT THE FIRST ONE
    for row in table.find_all('tr')[1:]:
        values = []
        # AND GET THE COLUMN CELLS, THE FIRST ONE BEING INSIDE A th-tag
        for col in row.find_all(['th', 'td']):
            values.append(col.text)
        if values:
            episode_dict = {headers[i] : values[i] for i in 
                            range (len(values))}
            episodes.append(episode_dict)
# SHOW THE RESULTS
for episode in episodes:
    print(episode)



































