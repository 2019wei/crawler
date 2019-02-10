from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

headers = {  'user-agent' :  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

res = requests.get('https://www.toyota.com.tw/', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

raw_content = soup.find('div', 'content ON')
items = raw_content.select('.item')

def get_content():
    format_content = []
    for item in items:
        item_name = item.select('span .name')[0].text
        item_price = item.select('span .price')[0].text
        item_img_link = item.select('img')[0].get('src')
        format_content.append('name: {}, price: {}, image: https:{}'.format(item_name, item_price, item_img_link))
    return format_content

format_items = get_content()

for format_item in format_items:
    print(format_item)
