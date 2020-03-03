# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 21:55:06 2019

@author: Abirmoy
"""

capital_world = {}

capital_asia = {'Bangladesh':'Dhaka', 'India': 'Dellhi', 'China': 'Beijing'}
capital_europe = {'England': 'London', 'Italy': 'Rome', 'Ireland': 'Dublin'}

capital_world.update(capital_asia)
print(capital_world)
capital_world.update(capital_europe)
print(capital_world)
