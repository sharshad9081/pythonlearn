# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:01:18 2019

@author: Rivatech
"""

#fixed args
def display(arg1, arg2):
    print(arg1, arg2)
    
display(10,20)


#default args
#function overloading
def display1(arg1=0, arg2=0):
    print(arg1, arg2)

display1()
display1(10)
display1(10,20)


#keyword args
def display2(arg1, arg2):
    print(arg1, arg2)

display1(arg2=20, arg1=10)


#variable length args
def display3(*data):    #variable prefixed with * is tuple
    for val in data:
        print(val)

display3(10,20,30,40)

def display4(**data):    #variable prefixed with ** is dictionary
    for key, val in data.items():
        print("key:", key, "& val:", val)

display4(a1=20,a2=40)


