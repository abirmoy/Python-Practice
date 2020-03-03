# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:07:52 2019

this program prints the result of
x to the power y
and 2 base log(x)

@author: Abirmoy
"""
import numpy #in orger to perform log calculation

print("Enter number: ")
base = int(input())
power = int(input())

squer = base**power
print("x to the power y is: ",squer)

print(numpy.log2(base))