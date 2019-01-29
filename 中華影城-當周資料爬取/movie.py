from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get('https://movies.yahoo.com.tw/theater_result.html/id=99', headers=headers)  # 網址下面-參考Beauty版
soup = BeautifulSoup(res.text, 'html.parser')
title = soup.select('.theaterlist_area')
print("戲院資訊:"+title[0].text)
title2 = soup.find_all('div','release_info')
for i in title2:
    print(i.find('a').text,i.find('div','en').text,i.find('ul','theater_time').text,i.find('div','leveltext').text)

image = soup.find_all('div','release_foto')


for z in image:     #抓取圖片
    #print(z.select('img[src$=jpg]'))
    for q in z.select('img[src$=jpg]'):
        print(q['src'])
        filename = q['src'].split('/')[11]
        img = urlopen(q['src'])
        with open('./123/' + str(filename), 'wb') as f:
             f.write(img.read())