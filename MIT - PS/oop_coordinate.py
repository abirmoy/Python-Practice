# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 23:38:27 2019

@author: Abirmoy
"""

class Coordinate(object):
    # METHOD, PARAMETER INSIDE THE MATHOD CALLED ATTRIBUTE(here: x,y are ATTRIBUTE)
    def __init__ (self, x, y): # self IS ALWAYS AN INSTANCE OF AN OBJECT THAT WE R GOING TO OPERATION ON
        self.x = x
        self.y = y
    def distance (self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>' 

# CRETING OBJECT
c = Coordinate(3,4) # c IS THE OBJECT OF CLASS Coordinate
zero = Coordinate(0,0) # ANOTHER OBJECT zero
print(c.distance(zero))
print(c.x) # USE DOT TO ACCESS AN ATTRIBUTE OF INSTANCE C
print(c) # WILL RETURN WHAT WE DEFINED AT __str__ METHOD
print(isinstance(c, Coordinate)) # CHECKING IF AN OBJECT IS A COORDINATE, IF WILL RETURN TRUE