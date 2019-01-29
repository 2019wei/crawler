**#顯示 車款名稱/價格/圖片網址**
 [enter link description here](https://repl.it/repls/IllustriousTechnicalCompilers)
 **#增加自動下載圖片**

    from bs4 import BeautifulSoup  
    import requests  
    from urllib.request import urlopen  
    headers = {  
      'user-agent' :  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'  
    }  
      
    res = requests.get('https://www.toyota.com.tw/',headers=headers) #網址  
    soup = BeautifulSoup(res.text,'html.parser')  
    imgages = soup.select('img[src$=png]')  
    for i in imgages:  
        print('https:'+i['src'])  
        filename = i['src'].split('/')[4]  
        img = urlopen('https:'+i['src'])  
        with open('./123/'+str(filename),'wb') as f:  #./123/放置路徑
            f.write(img.read())
![enter image description here](https://github.com/2019wei/crawler/blob/master/TOYOTA%E8%B3%BC%E8%BB%8A-%E5%9C%96%E7%89%87%E8%87%AA%E5%8B%95%E6%8A%93/%E6%93%B7%E5%8F%96.PNG?raw=true)
