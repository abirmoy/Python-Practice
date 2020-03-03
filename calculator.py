# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:05:49 2019

@author: Abirmoy
"""



tenth = 10
hundrad = pow(tenth, 2)
thousand = pow(tenth, 3) 
万_wan = pow(tenth, 4) 
lakh = pow (tenth, 5)
million = pow(tenth, 6)
crore = pow(tenth, 7)
billion = pow(tenth, 9)

while True:
  x = int(input('Give me number: '))
  result = f'{x} is equvalent to:\n{x/hundrad} Hundrad or \n{x/thousand} Thousand or \n'
  print(result)