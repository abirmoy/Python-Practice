# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:33:06 2019

@author: Abirmoy
"""

from bs4 import BeautifulSoup
#from selenium import webdriver # for webdriver

#driver = webdriver.PhantomJS()
#driver.get('http://python.org')
html_doc = """
<html>
	<head>
		<title>The Dormouse's story</title>
	</head>
<body>
	<p class="title">
		<b>The Dormouse's story</b>
	</p>
	<p class="story">Once upon a time there were three little sisters; and their names were
	<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
	<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
	<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
	and they lived at the bottom of a well.</p>
	<p class="story">...</p>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'lxml') # must import BeautifulSoup from bs4, also specify the directory of the driver
#print(soup.prettify()) # soup.prettify() FOR PRINTING OUT HTML

# fetching p teg
get_ptag = soup.find('p')
print("\n"*10)
print(get_ptag)
#driver.quit()

# FIND ALL TAGS

get_atag = soup.find_all('a') 
print("\n"*10)
print(get_atag)
print("length:" +str(len(get_atag)))




















