# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 16:54:55 2019

@author: qxz0ga0
"""

def fib(n): # WRITE FIBONACCI SERIES UP TO N
    """PRINT A FIBONACCI SERIES UP TO N."""
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()
    
    
# CALLING THE FUNCTION
fib(2000) #0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
    