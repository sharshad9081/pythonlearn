# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:38:30 2019

@author: Rivatech
"""

#alist = [10,20,"abc"]
alist = [10,20]
print(alist)

alist[0] = "test"
#alist[2] = 25
print("changes", alist)

atup = (10,20)
print(atup)

atup = 2
print("change", atup)


name = "python program"

print(name.capitalize())
print(name.center(5))
print(name.center(20, "."))
print(name.count('k'))
print(list(name))
print(tuple(name))
print(set(name))

num = 50
print(num)
print(num)
print("changes ", num+2)

str = "abc"
print(str)
print(str[0])
print("change ", str+ "ac   ")


aname = "This is {}"
print(aname.format("sparta", 12))
print(aname.format(10, 23))

bname = " test "
print("hi", bname.strip(), "hi")
print("hi", bname.lstrip(), "hi")
print(bname.strip().__len__())


anum = 50
print(anum.bit_length())

blist = [10, 12, "xyz"]
print(blist.remove(10))
print(blist.pop(0))
print(blist)

clist = [10, 12, 7]
clist.sort()
print(clist)

dlist = ["br", "cv", "ac"]
dlist.sort()
print(dlist)

btup = (10, 5, None)
print(btup)

adic = {1:'abc', 2:'xyz'}
print(adic)
print(adic.keys())
print(adic.items())
print(adic.get(0))
print(adic.get(0), "def")

bdic = {"c1":3, "c2":4}
adic.update(bdic)
print(adic)
print(bdic)
bdic.setdefault('c3')
print(bdic)
bdic.setdefault('c3',5)
print(bdic)




aset = {10,20,10,30,20}
print(aset)
aset.add(90)
print(aset)
bset={30,40,50,40}
print(aset.union(bset))
print(aset.intersection(bset))
print(aset.difference(bset))

print(aset & bset)
print(aset | bset)
print(aset - bset)
print(bset - aset)







#dir(__builtins__)
