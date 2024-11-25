#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


for i in range(20):
    adres = f"https://www.trendyol.com/elektrikli-ev-aletleri-x-c1104?pi={i}"
    baslik = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    sayfa = requests.get(adres,headers=baslik)
    soup = BeautifulSoup(sayfa.content,"html.parser")
    markalar = soup.find_all('span',{'class':'prdct-desc-cntnr-ttl'})
    for marka in markalar:
        print(marka.text)


# In[ ]:





# In[ ]:





# In[ ]:




