# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:02:51 2019

@author: Abirmoy
"""

num = int(input("Enter a number: "))

if num%2 == 0 and num%4 == 0:
    print(num,"is Even and divisible by 4")
elif num%2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")
    
    

#extra exersice 
check = int(input("Enter divisor: "))

if num%check == 0:
    print(check,"devides", num,"evenly")
else:
    print(check, "doensn't devide", num, "evenly")
