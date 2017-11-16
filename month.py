#-*- coding: utf-8 -*-
import sys
import re
import datetime
import logging
import math
sys.path.append('../')
import MySQLdb as md
import mysql.connector
import pdb
class GetTime():
    def getTime(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select pub_time from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyMonth(self,month,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set month=%d where id=%d'%(month,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
    def modifyDay(self,day,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set day=%d where id=%d'%(day,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
    def modifyWeekofmonth(self,weekofmonth,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set weekofmonth=%d where id=%d'%(weekofmonth,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
t=GetTime()
time=t.getTime()
i=0
for ti in time:
    a=[]
    i=i+1
    ###
    """
    matchObj = re.match( r'(.*)-(.*)-(.*)', ti[0].strftime('%Y-%m-%d'), re.M|re.I)
    year=str(matchObj.group(1))
    month=str(matchObj.group(2))
    day=str(matchObj.group(3))
    weekofmonth=(int(day)-1)/7 
    t.modifyMonth(int(month),i)
    #t.modifyDay(int(day),i)
    t.modifyWeekofmonth(weekofmonth,i)
    """
    ###
    """
    计算周几
    """
 
    matchObj = re.match( r'(.*)-(.*)-(.*)', ti[0].strftime('%Y-%m-%d'), re.M|re.I)
    year=str(matchObj.group(1))
    month=str(matchObj.group(2))
    day=str(matchObj.group(3))
    a.append(year)
    a.append(month)
    a.append(day)
    a="".join(a)
    tt=datetime.datetime.strptime(a,'%Y%m%d')
    day=tt.weekday()
    t.modifyDay(day,i)
  

    
