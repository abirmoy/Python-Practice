# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:35:42 2019

@author: Abirmoy
"""


from selenium import webdriver # for webdriver

#driver = webdriver.Chrome()  # will need to import selenium webdriver and specify the directory of driver if not in exetutated directory

driver = webdriver.PhantomJS(r'C:\Users\Abirmoy\Downloads\Compressed\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print(html_doc)




