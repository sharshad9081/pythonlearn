# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 12:27:29 2019

@author: Rivatech
"""
#with open(r"C:\Users\Rivatech\Desktop\Ars\filepy.txt", "w") as fobj:
#    fobj.write("test")
    

    
#with open(r"C:\Users\Rivatech\Desktop\Ars\filepy.txt", "w") as fobj:
#    fobj.write("test1\n")
#    fobj.write("test2\n")
#    
#    
#with open(r"C:\Users\Rivatech\Desktop\Ars\filepy.txt", "r") as fobj1:
#    for line in fobj1:
#        print(line)
        
#with open(r"C:\Users\Rivatech\Downloads\annual-enterprise-survey-2018-financial-year-provisional-csv (1).csv", "r") as fobj:
#    alist = []
#    for line in fobj:
#        data = line.split(",")
#        alist.append(data[5])
#    aset = set(alist)
#    print(aset)
        
#with open(r"C:\Users\Rivatech\Downloads\userdata1.parquet", "r") as fobj:
#    for line in fobj:
#        print(line)
        
#        ['2013', 'Level 3', 'ZZ11', 'Food product manufacturing', 'Percentage', 'H40', 'Return on total assets', 'Financial ratios', '5', '"ANZSIC06 groups C111', ' C112', ' C113', ' C114', ' C115', ' C116', ' C117', ' C118', ' and C119"\n']
#['2013', 'Level 3', 'ZZ11', 'Food product manufacturing', 'Percentage', 'H41', 'Liabilities structure', 'Financial ratios', '46', '"ANZSIC06 groups C111', ' C112', ' C113', ' C114', ' C115', ' C116', ' C117', ' C118', ' and C119"\n']



import urllib.request

link = "http://samplecsvs.s3.amazonaws.com/Sacramentorealestatetransactions.csv"
filename = link.split("/")[-1]
urllib.request.urlretrieve(link)
#with open(filename, "r") as fobj:
with open(r"C:\Users\Rivatech\Downloads\Sacramentorealestatetransactions.csv", "r") as fobj:
    adict = {}
    for line in fobj:
        line = line.strip()
        data = line.split(",")
        num = 0
        print(type(adict.get(data[1])))
        if not isinstance(adict.get(data[1]), NoneType):
            num = adict.get(data[1])
            adict.update(data[1], num+1)
#        alist.append(data[1])
#    aset = set(alist)
    print(adict)
        

