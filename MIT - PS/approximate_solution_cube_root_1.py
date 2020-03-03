# -*- coding: utf-8 -*-
"""
Created on Sun May 12 02:19:29 2019

@author: Abirmoy
"""
cube = 100000 #int(input('Enter a number:' ))
epsilon = 0.1
guess = 0
increment = 0.0001
num_guess = 0

while (abs(guess**3-cube)) >= epsilon and abs(guess**3) <= cube:
    guess += increment
    num_guess +=1
print('number of guess: ',num_guess)
if abs((guess**3)-cube) > epsilon:
    print('Failed of cube root of: ',cube)
else:
    print(guess,' is close to cube root of ',cube)