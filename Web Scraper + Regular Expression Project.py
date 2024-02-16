#!/usr/bin/env python
# coding: utf-8

# ### Web Scraping + Regular Expression + Pandas

# In[6]:


from bs4 import BeautifulSoup
import requests


# In[8]:


url = 'http://www.analytictech.com/mb021/mlk.htm'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[9]:


print(soup)


# In[11]:


mlkj_speech = soup.find_all('p')


# In[13]:


type(mlkj_speech)


# In[14]:


speech_combined = [p.text for p in mlkj_speech]

print(speech_combined)


# In[15]:


type(speech_combined)


# In[35]:


' '.join(speech_combined)


# In[43]:


string_speech = ' '.join(speech_combined)


# In[44]:


string_speech_cleaned = string_speech.replace('\r\n', ' ')


# In[45]:


string_speech_cleaned.replace('\\', '')


# In[49]:


import re


# In[52]:


speech_no_punt = re.sub(r'[^\w\s,]', '', string_speech_cleaned)

print(speech_no_punt)


# In[54]:


speech_lower = speech_no_punt.lower()


# In[56]:


speech_broken_out = re.split(r'\s+',speech_lower)


# In[57]:


speech_broken_out = re.split(r'\s+',speech_lower)


# In[58]:


import pandas as pd


# In[62]:


df = pd.DataFrame(speech_broken_out).value_counts()
df


# In[63]:


df.to_csv(r'C:\Users\antho\OneDrive\Documents\Python Scripts\MLKJ_Speech_Counts.csv', header = ['Counts'],index_label = 'Word')


# In[ ]:




