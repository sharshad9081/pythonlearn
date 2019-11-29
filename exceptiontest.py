# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:11:41 2019

@author: Rivatech
"""

import csv
import sys
#Sacramentorealestatetransactions.csv
try:
    citylist = list()
    
    filename = input("Ener filename\n")
    with open(filename) as fobj:
        
#        lines = fobj.readlines()
#        for line in lines:
#            data = line.split(",")
#            citylist.append(data[1])
            
#        for data in fobj:
#            line = data.split(",")
#            citylist.append(line[1])
            
        reader = csv.reader(fobj)
        for line in reader:
            citylist.append(line[1])
            
    for city in set(citylist):
        print(city)
    
except (TypeError, ValueError, FileNotFoundError) as error:
#    if not isinstance(error, FileNotFoundError):
#        print("instance of ")
#    print("Error type: ", type(error))
    print("Error logsf: ", error)
    print(sys.exc_info())
#except TypeError as error:
#    print("TypeError: ", error)
#    print(sys.exc_info())
#except ValueError as error:
#    print("ValueError: ", error)
#    print(sys.exc_info())
#except FileNotFoundError as error:
#    print("FileNotFoundError: ", error)
    print(sys.exc_info())
except Exception as error:
    print("Exception: ", error)
    print(sys.exc_info())
    
    