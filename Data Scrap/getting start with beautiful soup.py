# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:07:48 2019

@author: Abirmoy
"""
### CHECKEING SITE OWNER
#import whois 
#
#print(whois.whois('appspot.com')) 
###############################################################################
import re
import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError

def download(url,user_agent = 'wswp', num_retries = 2, charset = 'utf-8'):
    print('Downloading: ', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        resp = urllib.request.urlopen(request)
        cs = resp.headers.get_content_charset()
        if not cs:
            cs = charset
        html = resp.read().decode(cs)
    except (URLError, HTTPError, ContentTooShortError) as e:
        print('Download error: ', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # RECURSIVELY RETRY 5XX ERRORS
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the site map links
    links = re.findall('<loc>(.?)</loc>', sitemap)
    # download each link
    for link in links:
        html = download(link)
        # scrape html here

crawl_sitemap('http://example.webscraping.com/sitemap.xml')














