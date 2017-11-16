# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:54:23 2017

@author: kjl
"""

import MySQLdb as md
import mysql.connector
import pdb
import numpy as np
import pandas as pd
from scipy import stats,integrate
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
class GetTitlewordcount1():
    def gettitlewordcount(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select titlewordcount from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyTitlewordcount1(self,summarywordcount1,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set titlewordcount1=%f where id="%s"'%(summarywordcount1,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
i=0
t=GetTitlewordcount1()
data=t.gettitlewordcount()
min_max_scaler=preprocessing.MinMaxScaler()
authorscore1=min_max_scaler.fit_transform(data)
for tt in authorscore1:
    i=i+1
    t.modifyTitlewordcount1(tt,i)

    
