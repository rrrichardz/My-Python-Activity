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


# ## New activity starts from here (Practical Activity 3.1.10)

# ### Prepare your workstation

# In[1]:


# import pandas
import pandas as pd

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


# In[2]:


# view data frame
mov_ott


# ### 1: The film release date and content rating

# In[3]:


# Determine movies per year and age group
movies.pivot(index = 'Title', columns = 'Age', values = 'Year')


# ### 2: The title of movies, the directors, and genres by content rating

# In[4]:


# Determine movies, directors and genres per age group
movies.pivot(index = 'Title', columns = 'Age', 
             values = ['Directors', 'Genres'])


# ### 3: The title of movies, the released year, and language by content rating

# In[6]:


# Determine movies, year and language per age group
movies.pivot(index = 'Title', columns = 'Age', 
             values = ['Year', 'Language'])


# ### 4: Netflix screened movies based on language, runtime, and country

# In[7]:


# Determine the movies, language, runtime and country screened by Netflix
mov_ott.pivot(index = 'Title', columns = 'Netflix',
             values = ['Runtime', 'Language', 'Country'])


# ### 5: The title of movies, specified language, potential runtime, and genres by content rating

# In[8]:


# Determine the movies, language, runtime, and genres per age group
mov_ott.pivot(index = 'Title', columns = 'Age', 
              values = ['Runtime', 'Language', 'Genres'])


# In[ ]:




