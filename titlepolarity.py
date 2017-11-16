# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 10:49:51 2017

@author: kjl
"""

from collections import defaultdict
import os
import re
import jieba
import codecs
import MySQLdb as md
import mysql.connector
import logging
"""连接
mysql
"""
logging.basicConfig(level=logging.INFO)
class GetTitle():
    def getTitle(self):
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='select title from spiderdb.paper'               
        cursor.execute(sql)
        data=cursor.fetchall()
        return data
    def modifyTitlePolarity(self,titlepolarity,i):
        #i is the id,count is the wordcount
        db=mysql.connector.connect(host='127.0.0.1',user='root',password='lkmn159357',database='spiderdb',charset='utf8')
        cursor=db.cursor()
        Content=[]
        sql='update spiderdb.paper set titlepolarity=%f where id="%s"'%(titlepolarity,i)
        cursor.execute(sql) 
        db.commit()  
        db.close()
"""
1. 文本切割
"""

def sent2word(sentence):
    """
    Segment a sentence to words
    Delete stopwords
    """
    segList = jieba.cut(sentence)
    segResult = []
    for w in segList:
        segResult.append(w)

    stopwords =open('C:\\Users\\kjl\\Desktop\\wordsdict\\stop_words.txt')
    newSent = []
    for word in segResult:
        if word in stopwords.readlines():
            # print "stopword: %s" % word
            continue
        else:
            newSent.append(word)

    return newSent
def listToDist(wordlist):
    data={}
    for x in range(0, len(wordlist)):
        data[wordlist[x]]=x
    return data
"""
2. 情感定位
"""
def classifyWords(wordDict):
    # (1) 情感词
    senList =open('C:\\Users\\kjl\\Desktop\\wordsdict\\BosonNLP_sentiment_score.txt')
    senDict = defaultdict()
    print len(senDict)
    for s in senList.readlines():
        if not s.strip():
            continue
        senDict[s.split(' ')[0]] = s.split(' ')[1]
                
    # (2) 否定词
    notList =open('C:\\Users\\kjl\\Desktop\\wordsdict\\notDict.txt').readlines()
    # (3) 程度副词
    degreeList = open('C:\\Users\\kjl\\Desktop\\wordsdict\\degreeDict.txt')
    degreeDict = defaultdict()
    for d in degreeList.readlines():
        #print d
        if not s.strip():
            continue
        degreeDict[d.split(',')[0]] =d.split(',')[1]
        
    senWord = defaultdict()
    notWord = defaultdict()
    degreeWord =defaultdict()
    for word in wordDict.keys():
        if word in senDict.keys() and word not in notList and word not in degreeDict.keys():
            senWord[wordDict[word]] = senDict[word]
        elif word in notList and word not in degreeDict.keys():
            notWord[wordDict[word]] = -1
        elif word in degreeDict.keys():
            degreeWord[wordDict[word]] = degreeDict[word]
    return senWord, notWord, degreeWord
    
"""
#3. 情感聚合
"""
def scoreSent(senWord, notWord, degreeWord, segResult):
    W = 1
    score = 0
    # 存所有情感词的位置的列表
    senLoc = senWord.keys()
    notLoc = notWord.keys()
    degreeLoc = degreeWord.keys()
    senloc = -1
    # notloc = -1
    # degreeloc = -1

    # 遍历句中所有单词segResult，i为单词绝对位置
    for i in range(0, len(segResult)):
        # 如果该词为情感词
        if i in senLoc:
            # loc为情感词位置列表的序号
            senloc += 1
            # 直接添加该情感词分数
            score += W * float(senWord[i])
            # print "score = %f" % score
            if senloc < len(senLoc) - 1:
                # 判断该情感词与下一情感词之间是否有否定词或程度副词
                # j为绝对位置
                for j in range(senLoc[senloc], senLoc[senloc + 1]):
                    # 如果有否定词
                    if j in notLoc:
                        W *= -1
                    # 如果有程度副词
                    elif j in degreeLoc:
                        W *= float(degreeWord[j])
        # i定位至下一个情感词
        if senloc < len(senLoc) - 1:
            i = senLoc[senloc + 1]
    return score
#data="FreeBuf年终策划：FreeBuf 2014年漏洞分析文章精选"
#worddict=listToDist(sent2word(data))
#senWord, notWord, degreeWord= classifyWords(worddict)
#score=scoreSent(senWord, notWord, degreeWord,sent2word(data))
#print score



i=0
t=GetTitle()
data=t.getTitle()
for tt in data:
    i=i+1
    tt="".join(tt).encode('utf-8')
    worddict=listToDist(sent2word(tt))
    senWord, notWord, degreeWord= classifyWords(worddict)
    score=scoreSent(senWord, notWord, degreeWord,sent2word(tt))
    t.modifyTitlePolarity(score,i)
