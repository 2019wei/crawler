中油天然氣事業部-歷年天然氣價格資料 [點我](https://web.cpc.com.tw/division/lngb/oil-more8.aspx)

#hwhw4.py  這次主要是先把 1.工業用戶2.瓦斯公司3.汽電共生4.直營家庭 都不為0的資料抓出來 各自為list 然後再匯入mysql資料中，

在利用python呼叫mysql裡面的數據進行繪圖(參照hwhw3.py)。

    from bs4 import BeautifulSoup
    import requests
    import pymysql
    
    conn=pymysql.connect('localhost','root','#my','historygasprice2')
    
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









![enter image description here](https://github.com/2019wei/crawler/blob/master/%E6%AD%B7%E5%B9%B4%E5%A4%A9%E7%84%B6%E6%B0%A3%E5%83%B9%E6%A0%BC%E6%B3%A2%E5%8B%95%E5%9C%96/pic.png?raw=true)
