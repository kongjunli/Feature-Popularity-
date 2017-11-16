#-*- coding: utf-8 -*-
import sys
import logging
import math
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
class GetScan():
    def getScan(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select scan from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyScan(self,logscan,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set logscan=%f where id=%d'%(logscan,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
s=GetScan()
i=0
scan=s.getScan()
for sc in scan:
    i=i+1
    logsc=math.log(sc[0],math.e)
    s.modifyScan(logsc,i)
    

