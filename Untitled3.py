#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Verileri çekmek
fiyatt = []
puann = []
markaa = []
favlarr = []

for i in range(20):
    adres = f"https://www.trendyol.com/elektrikli-ev-aletleri-x-c1104?pi={i}"
    baslik = {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"}
    sayfa = requests.get(adres, headers=baslik)
    soup = BeautifulSoup(sayfa.content, "html.parser")
    
    fiyatlar = soup.find_all('div', {'class': 'prc-box-dscntd'})
    puanlar = soup.find_all('span', {'class': 'rating-score'})
    markalar = soup.find_all('span', {'class': 'prdct-desc-cntnr-ttl'})
    favlar = soup.find_all('div', {'class': 'social-proof-wrapper'})
    
    # Burada, liste uzunluklarını kontrol ediyoruz
    min_len = min(len(fiyatlar), len(puanlar), len(markalar), len(favlar))  # en küçük uzunluğu alıyoruz
    
    for j in range(min_len):  # sadece ortak uzunluk kadar döngüye giriyoruz
        fiyatt.append(fiyatlar[j].text.strip()) 
        puann.append(puanlar[j].text.strip() if len(puanlar) > j else '0')  # Eğer puan yoksa 0 ekliyoruz
        markaa.append(markalar[j].text.strip()) 
        favlarr.append(favlar[j].text.strip())

# Çekilen verilerle ilgili kontrol
print(f"Fiyatlar: {fiyatt[:5]}")
print(f"Puanlar: {puann[:5]}")
print(f"Markalar: {markaa[:5]}")
print(f"Favoriler: {favlarr[:5]}")


# In[3]:


data = pd.DataFrame(list(zip(fiyatt,puann,markaa,favlarr)),columns=["Fiyatlar","Puanlar","Markalar","Favoriler"])


# In[4]:


data


# In[5]:


plt.figure(figsize=(18, 8))  # Grafik boyutunu büyütüyoruz

# Fiyatlar histogramı
plt.subplot(1, 2, 1)
plt.hist(data['Fiyatlar'], bins=30, color='skyblue', edgecolor='black')  # Bin sayısını artırdık
plt.title('Fiyatlar Histogramı', fontsize=16)
plt.xlabel('Fiyatlar (TL)', fontsize=14)
plt.ylabel('Frekans', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Puanlar histogramı
plt.subplot(1, 2, 2)
plt.hist(data['Puanlar'], bins=20, color='lightcoral', edgecolor='black')  # Bin sayısını artırdık
plt.title('Puanlar Histogramı', fontsize=16)
plt.xlabel('Puanlar', fontsize=14)
plt.ylabel('Frekans', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Grafik gösterimi
plt.tight_layout()  # Grafikleri daha düzgün hizalayacak
plt.show()





# In[6]:


data = pd.DataFrame({
    'Fiyatlar': fiyatt,
    'Puanlar': puann,
    'Markalar': markaa,
    'Favoriler': favlarr
})

# Fiyatlar ve Puanlar sütunlarını sayısal formata dönüştürme
# Fiyatlar için '₺' simgesi veya diğer semboller varsa bunları temizleyip sayıya çeviriyoruz
data['Fiyatlar'] = data['Fiyatlar'].replace({r'[^\d.]': ''}, regex=True).astype(float)

# Puanlar için boş veya hatalı değerleri 0 yapıyoruz
data['Puanlar'] = pd.to_numeric(data['Puanlar'], errors='coerce').fillna(0)

# Kutu grafiği için ayarlar
plt.figure(figsize=(12, 6))

# Fiyatlar için kutu grafiği
plt.subplot(1, 2, 1)
plt.boxplot(data['Fiyatlar'], vert=False, patch_artist=True, 
            boxprops=dict(facecolor='skyblue', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
plt.title('Fiyatlar Kutu Grafiği')
plt.xlabel('Fiyatlar (TL)')

# Puanlar için kutu grafiği
plt.subplot(1, 2, 2)
plt.boxplot(data['Puanlar'], vert=False, patch_artist=True, 
            boxprops=dict(facecolor='lightcoral', color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'))
plt.title('Puanlar Kutu Grafiği')
plt.xlabel('Puanlar')

# Grafik düzenini sıkılaştırma ve gösterme
plt.tight_layout()
plt.show()


# In[7]:


# Fiyatlar için çubuk grafiği
plt.figure(figsize=(12, 6))

# Fiyatların histogramını çizmeyi tercih ediyoruz çünkü daha iyi bir dağılım gösterir
plt.subplot(1, 2, 1)
plt.hist(data['Fiyatlar'], bins=20, color='skyblue', edgecolor='black')
plt.title('Fiyatlar Histogramı')
plt.xlabel('Fiyatlar (TL)')
plt.ylabel('Frekans')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Puanlar için çubuk grafiği
plt.subplot(1, 2, 2)
plt.hist(data['Puanlar'], bins=10, color='lightcoral', edgecolor='black')
plt.title('Puanlar Histogramı')
plt.xlabel('Puanlar')
plt.ylabel('Frekans')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafik düzenini sıkılaştırma ve gösterme
plt.tight_layout()
plt.show()



# In[8]:


import matplotlib.pyplot as plt

# Scatter plot oluşturma
plt.figure(figsize=(8, 6))
plt.scatter(data['Fiyatlar'], data['Puanlar'], color='orange', edgecolor='black', alpha=0.6)
plt.title('Fiyatlar vs Puanlar', fontsize=16)
plt.xlabel('Fiyatlar (TL)', fontsize=14)
plt.ylabel('Puanlar', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)

# Grafik gösterimi
plt.tight_layout()
plt.show()


# In[9]:


import matplotlib.pyplot as plt

# Marka ve Ürün sayısını hesaplayalım
marka_sayisi = data['Markalar'].value_counts()

# Bar plot oluşturma
plt.figure(figsize=(12, 6))
marka_sayisi.plot(kind='bar', color='skyblue', edgecolor='black')

# Başlık ve etiketler
plt.title('Marka ve Ürün Sayısına Göre Dağılım', fontsize=16)
plt.xlabel('Markalar', fontsize=14)
plt.ylabel('Ürün Sayısı', fontsize=14)
plt.xticks(rotation=90, ha='center')  # X eksenindeki markaları döndürerek yerleştirme
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafik gösterimi
plt.tight_layout()
plt.show()


# In[10]:


from scipy.stats import ttest_ind

# Fiyatlara göre ürünleri iki gruba ayırma
low_price_group = data[data['Fiyatlar'] <= data['Fiyatlar'].median()]['Puanlar']
high_price_group = data[data['Fiyatlar'] > data['Fiyatlar'].median()]['Puanlar']

# T-testi uygulama
t_stat, p_value = ttest_ind(low_price_group, high_price_group, equal_var=False)

# Sonuçları yazdırma
print("Bağımsız Örneklem T-Testi Sonuçları:")
print(f"T-istatistiği: {t_stat}")
print(f"P-değeri: {p_value}")

# Karar
alpha = 0.05  # %5 anlamlılık seviyesi
if p_value < alpha:
    print("Sonuç: İki grup arasında istatistiksel olarak anlamlı bir fark vardır.")
else:
    print("Sonuç: İki grup arasında istatistiksel olarak anlamlı bir fark yoktur.")



# In[11]:


import pandas as pd
from scipy import stats

# Veri setinizi yükleyin (örneğin, data)
# Örneğin: data = pd.read_csv('veri.csv') veya DataFrame'iniz zaten mevcut olabilir

# Boş değerleri temizleme (özellikle fiyat ve marka sütunlarındaki)
data = data.dropna(subset=['Fiyatlar', 'Markalar'])

# Markalar'a göre fiyatları grupla
markalar_fiyat = [group['Fiyatlar'].values for name, group in data.groupby('Markalar')]

# ANOVA testi uygulama
f_statistic, p_value = stats.f_oneway(*markalar_fiyat)

# Sonuçları yazdırma
print(f"ANOVA testi sonucunda F-istatistiği: {f_statistic}")
print(f"p-değeri: {p_value}")

# p-değeri 0.05'ten küçükse, gruplar arasında anlamlı bir fark vardır.
if p_value < 0.05:
    print("Sonuç: Markalar arasında fiyatlar açısından anlamlı fark bulunmaktadır.")
else:
    print("Sonuç: Markalar arasında fiyatlar açısından anlamlı fark bulunmamaktadır.")


# In[12]:


import pandas as pd
from scipy.stats import chi2_contingency

# Verinizi yükleyin (örneğin data)
# data = pd.read_csv('veri.csv') veya DataFrame'iniz zaten mevcut olabilir

# Boş değerleri temizleme
data = data.dropna(subset=['Markalar', 'Favoriler'])

# Markalar ve Favoriler arasındaki kontenjans tablosunu oluşturma
contingency_table = pd.crosstab(data['Markalar'], data['Favoriler'])

# Ki-Kare Bağımsızlık Testi
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Sonuçları yazdırma
print(f"Ki-Kare İstatistiği: {chi2_stat}")
print(f"p-değeri: {p_value}")
print(f"Serbestlik Derecesi (Degrees of Freedom): {dof}")
print(f"Beklenen Frekanslar: \n{expected}")

# p-değeri 0.05'ten küçükse, iki değişken arasında anlamlı bir ilişki vardır.
if p_value < 0.05:
    print("Sonuç: Markalar ve Favoriler arasında anlamlı bir ilişki vardır.")
else:
    print("Sonuç: Markalar ve Favoriler arasında anlamlı bir ilişki yoktur.")




# In[13]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Veriyi yükleyin veya oluşturun (örneğin DataFrame 'data' adında)
# Örnek veri: data = pd.read_csv("veri.csv") veya mevcut DataFrame'inizi kullanabilirsiniz

# Verinin temizlenmesi (geçersiz değerleri veya NaN değerlerini temizleyin)
data['Fiyatlar'] = pd.to_numeric(data['Fiyatlar'], errors='coerce')  # Fiyatları sayısal hale getirin
data['Puanlar'] = pd.to_numeric(data['Puanlar'], errors='coerce')  # Puanları sayısal hale getirin
data = data.dropna(subset=['Fiyatlar', 'Puanlar'])  # NaN olan satırları temizleyin

# Pearson Korelasyon Katsayısı hesaplama
correlation = data[['Fiyatlar', 'Puanlar']].corr(method='pearson')

# Korelasyon matrisini yazdırma
print("Pearson Korelasyon Katsayısı:")
print(correlation)

# Korelasyon matrisini görselleştirme
plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
plt.title("Fiyatlar ve Puanlar Arasındaki Korelasyon")
plt.show()

# Eğer çok güçlü bir ilişki varsa, aşağıdaki gibi yorum yapabilirsiniz:
if correlation.iloc[0, 1] > 0.7:
    print("Fiyatlar ve Puanlar arasında güçlü pozitif bir ilişki var.")
elif correlation.iloc[0, 1] < -0.7:
    print("Fiyatlar ve Puanlar arasında güçlü negatif bir ilişki var.")
else:
    print("Fiyatlar ve Puanlar arasında zayıf bir ilişki var.")



# In[14]:


import pandas as pd
from scipy.stats import pearsonr

# Veriyi yükleyin veya oluşturun (örneğin DataFrame 'data' adında)
# data = pd.read_csv("veri.csv") veya mevcut DataFrame'inizi kullanabilirsiniz

# Verinin temizlenmesi (geçersiz değerleri veya NaN değerlerini temizleyin)
data['Fiyatlar'] = pd.to_numeric(data['Fiyatlar'], errors='coerce')  # Fiyatları sayısal hale getirin
data['Puanlar'] = pd.to_numeric(data['Puanlar'], errors='coerce')  # Puanları sayısal hale getirin
data = data.dropna(subset=['Fiyatlar', 'Puanlar'])  # NaN olan satırları temizleyin

# Pearson Korelasyon Testi (Fiyatlar ve Puanlar arasındaki ilişkiyi test et)
corr_coefficient, p_value = pearsonr(data['Fiyatlar'], data['Puanlar'])

# Sonuçları yazdır
print(f"Pearson Korelasyon Katsayısı: {corr_coefficient}")
print(f"P-değeri: {p_value}")

# Korelasyon katsayısının yorumu
if p_value < 0.05:
    print("Sonuç: İki değişken arasında istatistiksel olarak anlamlı bir ilişki bulunmaktadır.")
else:
    print("Sonuç: İki değişken arasında istatistiksel olarak anlamlı bir ilişki bulunmamaktadır.")


# In[ ]:





# In[ ]:





# In[ ]:




