# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 13:45:26 2019

@author: Rivatech
"""

from cryptography.fernet import Fernet

#creating key
key = Fernet.generate_key()
print("key: ", key)
fern = Fernet(key)
print("fern: ", fern)

pwd = "welcome@123"
msg = b"welcome@123"
#msg = pwd.encode()
print("msg: ", msg)

encryptedpwd = fern.encrypt(msg)
print("encrypted: ", encryptedpwd)

decryptedpwd = fern.decrypt(encryptedpwd)
print("decryptedpwd: ", decryptedpwd)
print("decrypted: ", decryptedpwd.decode('utf-8'))