# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 11:27:42 2019

@author: Rivatech
"""

import getpass
import stdiomask

#passw = getpass.getpass("Enter password\n")
#print(passw)


#passw = stdiomask.getpass("Enter password\n")
#print(passw)

passw = stdiomask.getpass("Enter password\n", mask="$")
print(passw)