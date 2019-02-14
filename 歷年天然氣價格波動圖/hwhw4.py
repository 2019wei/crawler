# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:26:42 2019

@author: user
"""

from bs4 import BeautifulSoup
import requests
import pymysql

conn=pymysql.connect('localhost','root','mysql密碼','historygasprice2')
cursor = conn.cursor()

url='https://web.cpc.com.tw/division/lngb/oil-more8.aspx'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
mydata= soup.find_all('span',attrs={'id':'Showtd'})
myrow=mydata[0].find_all('tr')

mylist=[]


for r in myrow:
    c= r.find_all('td')
    if(len(c[0].text)>0 and len(c[1].text)>0) and \
        (len(c[2].text)>0 and len(c[3].text)>0) \
                    and (len(c[4].text)>0):
        dataList = []
        dataList.append(c[0].text)        
        dataList.append(c[1].text)
        dataList.append(c[2].text)
        dataList.append(c[3].text)
        dataList.append(c[4].text)
        mylist.append(dataList)

i=0
for data in mylist:
    if(i<5000):
        i=i+1
        sql="insert into HistoryGasPrice2 values('{}',{},{},{},{});".format(\
             data[0],data[1],data[2],data[3],data[4])
        cursor.execute(sql)
        conn.commit()
conn.close()
    
    
    
    
