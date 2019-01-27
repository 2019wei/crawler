# Welcome to Clawer!
**爬蟲測試區~小小新手的爬蟲練習**

TOYOTA購車查詢 https://www.toyota.com.tw/offer.aspx - 車款展示間

    import requests
    
    from bs4 import BeautifulSoup
    
      
    
    res = requests.get('https://www.toyota.com.tw/offer.aspx') #網頁網址
    
    soup = BeautifulSoup(res.text, 'html.parser')  
    
      
    
    img = soup.find('ul', {'class':'list'}) #找到class = list的地方 上層為ul
    
    name = soup.find_all('span','text') #把span的內容抓出來
    
    for car in name: #跑for loop ,這個name就是這個list 
    
    print(car.find('span', {'class': 'name'}).text,'--價格:', car.find('span', {'class': 'price'}).text) #印出這屬性 class的內容 和 裡面價格的部分
    
    for imgs in img.select('img'):
    
    print(imgs['alt'],'--圖片網址:','https:'+ imgs['src'])

 
  [測試網址](https://repl.it/repls/QualifiedEveryDeprecatedsoftware)![enter image description here](https://github.com/2019wei/crawler/blob/master/%E6%93%B7%E5%8F%96.PNG?raw=true)
  

 中華電影城https://movies.yahoo.com.tw/theater_result.html/id=99?guccounter=1 
#當日電影時刻表     地址：雲林縣斗六市雲林路二段19號

 

> Blockquote

    import requests
    from bs4 import BeautifulSoup
    
    res = requests.get('https://movies.yahoo.com.tw/theater_result.html/id=99')
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.find_all('div',{'class':'release_info'})
    img = soup.find_all('div',{'class':'release_foto'})
    
    for name1 in title:
        print("片名:" + name1.find('a').text,name1.find('div','en').text,name1.find('div','leveltext').text, name1.find('ul','theater_time').text)
        
        
    for imgs in img:
        print(imgs.img['src'])

![enter image description here](https://github.com/2019wei/crawler/blob/master/%E6%93%B7%E5%8F%961.PNG?raw=true)
[測試網址](https://repl.it/repls/TrustingElectricCurrencies)
