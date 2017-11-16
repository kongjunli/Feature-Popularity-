#-*- coding: utf-8 -*-
import sys
import logging
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
import re
class GetSummary():
    def getSummary(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select summary from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyTitle(self,count,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set titlewordcount=%d where id=%d'%(count,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
    def modifySummary(self,count,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set summarywordcount=%d where id=%d'%(count,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
su=[]
ti=[]
a=GetSummary()
summary=a.getSummary()
i=0
for s in summary:
    i=i+1
    s=str(s).decode('utf-8')
    pe= re.findall(ur'[a-zA-Z0-9]+',s) 
    len1=len(pe)
    pc=re.findall(ur'[\u4e00-\u9fa5]',s)
    len2=len(pc)
    l=len1+len2
    a.modifySummary(l,i)
    
    



