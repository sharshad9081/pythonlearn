# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:20:16 2019

@author: Rivatech
"""

#constrcutor in python
# __init__

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        
    def info(self):
        print("name ", self.name)
        print("roll ", self.roll)
        
s1 = Student("asd", 10)
#s1.info()
print(s1.name)
print(s1.roll)