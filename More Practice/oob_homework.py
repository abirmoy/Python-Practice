# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:34:18 2019

@author: Abirmoy
"""

class Line:
    
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        return (((x2-x1)**2) + ((y2-y1)**2))**.5
        
        
        
    
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        return (y2-y1)/(x2-x1)
    
    
    
c1 = (3,2)
c2 = (8,10)

li = Line(c1, c2)

x = li.distance()
b = li.slope()


class Cylinder:
    pi = 3.14
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return self.pi*(self.radius**2)*self.height
    
    def surface_area(self):
        return 2*self.pi*self.radius*(self.radius + self.height)


c = Cylinder(2,3)

a = c.volume()
c = c.surface_area()



































