# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 22:19:28 2019

@author: Abirmoy
"""
##################################################################################
#
#
#
### LIST ###
#'''Lists are ordered sequences that can hold a variety of object type.
#Support indexing and slicing, list can be nested.'''
#
#my_list = [1,'two',['three',4],5,6,7]
#my_list2 = ['eight', 9, 'ten']
#
#print('len: ',len(my_list)) # -->6
#print(my_list[1]) # INDEX USED # -->two
#
## CONCATINATING LIST
#another_list = my_list + my_list2
#print(another_list) # -->[1, 'two', ['three', 4], 5, 6, 7, 'eight', 9, 'ten']
#
## CHANGING ELEMENT
#my_list[1] = 'zero'
#print(my_list) # -->[1, 'zero', ['three', 4], 5, 6, 7]
#
## ADDING NEW ITEM TO THE LIST USING .append
#another_list.append('eleven')
#print(another_list) # -->[1, 'two', ['three', 4], 5, 6, 7, 'eight', 9, 'ten', 'eleven']
#
## REMOVING ITEM FROM THE LIST USING .pop(), by DEFAULT IT REMOVES (-1) ELEMENT
## CAN REMOVE PARTICULAR ELEMENT BY PASSING INDEX POSITION
#another_list.pop(2)
#print(another_list) # -->[1, 'two', 5, 6, 7, 'eight', 9, 'ten', 'eleven']
#
## SORTING USING .sort() -->mutates and sorted(arg) --> doesnt mute
#new_list = [4,2,5,3,6,2,9]
#sorted(new_list)
#print(new_list) # NO CHANGE -->[4,2,5,3,6,2,9]
#new_list.sort()
#print(new_list) # MUTED -->[2, 2, 3, 4, 5, 6, 9]
#
## REVERSE SORTING USING .reverse() -->mutes
#new_list.reverse()
#print(new_list) # -->[9, 6, 5, 4, 3, 2, 2]
##
##
##
########################################################################################
#
#
#
### DICTIONARY ###
'''Dictionaries are UNORDERED mappings for storing objects, it uses KEY-VALUE
OBJECTS of dictionaries retrived by KEY name. UNORDERED and cannot be SORTED.
'''
## #1
#prices_lookup = {'apple': 2.99, 'orange': 1.99, 'milk': 5.8}
#print(prices_lookup['apple']) # -->2.99
#
#
#
## #2
## DICTIONARY ALSO CAN STORE LIST INSIDE IT
#d = {'k1': 122, 'k2':[0,1,4], 'k3': {'insidekey': 100}}
#print(d['k2']) # -->[0,1,4]
#print(d['k2'][2]) # -->4
#print(d['k3']) # -->{'insidekey': 100}
#print(d['k3']['insidekey']) # -->100
#
#
#
## #3
## MAKING A PARTICULAR ELEMENT UPPERCASE
# d = {'key1': ['a', 'b', 'c']}
# mylist = d['key1'] # mylist-->['a', 'b', 'c']
# letter = mylist[2] # -->'c'
# print(letter)
# print(letter.upper()) # -->'C' # DOESNT MUTE
# print(letter) # --'c' # NO CHANGES HAPPENED
# # IN ORDER TO MUTE
# a = letter.upper() # WILL BE ASSIGNED TO a
# print(a) # --> 'C'
#
#
#
#### #4
## APPENDING NEW KEY
#d = {'k1':100, 'k2':200}
#d['k3'] = 300 # -->{'k1': 100, 'k2': 200, 'k3': 300}
#print(d) 
#
#
#
#### #5
## OVERWRITING NEW VALUE
# d = {'k1': 100, 'k2': 200, 'k3': 300}
# d['k1'] = 'new value' #  -->{'k1': 'new value', 'k2': 200, 'k3': 300}
#print(d)
#
#
#
#### #6
## GETTING KEYS d.keys()
# d = {'k1': 100, 'k2': 200, 'fruit':'apple'}
# print(d.keys()) # -->dict_keys(['k1', 'k2', 'fruit']) #tuple
#
#
#
### #7
### GETTING VALUES d.values()
# d = {'k1': 100, 'k2': 200, 'fruit': 'orange'}
# print(d.values()) # -->dict_values([100, 200, 'orange']) #tuple
#
#
#
### #8
## PAIRING ITEMS IN TUPLE d.items()
d = {'k': 100, 'k3': 400, 'fruit': 'apple'}
print(d.items())
# -->dict_items([('k', 100), ('k3', 400), ('fruit', 'apple')])
#
#
#
###############################################################################
#
#
#
### TUPLE ###














































