# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
import tkinter as tk
import json
import time
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="", width="30", height="2", font=('Arial', 40,"bold"))
        self.label1= tk.Label(text="", width="30", height="2", font=('Arial', 40,"bold"))
        self.label2= tk.Label(text="", width="30", height="2", font=('Arial', 40,"bold"))
        self.label3= tk.Label(text="", width="30", height="2", font=('Arial', 40,"bold"))
        self.label4= tk.Label(text="", font=('Arial', 40,"bold"))
        self.label.pack()
        self.label1.pack()
        self.label2.pack()
        self.label3.pack()
        self.label4.pack()
        self.update_clock()
        self.root.mainloop()
        
    def update_clock(self):
      try:  
        res = requests.get('http://secure3estatics.ddns.net:9001/vclamp/device/gugugoo/84402480', headers=headers)  # 網址下面-參考Beauty版
        res1 = requests.get('http://secure3estatics.ddns.net:9001/vclamp/device/gugugoo/84743355', headers=headers)
        #print(json.loads(res.text))
        f2 = json.loads(res.text)
        f3 = json.loads(res1.text)
        #print(f2["data"][0]["current"])
        #print(f2["data"][1]["current"])
        #print(f2["data"][2]["status"])
        now = time.strftime("%m/%d %H:%M:%S")
        a = str(f2["data"][0]["current"]/1000)
        b = str(f2["data"][1]["current"]/1000)
        c = str(f2["data"][2]["current"]/1000)
        d = str(f3["data"][0]["current"]/1000)
        a1 = str(f2["data"][0]["status"])
        b1 = str(f2["data"][1]["status"])
        c1 = str(f2["data"][2]["status"])
        d1 = str(f3["data"][0]["status"])
        
        if  a1 =='True':
              self.label.configure(text='電宰_貯冰機_R:'+ '　'+a,bg="white")
        else:
              self.label.configure(text='電宰_貯冰機_R:'+ '　'+a,bg="red")
           
        if  b1 =='True':
              self.label1.configure(text='電宰_貯冰機_S:'+ '　'+b,bg="white")
        else:
              self.label1.configure(text='電宰_貯冰機_S:'+ '　'+b,bg="red")
           
        if  c1 =='True':
              self.label2.configure(text='電宰_貯冰機_T:'+ '　'+c,bg="white")
        else:
              self.label2.configure(text='電宰_貯冰機_T:'+ '　'+c,bg="red")
                      
        if  d1 =='True':
              self.label3.configure(text='2號冷凍機_R:'+ '　'+d,bg="white")
        else:
              self.label3.configure(text='2號冷凍機_R:'+ '　'+d,bg="red")       
                 
        #self.label.configure(text='電宰_貯冰機_R:'+ '　'+a)
        #self.label1.configure(text='電宰_貯冰機_S:'+ '　'+b)
        #self.label2.configure(text='電宰_貯冰機_T:'+ '　'+c)
        #self.label3.configure(text='2號冷凍機_R:'+ '　'+d)
        self.label4.configure(text=now)
      except Exception:
        print('----')
        self.root.after(3000, self.update_clock)
      else:    
        self.root.after(3000, self.update_clock)
app=App()