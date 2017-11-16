# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:11:21 2017

@author: kjl
"""
from pandas import Series,DataFrame
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_selection import SelectFromModel
from numpy import array
from numpy import argmax
import sys
import re
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import RandomizedLasso
import logging
sys.path.append('../')
import MySQLdb as md
import mysql.connector
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
import numpy as np
from sklearn.linear_model import RidgeCV
from sklearn.cross_validation import train_test_split
from sklearn.feature_selection import RFE
class GetData():
    def Data(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select month,weekofmonth,day,authorscore,categoryscore,titlewordcount,summarywordcount,titlescore,summaryscore,titlepolarity,logscan from spiderdb.paper'              
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
       X.append(datas[i][0:10])
       Y.append(datas[i][10])
    except:
        continue
x_train, x_test, y_train, y_test = train_test_split(X, Y,random_state=1)
ridgecv = RidgeCV(alphas=[0.01,0.5,3,5,7,10,100,1000,7000,5000,3000])
names=['month','weekofmonth','day','authorscore','categoryscore','titlewordcount1','summarywordcount1','titlescore','summaryscore','titlepolarity']
#rf = RandomForestRegressor(n_estimators=20, max_features=2)
#rf.fit(X,Y)
#print(sorted(zip(map(lambda x: "%.4f"%x, rf.feature_importances_), names), reverse=True))

ridge =Ridge(alpha=7)
ridge.fit(x_train,y_train) #X为训练集 Y为目标值
print ("Ridge model: ", (ridge.coef_),names)
