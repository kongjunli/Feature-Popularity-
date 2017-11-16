#-*- coding: utf-8 -*-
import sys
import scipy
from scipy import stats
import MySQLdb as md
import mysql.connector
import pdb
import numpy as np
import matplotlib.pyplot as plt
class GetScan():
    def getScan(self):
        db=mysql.connector.connect(user='root',password='lcy492',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select pub_time,scan from spiderdb.freebuf where pub_time>="2015-02-01" and pub_time<="2015-02-31"'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
d0=[]
d1=[]
d2=[]
d3=[]
d4=[]
d5=[]
d6=[]
scan=GetScan()
data_raw=scan.getScan()
for d in data_raw:
    if int(d[0])==0:
        d0.append(int(d[1]))
    if int(d[0])==1:
        d1.append(int(d[1]))
    if int(d[0])==2:
        d2.append(int(d[1]))
    if int(d[0])==3:
        d3.append(int(d[1]))
    if int(d[0])==4:
        d4.append(int(d[1]))
    if int(d[0])==5:
        d5.append(int(d[1]))
    if int(d[0])==6:
        d6.append(int(d[1]))
data_to_plot=[d0,d1,d2,d3,d4,d5,d6]
fig = plt.figure(1, figsize=(9, 6))
ax = fig.add_subplot(111)
#plt.plot([0,1,2,3,4,5,6],[153372.06074766355,151759.89871611982,157024.88592057762,162222.92412746587,150321.79836734693,161548.2511013216,150004.95792079208])
bp = ax.boxplot(data_to_plot,patch_artist=True)
for box in bp['boxes']:
    box.set( color='#7570b3', linewidth=2)
    box.set( facecolor = '#1b9e77' )
for whisker in bp['whiskers']:
    whisker.set(color='#7570b3', linewidth=2)
for median in bp['medians']:
    median.set(color='#b2df8a', linewidth=2)
for flier in bp['fliers']:
    flier.set(marker='o', color='#e7298a', alpha=0.5)
ax.set_xticklabels(['Mon.', 'Tue.', 'Wed.','Thu.','Fri.','Sat.','Sun.'])

plt.title("scan's boxplot")
plt.ylabel('scan_num')
fig.savefig('week1.png', bbox_inches='tight')
    
        
