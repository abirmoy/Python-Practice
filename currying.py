# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:20:08 2019

@author: Abirmoy
"""

# CURRYING

def a(x):
    def b(y):
        return x+y
    return b

print(a(3)(4)) #3+4 = 7

adder_3 = a(3)
adder_10 = a(10)

print(adder_3(6)) # 3+6 = 9
print(adder_10(7)) # 10+7 = 17