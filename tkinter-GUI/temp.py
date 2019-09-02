from bs4 import BeautifulSoup
import requests
import tkinter as tk
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", width="30", height="5", font=('Arial', 20))
        self.label1= tk.Label(text="", width="30", height="5", font=('Arial', 20))
        self.label1.pack()
        self.label.pack()
        self.update_clock()
        self.root.mainloop()
        
    def update_clock(self):
         res = requests.get('https://www.google.com/search?q=%E6%99%82%E9%96%93&oq=%E6%99%82%E9%96%93&aqs=chrome..69i57j69i61l3.1390j0j7&sourceid=chrome&ie=UTF-8', headers=headers)  # 網址下面-參考Beauty版
         soup = BeautifulSoup(res.text, 'html.parser')
         title2 = soup.find_all('div','gsrt vk_bk dDoNo')
         for i in title2:
            print(i.text)           
            self.label.configure(text='測試:'+i.text)
            self.label1.configure(text='測試1:'+i.text)
            self.root.after(1000, self.update_clock)
app=App()
















    