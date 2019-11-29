# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:06:17 2019

@author: Rivatech
"""
import re

"""
with open("language.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        if re.search("pyt*hon", line):
            print(line)
        if re.search("py.hon", line):
            print(line)
        if re.search("pyt?hon", line):
            print(line)
        if re.search("pyt+hon", line):
            print(line)
        if re.search("py.hon", line):
            print(line)
        if re.search("python$", line):
            print(line)


name = "31244 154, 1222 145"
pattern = ""
"""

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
email = "ars.hal@gmail.com"
if re.search(regex, email):
    print("valid")
else:
    print("invalid")