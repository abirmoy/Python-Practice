# -*- coding: utf-8 -*-
"""
Created on Mon May 13 03:56:41 2019

@author: Abirmoy
"""

cube = -27
epsilon = 0.01
num_guess = 0
low = 0
high = abs(cube)
guess = (high + low)/2


while abs(guess**3 - abs(cube)) >= epsilon:
    if guess**3 < abs(cube):
        low = guess
    else:
        high = guess
    guess = (high + low)/2
    num_guess += 1
if cube < 0: #so that we shall perform negative number operation as well
    guess = -guess
print('num_guess', num_guess)
print(guess,'is close to the cube root of ', cube)