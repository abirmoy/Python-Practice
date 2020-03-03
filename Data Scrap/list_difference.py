# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:57:19 2019

@author: Abirmoy
"""

list1 = [10, 20, 30, 40, 50]
list2 = [5, 10, 15, 20, 25]

# ONLY ELEMENTS WHICH ARE EITHER IN LIST1 OR IN LIST2 BUT NOT IN BOTH
diff = list(set(list1).symmetric_difference(set(list2)))
print(diff)
