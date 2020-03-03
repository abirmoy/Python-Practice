# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 06:32:40 2019

@author: Abirmoy
"""

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS()
url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'

driver.get(url)
print(driver.page_source)

soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find('table', class_ = 'chart')
for td in table.find_all('td', class_ = 'titleColumn'):
    full_title = td.text.strip().replace('\n', '').replace('      ', '')
    
    rank = full_title.split('.')[0]
    print(rank)
    
    title = full_title.split('.')[1].split('(')[0]
    print(title)
    
    year = full_title.split('(')[1][:-1]
    print(year)
    
    a = td.find('a')
    print(a['href'])
    
    print('\n')
    
    
driver.quit()































    
    
    
    
    
    
    
    
    
    
    
    
    