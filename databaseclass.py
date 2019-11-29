# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 15:27:18 2019

@author: Rivatech
"""
import pymysql


class Database:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        
    def connectdb(self):
        db1 = pymysql.connect(host = self.host, 
                        port = self.port, 
                        user = self.user, 
                        password = self.pwd, 
                        database = self.db)
        return db1.cursor()
    
    def executedb(self, db1, query):
        db1.execute(query)
        print(db1.fetchall())
        
        
d1 = Database("localhost", 
              3333, 
              "root", 
              "mysqlpassword", 
              "jpmc1")

query = "SELECT * FROM `emp`"
db1 = d1.connectdb()
d1.executedb(db1, query)

"""





class Database:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        
    def run(self, query):
        with pymysql.connect(host = self.host, 
                        port = self.port, 
                        user = self.user, 
                        password = self.pwd, 
                        database = self.db) as obj:
            obj.execute(query)
            res = obj.fetchall()
            print(res)
        
        
        
d1 = Database("localhost", 
              3333, 
              "root", 
              "mysqlpassword", 
              "jpmc1")

query = "SELECT * FROM `emp`"
d1.run(query)





class Database:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db
        
    def connectdb(self, query):
        db1 = pymysql.connect(host = self.host, 
                        port = self.port, 
                        user = self.user, 
                        password = self.pwd, 
                        database = self.db)
        db1.execute(query)
        print(db1.fetchall())
#        return db1
    
    def executedb(self, db1, query):
        db1.execute(query)
        print(db1.fetchall())
        
        
d1 = Database("localhost", 
              3333, 
              "root", 
              "mysqlpassword", 
              "jpmc1")

query = "SELECT * FROM `emp`"
db1 = d1.connectdb(query)

#d1.executedb(db1, query)


"""