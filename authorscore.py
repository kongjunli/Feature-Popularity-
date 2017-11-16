#-*- coding: utf-8 -*-
import sys
import re
import logging
import math
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
class GetAuthor():
    def getAuthor(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select author,scan from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyAuthor(self,authorscore,author):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set authorscore=%f where author="%s"'%(authorscore,author)
        cursor.execute(sql) 
        db.commit()  
        db.close()
        
a=GetAuthor()
author=a.getAuthor()
d={}
ds={}
dn={}
for ca in author:
    if d.has_key(ca[0]):
        d[ca[0]]+=1
    else:
        d[ca[0]]=1
    if ds.has_key(ca[0]):
        ds[ca[0]]+=ca[1]
    else:
        ds[ca[0]]=ca[1]
for key in d:
    dn[key]=math.log(ds[key]/d[key],math.e)
for ca in author:
    a.modifyAuthor(dn[ca[0]],ca[0])
    
