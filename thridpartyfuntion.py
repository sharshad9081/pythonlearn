# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:41:40 2019

@author: Rivatech
"""

import os
import sys
import random
import shutil
import string
"""
for file in os.listdir():
    print(file)
    



for file in os.listdir("C:\\"):
    print(file)
    



filelist = []
dirlist = []
for file in os.listdir():
    if os.path.isfile(file):
        filelist.append(file)
    else:
        dirlist.append(file)
print(filelist)
print(dirlist)





for file in os.listdir():
    if os.path.isfile(file) and file.endswith(".csv"):
        os.unlink(file)
        



for file in os.listdir():
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(file.ljust(40), size)
        



        
print("current dir: ", os.getcwd().rjust(40))
print("user name: ", os.getlogin().rjust(21))
print("OS name: ", os.name.rjust(17))
print("current python version: ", sys.version.rjust(20))
print("current python version: ", sys.version.rjust(20))
print("platform: ", sys.platform.rjust(19))

mod = sys.modules
#for val in mod:
#    print(val)
#print("libraries: ", [x for x in sys.modules])
print(list(map(lambda x : x, sys.modules)))
#print(list(map(lambda x : x+5, alist)))






source = "C:\\Users\\Rivatech\\Desktop\\Ars\\src\\"
destination = "C:\\Users\\Rivatech\\Desktop\\Ars\\dest\\"

os.chdir(source)
for file in os.listdir(source):
    if os.path.isfile(file):
        shutil.copy(file, destination)
        print(file, "copied to ", destination)


#without chdir()
source = "C:\\Users\\Rivatech\\Desktop\\Ars\\src\\"
destination = "C:\\Users\\Rivatech\\Desktop\\Ars\\dest\\"

os.chdir(source)
for file in os.listdir(source):
    if os.path.isfile(file):
        shutil.copy(source + file, destination)
        print(file, "copied to ", destination)




user = input("Enterusername\n")
def pas():
    lletters = string.ascii_lowercase
    uletters = string.ascii_uppercase
    digit = string.digits
    punc = string.punctuation
    l = ''.join(random.choice(lletters) for i in range(0,2))
    u = ''.join(random.choice(uletters) for i in range(0,2))
    d = ''.join(random.choice(digit) for i in range(0,2))
    p = ''.join(random.choice(punc) for i in range(0,2))
    return l + u + d + p
passw = pas()
print(passw)

"""


user = input("Enterusername\n")
def pas():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation) for i in range(0,8))
pasw = pas()
if(pasw.c)
print(passw)