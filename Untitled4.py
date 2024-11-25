#!/usr/bin/env python
# coding: utf-8

# In[12]:


import requests
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[11]:


for i in range(20):
    adres = f"https://www.trendyol.com/elektrikli-ev-aletleri-x-c1104?pi={i}"
    baslik = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    sayfa = requests.get(adres, headers=baslik)
    soup = BeautifulSoup(sayfa.content, "html.parser")
    
    favlar = soup.find_all('div', {'class': 'social-proof-wrapper'})
    for fav in favlar:
        # Favori sayısını çekmek için regex kullan
        fav_text = fav.text
        fav_count = re.findall(r'[\d\.]+', fav_text)  # Sayıları al
        if fav_count:
            fav_count = fav_count[0]  # İlk bulduğumuz sayıyı al (favori sayısı)
            print(f"Favori Sayısı: {fav_count}")


# In[ ]:





# In[ ]:




