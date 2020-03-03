# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:26:54 2019

@author: Abirmoy
"""
### #1
#import requests
#
#url = 'http://www.webscrapingfordatascience.com/postform2/'
#
## FIRST PERFORM A GET REQUEST
##r = requests.get(url)
#
## FOLLOWED BY A POST REQUESTS
#formdata = {
#        'name': 'Seppe',
#        'gender': 'M',
#        'pizza': 'like',
#        'haircolor': 'brown',
#        'comments': ''
#        }
#r = requests.post(url, data = formdata)
#print(r.text)


### #2
#import requests
#
#url = 'http://www.webscrapingfordatascience.com/postform3/'
#
## NO GET REQUEST NEEDED
#
#formdata = {
#        'name': 'Seppe',
#        'gender': 'M',
#        'pizza': 'like',
#        'haircolor': 'brown',
#        'comments': ''
#        }
#
#r = requests.post(url, data = formdata)
#
#print(r.text)
## Will show: Are you trying to submit information from somewhere else?
## IN ORDER TO MAKE IT WORK
### #3
#import requests
#
#url = 'http://www.webscrapingfordatascience.com/postform3/'
#
## NO GET REQUEST NEEDED
#
#formdata = {
#        'name': 'Seppe',
#        'gender': 'M',
#        'pizza': 'like',
#        'haircolor': 'brown',
#        'comments': '',
#        'protection': '2c17abf5d5b4e326bea802600ff88405'
#        }
#
#r = requests.post(url, data = formdata)
#
#print(r.text)
## Will show: You waited too long to submit this information
## INORDER TO RESOLVE THIS AS WELL
### #4
#import requests
#from bs4 import BeautifulSoup
#
#url = 'http://www.webscrapingfordatascience.com/postform3/'
#
## FIRST PERFORM A GET REQUEST
#r = requests.get(url)
#
## GET OUT THE VALUE FOR PROTECTION
#html_soup = BeautifulSoup(r.text, 'html.parser')
#p_val = html_soup.find('input', attrs={'name': 'protection'}).get('value')
#
## NOW USE THIS p_val IN A POST REQUEST
#formdata = { 
#        'name': 'Seppe',
#        'gender': 'M',
#        'pizza': 'like',
#        'haircolor': 'brown',
#        'comments': '',
#        'protection': p_val
#        }
#r = requests.post(url, data = formdata)
#print(r.text)
#
#
### #5
#To upload a file, we simply use another argument, named files 
#(which can be used together with the data argument):
import requests

url = 'http://www.webscrapingfordatascience.com/postform2/'

formdata = {'name': 'Seppe'}
filedata = {'profile_picture': open('me.jpg', 'rb')}

r = requests.post(url, data=formdata, files=filedata)










































