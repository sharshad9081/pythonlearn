# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:01:40 2019

@author: Rivatech
"""
"""
print("enter file name")
val = input()
name = val.split(".")
print("filename : ", name[0])
print("extension : ", name[1])
 







print("Enter any delimited string :")
val = input()
alist = list(val.split(","))
print("List elements are :", alist)
print("Length of the list  :", len(alist))






atup = ()
print("empty tuple :", atup)
alist = list(atup)
alist.append("unix")
print("tuple appended:", alist)
alist.extend(['spark', 'scala','hadoop','sccm'])
print("list appended:", alist)
alist.extend(['c','cpp','java','salesforce','sap','unix'])
print("list appended again:", alist)
alist.remove("java")
print("java removed:", alist)
alist.remove("salesforce")
print("salesforce removed:", alist)
alist.insert(0, "oracle")
print("oracle added:", alist)
alist.insert(5, "mododb")
print("mogodb added:", alist)
print("reverse :", alist[::-1])
print("total :", len(alist))
print("total unix count :", alist.count("unix"))






ntup = (10,20,10,20,30,40,60,70)
print("tuple: ",ntup)
nset = set(ntup)
print("no duplicate tuple: ",nset)





print("Enter first number: ")
anum = input()
print("Enter second number: ")
bnum = input()
a = int(anum)
b = int(bnum)
#a = 5
#b = 6
c = a.__add__(b)

print("sum: ",c)









print("Enter string")
str = input()
print(str.replace("python", "scala"))





alist = [10,20,30,40,50,10]
blist = [40,50,60,70,80]
aset = set(alist)
bset = set(blist)
print("unique: ", aset | bset)
print("common: ", aset & bset)





lang = "perl,unix,hadoop,scala,spark,ruby,go"
print(lang.find("python"))
print(lang.find("unix"))

if (lang.find("python") == -1) :
    print("no")
else :
    print("yes")





questionbank ={
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}
            
print(questionbank['quiz']['sport']['q1']['question'])
print(questionbank['quiz']['maths']['q1']['question'])
print(questionbank['quiz']['maths']['q2']['question'])






book = {"chap1":[10,'UK','Mark'] ,"chap2":[20,'US','Pet']}
alist = book['chap1']
blist = book['chap2']
alist.append("200pages")
blist.append("400pages")
book1 = {"chap1":alist,"chap2":blist}
print(book1)




print("Enter string")
str = input()
print("is it upper: ",str.isupper())
alist = list(str)
print("list: ", alist)
print("center: ", str.center(30))





str = input()
if(str.__contains__("@")):
    print("@")
else:
    print("no")




print("Enter password")
passw = input()
if (len(passw) < 5) :
    print("length of the password should be greater than  5")
    exit()
if (len(passw) > 12):
    print(" length of the password should be less than 12")
    exit()
if(passw.__contains__("@") or passw.__contains__("*") or passw.__contains__("$")):
    print("good")
else:
    print("atleast  one symbol ( @ or * or  $ ) should exist in the password")
    exit()
if(passw.isupper()):
    print("whole password SHOULD not be in upper case")
    exit()





print(list(range(50,1,-1)))
print(list(range(20,0,-2)))




str = "sd"
str.replace
if not (str.startswith("s")):
    print("a")
else:
    print("c")




domains = ["google","www.unix","oracle.com"]
print("before", domains)
for val in domains :
    if not (val.startswith("www.")):
        nval = "www." + val
    else:
        nval = val
    if not (val.endswith(".com")):
        nval += ".com"
    domains.remove(val)
    domains.append(nval)
print("after ", domains)







alist = ["google","oracle","microsoft"]
nlist = []
print("before", alist)
for val in alist:
    print("val",val)
    nval = "www." + val + ".com"
    print("nval",nval)
    nlist.append(nval)
print("after ", nlist)






ydict = {
  "kind": "youtube#searchListResponse",
  "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/PaiEDiVxOyCWelLPuuwa9LKz3Gk\"",
  "nextPageToken": "CAUQAA",
  "regionCode": "KE",
  "pageInfo": {
    "totalResults": 4249,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/QpOIr3QKlV5EUlzfFcVvDiJT0hw\"",
      "id": {
        "kind": "youtube#channel",
        "channelId": "UCJowOS1R0FnhipXVqEnYU1A"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/AWutzVOt_5p1iLVifyBdfoSTf9E\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "Eqa2nAAhHN0"
      }
    },
    {
      "kind": "youtube#searchResult",
      "etag": "\"m2yskBQFythfE4irbTIeOgYYfBU/2dIR9BTfr7QphpBuY3hPU-h5u-4\"",
      "id": {
        "kind": "youtube#video",
        "videoId": "IirngItQuVs"
      }
    }
  ]
}
for key, value in ydict.items():
    if key == "etag":
        print(value)
    elif isinstance(value, list):
        for item in value:
            print(item["etag"])







items =[
{
"id": "0001",
"type": "donut",
"name": "Cake",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" },
{ "id": "1002", "type": "Chocolate" },
{ "id": "1003", "type": "Blueberry" },
{ "id": "1004", "type": "Devil's Food" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5005", "type": "Sugar" },
{ "id": "5007", "type": "Powdered Sugar" },
{ "id": "5006", "type": "Chocolate with Sprinkles" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
},
{
"id": "0002",
"type": "donut",
"name": "Raised",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5005", "type": "Sugar" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
},
{
"id": "0003",
"type": "donut",
"name": "Old Fashioned",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" },
{ "id": "1002", "type": "Chocolate" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
}
]
for val in items:
    for key, value in val["batters"].items():
        for item in value:
            print(item.get("type"), "(", item.get("id"), ")")







adict = {
"id": "0001",
"type": "donut",
"name": "Cake",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" },
{ "id": "1002", "type": "Chocolate" },
{ "id": "1003", "type": "Blueberry" },
{ "id": "1004", "type": "Devil's Food" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5005", "type": "Sugar" },
{ "id": "5007", "type": "Powdered Sugar" },
{ "id": "5006", "type": "Chocolate with Sprinkles" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
}
for key, value in adict.items():
    if key == "batters":
        for item in value["batter"]:
            print(item["type"], "(", item["id"], ")")
    
    






print("Enter ipaddress")
ipstr = input()
if ipstr.count(".") < 3:
    print("Invalid ip .")
else:
    ip = ipstr.split(".")
    for num in ip:
        if not num.isnumeric():
            print("Invalid ip num")
            break
        else:
            if ip[0] in range(0,256) and ip[1] in range(0,256) and ip[2] in range(0,256) and ip[3] in range(0,256):
                print("valid IP")
            else:
                print("invalid IP")
                break

"""

print("Enter ipaddress")
ipstr = input()
if ipstr.count(".") < 3:
    print("Invalid ip .")
else:
    ip = ipstr.split(".")
    for num in ip:
        if not num.isnumeric():
            print("Invalid ip num")
            break
        else:
            if int(num) in range(0,256):
                continue
            else:
                print("invalid IP")
                break
    print("valid ip")




