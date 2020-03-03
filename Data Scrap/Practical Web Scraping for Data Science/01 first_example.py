# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:58:31 2019

@author: Abirmoy
"""

import requests


url = 'http://www.webscrapingfordatascience.com/basichttp/'
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=tes/'
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=test&other=ignored'
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query=complex?&'
url = 'https://api.github.com/events'
url = 'https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue%26pli%3D1%26nlr%3D1&csig=AF-SEnacwnHx9aUcbZ4i%3A1569047002&flowName=GlifWebSignIn&flowEntry=AddSession'


r = requests.get(url) # requests.get() PERFORMS "HTTP GET" REQUESTS TO THE PROVIDED URL
print(r.text) # r.text CONTAINS HTTP RESPONS CONTENT BODY IN A TEXTUAL FORM
#
# EXPAND UPON THIS EXAMPLE A BIT FURTHER TO SEE WHATS GOING ON UNDER THE HOOD
#
# WHICH HTTP STATUS CODE DID WE GET BACK FROM THE SERVER
#print(r.status_code)
### WHAT IS THE TEXTUAL STATUS CODE
#print(r.reason)
## WHAT WERE THE HTTP RESPONS HEADERS
#print(r.headers)
### THE REQUEST INFORMATION IS SAVED AS A PYTHON OBJECT IN r.request
#print(r.request)
## WHAT WERE THE HTTP REQUEST HEADER
#print(r.request.headers)
## THE HTTP RESPONSE CONTENT
#print(r.request.url)