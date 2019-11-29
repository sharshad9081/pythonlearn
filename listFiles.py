# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 16:10:58 2019

@author: Rivatech
"""

import os
import subprocess
#alist = os.listdir("C:/Users/Rivatech/Desktop")
#for item in alist:
#    if item.is_file():
#        print("file ", item)
#    else:
#        print("dir ", item)

#for item in list:
#    print(item)
#lista = (os.popen('ls | grep aa').read()).split('\n')
#print(blist)



#with os.scandir("C:/Users/Rivatech/Desktop/Ars") as ob:
#with os.scandir("C:/Users/Rivatech/Desktop") as ob:
#    for entry in ob:
#        if not entry.is_file():
#            print("dir:  ", entry.name)
#        else:
#            print("file: ", entry.name)
            
            



data = subprocess.Popen(['dir'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = str(data.communicate())
print(output)





