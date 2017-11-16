# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:36:26 2017

@author: kjl
"""
from numpy import array
from numpy import argmax
from keras.utils import to_categorical
import sys
import re
import datetime
import logging
sys.path.append('../')
import MySQLdb as md
import mysql.connector
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
import numpy as np
###
"""
class GetTime():
    def getTime(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select weekofmonth from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyHotDay(self,day,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set hotday=%s where id=%d'%(day,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
t=GetTime()
time=t.getTime()
data=[]
encoded=to_categorical(time)
print encoded
###
"""
"""
for tt in time:
    data.append(tt)
    encoded=to_categorical(data)
    return encoded    
"""
###
class GetData():
    def Data(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select month,weekofmonth,day,authorscore,categoryscore,summarywordcount,titlewordcount,titletoppeoplename,titletoporganization,titletoplocation,titletopspecial,sumtoppeoplename,sumtoporganization,sumtoplocation,sumtopspecial,titlepolarity,logscan from spiderdb.paper'              
        cursor.execute(sql)
        data=cursor.fetchall()
        return data   

obj=GetData()
datas=obj.Data() 
X=[]
Y=[]
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
for i in range(len(datas)):
    try:
       X.append(datas[i][0:16])
       Y.append(datas[i][16])
    except:
        continue
names=['month','weekofmonth','day','authorscore','categoryscore','summarywordcount','titlewordcount','titletoppeoplename','titletoporganization','titletoplocation','titletopspecial','sumtoppeoplename','sumtoporganization','sumtoplocation','sumtopspecial','titlepolarity']
ridge = Ridge(alpha=7)
ridge.fit(X,Y)
print ("Ridge model: ", (ridge.coef_),names)