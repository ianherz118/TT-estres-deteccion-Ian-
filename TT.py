#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

############### CONFIGURAR ESTO ###################
db = pymysql.connect("database_host","username","password","database_name")
##################################################
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : {0}".format(data))
db.close()
############### CONFIGURAR ESTO ###################
db = pymysql.connect("database_host","username","password","database_name")
##################################################
cursor = db.cursor()
sql = "INSERT INTO test(id, name, email) \
   VALUES (NULL,'{0}','{1}')".format("cosme","testmail@sever.com")
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()
db.close()
############### CONFIGURAR ESTO ###################
db = pymysql.connect("database_host","username","password","database_name")
##################################################
cursor = db.cursor()
sql = "SELECT * FROM test \
WHERE id > {0}".format(0)
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
   id = row[0]
   name = row[1]
   email = row[2]
   print ("id = {0}, name = {1}, email = {1}".format(id,name,email))
db.close()

