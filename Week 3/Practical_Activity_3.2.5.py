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


# ## New activity starts from here (Practical Activity 3.2.5)

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

#merge the data
mov_ott = pd.merge(movies, ott, how='left', on = "ID")

# DataFrames merged correctly?
print(mov_ott.columns)
print(mov_ott.shape)


# ### Question 1: What is the average rating per movie?

# In[2]:


# view IMDb and Rotten Tomatoes columns
mov_ott_ratings = mov_ott[['ID', 'IMDb', 'Rotten Tomatoes']]

mov_ott_ratings


# In[3]:


# replace missing values with 0
mov_ott_ratings_final = mov_ott_ratings.fillna(0)

mov_ott_ratings_final


# In[4]:


# add new column to DataFrame indicating average rating
# average rating is (IMDb / 10 + Rotten Tomatoes) / 2
# write user defined function
def avg_col2(df1, df2):
    df = (df1 / 10 + df2) / 2
    return df

mov_ott_ratings_final['Ratings'] = avg_col2(mov_ott_ratings_final['IMDb'],
                                           mov_ott_ratings_final['Rotten Tomatoes'])
                                            
mov_ott_ratings_final


# ### Question 2: How many movies were released per content rating (age)?

# In[7]:


# categorical count 
def cat_cnt(df1):
    print(df1.value_counts())
    
# number of movies released per 'Age'
df = mov_ott['Age'].astype('category')

cat_cnt(df)


# ### Question 3: How many movies were released per year?

# In[8]:


# categorical count
def cat_cnt(df1):
    print(df1.value_counts())
    
# number of movies released per 'Year'
df = mov_ott['Year'].astype('category')

cat_cnt(df)


# In[ ]:




