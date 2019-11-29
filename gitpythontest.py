# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:46:11 2019

@author: Rivatech
"""

import requests
import json

url = "https://api.github.com/"
endpoint = "users/sharshad9081/gists"

response = requests.get(url + endpoint, 
                        auth=('sharshad9081', '1530265a2825d9a3df338f4e8b299d4dc0c0c902'))
alist = response.json()
for adict in alist:
#    for key, value in adict.items():
#        print(key)
    
    for key, value in adict.items():
        if key == "files":
            for key, value in value.items():
                for key, value in value.items():
                    if key == "filename":
                        print(value)
    
#    for key, value in adict.items():
#        if key == "files":
#            bdict = value
#            for key, value in bdict.items():
#                cdict = value
#                for key, value in cdict.items():
#                    if key == "filename":
#                        print(value)
                    
                    
                    
                    
#    print(fil.get("files"))
#print(response.json())


#data = json.loads(response.text)
#
#for key, value in data.items():
#    print(key.ljust(30), value)



#url = "https://api.github.com/"
#endpoint = "gists"
#
#payload = {
#  "description": "Hello World Examples",
#  "public": True,
#  "files": {
#    "hello_world.py": {
#      "content": "class HelloWorld:\n\n    def __init__(self, name):\n        self.name = name.capitalize()\n       \n    def sayHi(self):\n        print \"Hello \" + self.name + \"!\"\n\nhello = HelloWorld(\"world\")\nhello.sayHi()"
#    }
##    "hello_world.rb": {
##      "content": "class HelloWorld\n   def initialize(name)\n      @name = name.capitalize\n   end\n   def sayHi\n      puts \"Hello !\"\n   end\nend\n\nhello = HelloWorld.new(\"World\")\nhello.sayHi"
##    }
##     "hello_world.rb": {
##      "content": "class HelloWorld\n   def initialize(name)\n      @name = name.capitalize\n   end\n   def sayHi\n      puts \"Hello !\"\n   end\nend\n\nhello = HelloWorld.new(\"World\")\nhello.sayHi"
##    }
#  }
#}
#     
#response = requests.post(url + endpoint, 
#                        data = json.dumps(payload), 
#                        auth=('sharshad9081', '1530265a2825d9a3df338f4e8b299d4dc0c0c902'))
#print(response.text)


"""

url = "https://api.github.com/"
endpoint = "/gists"
filen = "helloworld.py"
filename = filen.split(".")[0]
with open(filen) as file:
    dat = file.read()
payload = {
  "description": filename,
  "public": True,
  "files": {
    filen: {
      "content": dat
    }
#    "hello_world.rb": {
#      "content": "class HelloWorld\n   def initialize(name)\n      @name = name.capitalize\n   end\n   def sayHi\n      puts \"Hello !\"\n   end\nend\n\nhello = HelloWorld.new(\"World\")\nhello.sayHi"
#    }
#     "hello_world.rb": {
#      "content": "class HelloWorld\n   def initialize(name)\n      @name = name.capitalize\n   end\n   def sayHi\n      puts \"Hello !\"\n   end\nend\n\nhello = HelloWorld.new(\"World\")\nhello.sayHi"
#    }
  }
}
response = requests.post(url + endpoint,
                         data = json.dumps(payload), 
                         auth=('sharshad9081', '1530265a2825d9a3df338f4e8b299d4dc0c0c902'))
print(response.json())


"""


