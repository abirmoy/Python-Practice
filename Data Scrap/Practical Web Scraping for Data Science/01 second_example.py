# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 08:36:11 2019

@author: Abirmoy
"""


##############################################################################
### #1
#
#from urllib.parse import quote, quote_plus
#
#raw_string = 'a query with /, spaces and?&'
#
#print(quote(raw_string))
#print(quote_plus(raw_string))

##############################################################################
#import requests
#from urllib.parse import quote, quote_plus
#### #2
#url = 'http://www.webscrapingfordatascience.com/paramhttp/?query='
#raw_string = 'a query with /, spaces and?&'
#
#print('\nUsing quote: ')
## NOTHING IS SAFE, NOT EVEN '/' CHARACTERS, SO ENCODE EVERYTHING
#
#r = requests.get(url + quote(raw_string, safe=''))
#print(r.url)
#print(r.text)
#print('\nUsing quote_plus: ')
#
#r = requests.get(url + quote_plus(raw_string))
#print(r.url)
#print(r.text)
#

############################################################################
'''All this encoding juggling can quickly lead to a headache. Wasn’t requests 
supposed to make our life easy and deal with this for us? Not to worry, 
as we can simply rewrite the example above using requests only as follows:
    
    Note the usage of the params argument in the requests.get method: you can
simply pass a Python dictionary with your non-encoded URL parameters and 
requests will take care of encoding them for you'''



#
#### #3 # NEED TO IMPORT REQUESTS ONLY
#import requests
#
#url = 'http://www.webscrapingfordatascience.com/paramhttp/'
#parameters = {
#        'query': 'a query with /, spaces and?&'
#        } # SEE NOTE
#r = requests.get(url, params=parameters)
#
#print(r.url)
#print(r.text)

###############################################################################
'''
Silencing requests Completely Even when passing a string to params, or
including the full url in the requests.get method, requests will still try,
 as we have seen, to help out a little. For instance, writing:
requests.get('http://www.example.com/?spaces |pipe')
will make you end up with “?spaces%20%7Cpipe” as the query string in the
request URL, with the space and pipe (“|”) characters encoded for you. 
In rare situations, a very picky web server might nevertheless expect URLs 
to come in unencoded. Again,cases such as these are extremely rare, but we 
have encountered situations in the wild where this happens.
 In this case, you will need to override requests as follows:
'''
#
#
#### #3 
#
#import requests
#from urllib.parse import unquote
#
#class NonEncodedSession(requests.Session):
#    # OVERRIDE THE DEFAULT SEND METHOD
#    def send(self, *a, **kw):
#        # REVERT THE ENCODING WHICH WAS APPLIED
#        a[0].url = unquote(a[0].url)
#        return requests.Session.send(self, *a, **kw)
#
#
#my_requests = NonEncodedSession()
#url = 'http://www.example.com/?spaces |pipe'
#r = my_requests.get(url)
#print(r.url)
## WILL SHOW: 'http://www.example.com/?spaces |pipe'
#

##################################################################################
### #4
#
#import requests
#
#def calc(a, b, op):
#    url = 'http://www.webscrapingfordatascience.com/calchttp/'
#    params = {'a':a, 'b':b, 'op':op }
#    r = requests.get(url, params = params)
#    return r.text
#
#print(calc(4, 6, '*'))
#print(calc(4, 6, '/'))
#
#
##################################################################################
#### #5
##
#import requests
#
#url = 'https://en.wikipedia.org/w/index.php' + \
#'?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
#r = requests.get(url)
#print(r.text)















