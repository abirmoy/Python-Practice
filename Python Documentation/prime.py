# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:27:13 2019

@author: qxz0ga0
"""

for n in range(3, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
             # loop fell through without finding a factor
             print(n, 'is a prime number')
#             break