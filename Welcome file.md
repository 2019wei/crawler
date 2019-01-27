---


---

<h1 id="welcome-to-clawer">Welcome to Clawer!</h1>
<p><strong>爬蟲測試區~小小新手的爬蟲練習</strong></p>
<p>TOYOTA購車查詢 <a href="https://www.toyota.com.tw/offer.aspx">https://www.toyota.com.tw/offer.aspx</a> - 車款展示間</p>
<pre><code>import requests

from bs4 import BeautifulSoup

  

res = requests.get('https://www.toyota.com.tw/offer.aspx') #網頁網址

soup = BeautifulSoup(res.text, 'html.parser')  

  

img = soup.find('ul', {'class':'list'}) #找到class = list的地方 上層為ul

name = soup.find_all('span','text') #把span的內容抓出來

for car in name: #跑for loop ,這個name就是這個list 

print(car.find('span', {'class': 'name'}).text,'--價格:', car.find('span', {'class': 'price'}).text) #印出這屬性 class的內容 和 裡面價格的部分

for imgs in img.select('img'):

print(imgs['alt'],'--圖片網址:','https:'+ imgs['src'])
</code></pre>
<p><a href="https://repl.it/repls/QualifiedEveryDeprecatedsoftware">測試網址</a><img src="https://github.com/2019wei/crawler/blob/master/%E6%93%B7%E5%8F%96.PNG?raw=true" alt="enter image description here"></p>
<p>中華電影城https://movies.yahoo.com.tw/theater_result.html/id=99?guccounter=1<br>
#當日電影時刻表     地址：雲林縣斗六市雲林路二段19號</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<p>import requests<br>
from bs4 import BeautifulSoup</p>
<p>res = requests.get(‘<a href="https://movies.yahoo.com.tw/theater_result.html/id=99">https://movies.yahoo.com.tw/theater_result.html/id=99</a>’)<br>
soup = BeautifulSoup(res.text, ‘html.parser’)<br>
title = soup.find_all(‘div’,{‘class’:‘release_info’})<br>
img = soup.find_all(‘div’,{‘class’:‘release_foto’})</p>
<p>for name1 in title:<br>
print(“片名:” + name1.find(‘a’).text,name1.find(‘div’,‘en’).text,name1.find(‘div’,‘leveltext’).text, name1.find(‘ul’,‘theater_time’).text)</p>
<p>for imgs in img:<br>
print(imgs.img[‘src’])<br>
<img src="https://github.com/2019wei/crawler/blob/master/%E6%93%B7%E5%8F%961.PNG?raw=true" alt="enter image description here"><br>
<a href="https://repl.it/repls/TrustingElectricCurrencies">測試網址</a></p>

