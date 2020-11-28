# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 23:43:58 2020

@author: ThinkPad
"""

class Point :
    # Create a new Point , at coordinates x, y
    def __init__ (self, x=0, y=0):
        # Create a new point at x , y
        self.x = x
        self.y = y
    def distance_from_origin(self):
        # Compute my distance from the origin
        return((self.x ** 2) + (self.y ** 2 )) ** 0.5
    def __str__(self): # Pr int the point
        return "({0}, {1})".format(self.x, self.y)
    def slope_from_origin(self):
        # Calculate the slope from(0,0)
        if self.x != 0:
            return self.y/self.x
        else:
            return False
    
    def get_line_to(self, p):
        # Calculate the line confirmed with point p
        if self.x != p.x:
            self.a = (self.y - p.y)/(self.x - p.x)
            self.b = self.y - self.x * self.a
            return "({0}, {1})".format(self.a, self.b)
        else:
            return False