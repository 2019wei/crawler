from bs4 import BeautifulSoup
import requests
headers = {
  'user-agent' :  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

res = requests.get('https://www.toyota.com.tw/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
title = soup.find('div','content ON')

def img():
    for i in title.select('img'):
         print('https:'+i['src'])

def car():
    for i in title.find_all('span','name'):
         print(i.text)

def price():
    for i in title.find_all('span','price'):
         print(i.text)


car(),price(),img()
