# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:30:11 2019

@author: Rivatech
"""

class R:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        
    def area(self):
        return self.l * self.w
    
class S(R):
    def __init__(self, l):
        super().__init__(l, l)
        
    def area(self):
        return self.l * self.l
    
s = S(4)
print("s area ", s.area())

r = R(2, 3)
print("r area ", r.area())




