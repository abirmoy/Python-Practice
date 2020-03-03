# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:29:52 2019

@author: Abirmoy
"""
def pig_latin(word):
    first_letter = word[0]
    
    #check if vowel
    if first_letter in 'aeiou':
        pig_word = word + "ay"
    else:
        pig_word = word[1:] + first_letter + "ay"
    
    return pig_word


print(pig_latin('apple'))