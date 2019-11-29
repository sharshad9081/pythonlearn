# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 16:17:43 2019

@author: Rivatech
"""

class A:
    def __init__(self):
        self.__priv = "i am private"
        self._prot = "i am protected"
        self.pub = "i am public"
        print(self.__priv)
        
obj = A()
print(obj.pub)
#print(obj.__priv)
print(obj._prot)