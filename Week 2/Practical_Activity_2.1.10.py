#!/usr/bin/env python
# coding: utf-8

# ### movies.xlsx

# In[8]:


import pandas as pd

movies = pd.read_excel("movies.xlsx")

movies


# In[11]:


print(movies.shape)
print(movies.head())
print(movies.tail())


# In[10]:


print(movies.dtypes)


# ### ott.csv

# In[5]:


ott = pd.read_csv("ott.csv")

ott


# In[12]:


print(ott.shape)
print(ott.head())
print(ott.tail())


# In[13]:


print(ott.dtypes)


# In[ ]:




