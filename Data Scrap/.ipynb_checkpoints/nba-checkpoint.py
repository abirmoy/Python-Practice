# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 05:24:57 2019

@author: Abirmoy
"""
# PLAYER CLASS row nba-player-index__row


from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS()

url = 'https://www.nba.com/players'
driver.get(url)
print(driver.page_source)

# CREATE SOUP
soup = BeautifulSoup(driver.page_source, 'lxml')
div = soup.find('div', class_ = 'nba-player-index__row')
#print(div)
for a in div.find_all('a'):
    print(a.text)

driver.quit()