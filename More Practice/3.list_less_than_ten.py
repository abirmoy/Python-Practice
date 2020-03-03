# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:15:30 2019

@author: Abirmoy
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_a = []
for num in a:
    if num <= 10:
        new_a.append(num)

print(new_a)

#in order to get list as output the for loop can be written as follows

newlist = [num for num in a if num <= 10]

print(newlist)