# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:22:30 2019

@author: Abirmoy
"""

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
even_a = []

for i in a:
    if i%2==0:
        even_a.append(i)

print(even_a)

##################################################
# SAME CODE IN ONE LINE
##################################################

new_even = [i for i in a if i%2==0]
print(new_even)