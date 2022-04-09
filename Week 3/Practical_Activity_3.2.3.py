#!/usr/bin/env python
# coding: utf-8

# ## Previous Activity

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


# ## New activity starts from here (Practical Activity 3.2.3)

# ### Prepare your workstation

# In[1]:


# import pandas
import pandas as pd
import numpy as np

# load the excel data using pd.read_excel
movies = pd.read_excel("movies_merge.xlsx")

# load the csv data using pd.read_csv
ott = pd.read_csv("ott_merge.csv")

# data imported correctly?
print(movies.columns)
print(movies.shape)
print(ott.columns)
print(ott.shape)

# merge the data
mov_ott = pd.merge(movies, ott, how = 'left', on = 'ID')

# DataFrames merged correctly?
print(mov_ott.columns)
print(mov_ott.shape)


# ### Question 1: What is the effect of adding 60 seconds (1 minute) to each movie?

# In[2]:


# determine the runtime of each movie
mov_ott_runtime = mov_ott[['ID', 'Runtime', 'Genres']]

mov_ott_runtime


# In[3]:


# add 60 seconds or 1 minute to runtime
mov_ott_runtime['Runtime'].add(1)


# ### Question 2: Which movies are documentaries?

# In[4]:


#create a new column with doc
mov_ott_runtime['Gen_doc'] = np.where(mov_ott_runtime['Genres'] .str.contains('Documentary'), 'Documentary', 'Not Documentary')

mov_ott_runtime


# In[5]:


# apply len (determine length of string)
mov_ott_runtime.Gen_doc.apply(len)


# ### Challenge

# In[6]:


# subtract 6 seconds / 0.01 mins from runtime
mov_ott_runtime[['ID', 'Runtime']]


# In[7]:


# subtract 6 seconds / 0.01 mins from runtime
mov_ott_runtime['Runtime'].subtract(0.01)


# ### Try these lambda functions

# In[11]:


# add 60 seconds or one minute with lambda function
mov_ott['Runtime'] = mov_ott['Runtime'].apply(lambda x: x + 1)

mov_ott['Runtime']


# In[12]:


# subtract 0.01 from runtime with lamda function
mov_ott['Runtime'] = mov_ott_runtime['Runtime'].apply(lambda x: x - 0.01)

mov_ott['Runtime']


# In[ ]:




