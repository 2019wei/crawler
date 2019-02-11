from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
x= str(input('請輸入網址(先按一個空白再輸入)'))
url = x
res = requests.get(url, headers=headers)  # 網址下面-參考Beauty版
soup = BeautifulSoup(res.text, 'html.parser')
imgages = soup.select('a[href$=jpg]')   # 抓取a連結 href 的網址  #'＄＝結尾'，^=開頭
for i in imgages:                       # 把list一個一個抓出來 for loop
    print(i['href'])
    filename = i['href'].split('/')[3]   # 這邊是下載圖片的開始..split把/切段-因為我命名檔案要用
    img = urlopen(i['href'])             # 打開圖片的連結
    with open('./123/' + str(filename), 'wb') as f:  # /123/是寫讓檔案的位置/後面的wb是寫入文件
        f.write(img.read())                          # 把圖片讀出來 寫進去

# https://www.ptt.cc/bbs/Beauty/M.1548652105.A.240.html