#!/usr/bin/env python
# coding: utf-8

# In[4]:

                                                  #PUAN ÇEKME
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


for i in range(20):
    adres = f"https://www.trendyol.com/elektrikli-ev-aletleri-x-c1104?pi={i}"
    baslik = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    sayfa = requests.get(adres,headers=baslik)
    soup = BeautifulSoup(sayfa.content,"html.parser")
    puanlar = soup.find_all('span',{'class':'rating-score'})
    for puan in puanlar:
        print(puan.text)


# In[ ]:





# In[ ]:




