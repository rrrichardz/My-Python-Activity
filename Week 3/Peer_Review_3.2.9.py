#!/usr/bin/env python
# coding: utf-8

# ### Peer Review Activity 3.2.9

# ### Below are my codes with insturctions before each code

# In[3]:


# make sure the data file is uploaded properly
# import pandas
import pandas as pd

# read CSV file from the current working directory
products = pd.read_csv('products.csv')

products.shape


# In[4]:


# create a user-defined function to view products contain the word 'fire'
def contains_fire(x):
    """Does the product contain the word 'fire'?"""
    y = x.lower()
    return 'fire' in y

# now apply the function created with the apply() function to answer the question
cf = products['Description'].apply(contains_fire)

# view and filter
print(cf)
products[cf]


# #### by counting above, the answer for the questions is 9 products contain the word fire

# In[6]:


# repeat the same process with creating a user-defined function to view products contain the word 'candle'
def contains_candle(x):
    """Does the product contain the word 'candle'?"""
    y = x.lower()
    return 'candle' in y

# now apply the function created with the apply() function to answer the question
cc = products['Description'].apply(contains_candle)

# view and filter
print(cc)
products[cc]


# ####  By checking the total rows above, the answer for the questions is 178 products contain the word candle

# In[7]:


# repeat the same process with creating a user-defined function to view products contain the word 'matches'
def contains_matches(x):
    """Does the product contain the word 'matches'?"""
    y = x.lower()
    return 'matches' in y

# now apply the function created with the apply() function to answer the question
cm = products['Description'].apply(contains_matches)

# view and filter
print(cm)
products[cm]


# #### by counting above, the answer for the questions is 6 products contain the word matches

# In[ ]:




