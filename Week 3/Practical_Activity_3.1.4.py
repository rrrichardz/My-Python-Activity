#!/usr/bin/env python
# coding: utf-8

# ### 1. Import Pandas

# In[1]:


#import necessary packages
import pandas as pd


# ### 2. Import Excel and CSV file

# In[19]:


#Load the excel data using pd.read_excel
movies_merge = pd.read_excel("movies_merge.xlsx")

ott_merge = pd.read_csv("ott_merge.csv")

print(movies_merge.columns)

print(ott_merge.columns)


# ### 3. Validate the DataFrames

# In[8]:


# data imported correctly?
print(movies_merge.shape)

movies_merge.head()


# In[9]:


# data imported correctly?
print(ott_merge.shape)

ott_merge.head()


# ### 4. Describe the data types

# In[21]:


# data types
print(movies_merge.dtypes)

print(ott_merge.dtypes)


# ### 5. Combine the two DataFrames
# #### a) merge()

# In[22]:


# merge the data
movies_ott_merge = pd.merge(movies_merge, ott_merge, how = 'left', on = 'ID')

print(movies_ott.shape)

movies_ott.head()


# #### b) concat()

# In[17]:


# concat data frames
movies_ott_concat = pd.concat([movies_merge, ott_merge], axis = 0)

print(movies_ott_concat.shape)

movies_ott_concat.head()


# #### c) append()

# In[18]:


# append data frames
movies_ott_append = movies_merge.append(ott_merge)

print(movies_ott_append.shape)

movies_ott_append.head()


# In[ ]:




