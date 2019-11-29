# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:05:39 2019

@author: Rivatech
"""

#class contains data members and member function
#object is instance of class
#self is instance of object


"""
class Student:
    def displayName(self):
        print("name")
    
    def displayEmpId(self):
        print("id")
        
s1 = Student()
s1.displayName()
s1.displayEmpId()

"""

class Student:
    def displayName(self, name):
#        self.name1 = name
#        print("name ",self.name1)
        print("namee ", name)
    
    def displayEmpId(self, id):
#        self.id1 = id
#        print("id ", self.id1)
        print("idd ", id)
        
s1 = Student()
s1.displayName("ars")
s1.displayEmpId("1")
