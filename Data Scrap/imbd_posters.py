# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 08:08:31 2019

@author: Abirmoy
"""
# div class_= poster --> div[1] class_ = pswp__zoom-wrap --> img[1]['src']

from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=6BZWJ7VGJ5RPF0C6P66S&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'

driver = webdriver.PhantomJS()
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

div = soup.find('div', class_ = 'poster')

a = div.find('a')
print(a['href'])

















