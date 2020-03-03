# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 02:07:34 2019

@author: Abirmoy
"""

from bs4 import BeautifulSoup



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

# SEARCH FOR ALL CHILD
p = soup.find('p', class_ = 'story')
all_p_child = p.findChildren()
print(all_p_child) 
print(len(all_p_child))

# SEARCH FOR PARENT
parent_of_p = soup.find('p', class_ = 'story')
all_parant = p.findParent()
print('\n'*10)
print(all_parant)

# SEARCH FOR SIBLINGS
first_a = soup.find('a')
remain_siblings = first_a.findNextSiblings() # WILL FIND REMAINING SIBLINGS AFRAR A
print('\n'*5)
print(remain_siblings)
print('length:'+str(len(remain_siblings)))












