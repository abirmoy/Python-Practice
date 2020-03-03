# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 03:18:59 2019

@author: Abirmoy
"""

from bs4 import BeautifulSoup

##############################################################################
# CREATING SEARCHING SCOPE VIA LOCAL HTML FILE
# 1. IF THE FILE TO BE PARSED IN THE EXECUTABLE DIRECTORY 
#    THEN JUST MENTION THE FILE NAME EX. file.html
# 2. IF IN SOME OTHER DIRECTORY THEN, ADD \\ SO PYTHON DOSENT GET CONFUSED
#      EX. 'C:\\Users\\Abirmoy\\Downloads\\file.html'
##############################################################################


# sample.html not available
soup = BeautifulSoup(open('sample.html'), 'lxml') # must import BeautifulSoup from bs4, also specify the directory of the driver
#print(soup.prettify()) # soup.prettify() FOR PRINTING HTML IN CONSOLE

#"""
#in BeautifulSoup after declaring variable, it also becomes a scope
#"""

for tr in soup.find_all('tr'):
    for td in tr.find_all('td'):
        print(td.text)




















