# -*- coding: utf-8 -*-
"""
Created on Wed May 15 03:23:31 2019

@author: Abirmoy
"""




num = int(input("Enter a number: "))
listrange = (range(1,num+1))
divisorlist = []
for item in listrange:
    if num%item == 0:
        divisorlist.append(item)
print(divisorlist)

#another way
num = int(input("Enter a number: "))

divisorlist = []
for item in range(1,num+1):
    if num%item == 0:
        divisorlist.append(item)
print(divisorlist)