# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 02:55:50 2019

@author: Abirmoy
"""

from bs4 import BeautifulSoup

# SEARCH SCOPE 
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
# CREATING SOUP OBJECT
soup = BeautifulSoup(html_doc, 'lxml')
# must import BeautifulSoup from bs4, also specify the directory of the driver

"""
in BeautifulSoup after declaring variable, it also becomes a scope
"""

#  TEXT OUTPUT
first_p = soup.find('p')
print(first_p.text) # .text FOR TEXT OUTPUT

# ANOTHR EXAMPLE FOR TEXT
first_a = soup.find('a')
print(first_a.text) # .text FOR TEXT OUTPUT
















