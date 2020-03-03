# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:03:31 2019

@author: Abirmoy
"""

from selenium import webdriver # for webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()  # will need to import selenium webdriver and specify the directory of driver if not in exetutated directory
# if driver not in the location of .py file, 
#must pass the driver location inside parentheses (r'input location')


driver.get('http://python.org')
html_doc = driver.page_source
soup = BeautifulSoup(html_doc, 'lxml') # must import BeautifulSoup from bs4, also specify the directory of the driver
print(soup.prettify()) # soup.prettify() FOR PRINTING OUT HTML
driver.quit()
