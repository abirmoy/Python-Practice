# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:45:40 2019

@author: qxz0ga0
"""

a, b = 0, 1

while a<10:
    print(a, end = ',') # end = ',' TO AVOID NEW LINE AFTER EACH ITERATION USING end PARAMETER WE ARE REPLACING '\n'
    a, b = b, a+b