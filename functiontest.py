# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:18:36 2019

@author: Rivatech
"""
"""
def add(arg1):
    return arg1 + 10

sum = add(5)
print(sum)


#lambda is a replacement of single liner function
#inline function
#syntax > functioname = lambda variables : expression
add1 = lambda arg1 : arg1 + 10
sum = add1(5)
print(sum)

"""

add2 = lambda arg1,arg2 : arg1 + arg2
sum = add2(5,10)
print(sum)



alist = [10,20,30,40]
#output : [15,25,35,45]

blist = []
for val in alist:
    blist.append(val + 5)
print(blist)

#map funtion
def incr(x):
    return x+5
print(list(map(incr, alist)))

#lambda
print(list(map(lambda x : x+5, alist)))


#converting list of strings
value = ['1','2','3']
print(list(map(lambda x : int(x), value)))


#  filter
alist = list(range(1,100))
#odd numer
print(list(filter(lambda x : x%2, alist)))
#even numer
print(list(filter(lambda x : x%2 == 0, alist)))

print(list(filter(lambda x : x%x == 0, alist)))