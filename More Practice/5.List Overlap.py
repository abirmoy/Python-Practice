# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:22:30 2019

@author: Abirmoy
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1,2, 3, 4, 5, 6, 7, 8, 9, 89,10, 11, 12, 13]

new_list = []
new_list2 = []

for i in a:
    if i in b:
        new_list.append(i)
for i in new_list:
    if i not in new_list2:
        new_list2.append(i)
print(new_list2)


#########################################################
# Writing same code in one line

