# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 20:53:50 2019

@author: user
"""
import pymysql
import matplotlib.pyplot as pt

db=pymysql.connect("localhost","root","#mysql密碼","HistoryGasPrice2")
cursor=db.cursor()
sql="Select * from HistoryGasPrice2"

listMonth=[]
list1=[]
list2=[]
list3=[]
list4=[]
cursor.execute(sql)
results=cursor.fetchall()
for row in results:
        listMonth.append(row[0])
        list1.append(row[1])
        list2.append(row[2])
        list3.append(row[3])
        list4.append(row[4])
        print("%s,%6.4f,%6.2f,%6.4f,%6.2f"%\
              (row[0],row[1],row[2],row[3],row[4]))

db.close()
pt.figure(num=None,figsize=(6,6),dpi=168,facecolor='w',edgecolor='k')
pt.plot(listMonth,list1,lw=2,label='Industrial user')
pt.plot(listMonth,list2,lw=2,label='Gas company')
pt.plot(listMonth,list3,lw=2,label='electricity symbiosis')
pt.plot(listMonth,list4,lw=2,label='Direct family')
pt.xlabel('month')
pt.ylabel('dollars/cubic meter')
pt.legend()
pt.title("Python Data Science")
pt.show()
