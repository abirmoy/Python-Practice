# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:20:26 2019

@author: Abirmoy
"""

cube = 27
for guess in range (cube+1):
    if guess**3 == cube:
        print('Cube of',cube,'is',guess)
