#-*- coding: utf-8 -*-
import sys
import logging
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
import jieba
import xlrd
import math
class GetTitle():
    def getTitle(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select title from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyTitle(self,count,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set titletoplocation=%f where id=%d'%(count,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
data = xlrd.open_workbook('C:\Users\kjl\Desktop\TOPWORDSTitlecixingall.xls')
table=data.sheet_by_name(u'location')
topwords={}
for i in range(50):
    topwords[table.row_values(i)[0]]=table.row_values(i)[2]
t=GetTitle()
titles=t.getTitle()
j=0
for title in titles:
    j=j+1
    sum=0
    title=jieba.cut(title[0])
    ltitle=list(title)
    for top in topwords:
        sum+=ltitle.count(top)*topwords[top]
    t.modifyTitle(sum/100,j)
    
      
    
