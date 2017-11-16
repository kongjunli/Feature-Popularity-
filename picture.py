# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:59:38 2017

@author: kjl
"""
import gensim
import numpy as np
import pandas as pd
import jieba
import mysql.connector
from gensim.models import word2vec
import logging
from scipy import stats, integrate
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
sns.set(color_codes=True)
class GetData():
    def Data(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select sentiment,logscan from spiderdb.paper'              
        cursor.execute(sql)
        data=cursor.fetchall()
        return data

obj=GetData()
datas=obj.Data()

###
"""
'''
logscan分布图 logscan><8
'''
###

plt.title('Log-normal Distribution')
sns.distplot(datas);
plt.xlabel(' Logarithmic Transformation of View')
plt.ylabel('Probability density')
a=[]
for d in datas:
    a.append(d[0])
data=pd.Series(a)
#print data.describe()
print data.describe()
plt.text(13.6, 0.5, r'$mu=11.94906$')
plt.text(13.6,0.4,r'$sigma=1.39431$')
plt.show()


"""
###

"""
#未标准化的authorscore与logscan核密度图 logscan>8.8
"""

X=[]
Y=[]

for d in datas:

    x=d[0]
    y=d[1]
    X.append(x)
    Y.append(y)
tt={"Title Sentiment Score" : X,
   "Logarithmic Transformation of View" : Y}
data=pd.DataFrame(tt)

sns.boxplot(x='Title Sentiment Score',y='Logarithmic Transformation of View',data=data);

#sns.jointplot(x="Title Length", y="Logarithmic Transformation of View", data=data)
