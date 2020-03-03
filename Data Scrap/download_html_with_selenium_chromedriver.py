# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:06:03 2019

@author: Abirmoy
"""
#import time
#from selenium import webdriver
#
#driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
#driver.get('http://www.google.com/xhtml');
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()

from selenium import webdriver # for webdriver

driver = webdriver.Chrome()  # will need to import selenium webdriver and specify the directory of driver if not in exetutated directory

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)























