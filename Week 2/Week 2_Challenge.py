#!/usr/bin/env python
# coding: utf-8

# ### 1. Prepare your workstation

# In[3]:


# import libarary
import pandas as pd

# import csv files
oil = pd.read_csv("oil_price.csv")

gold = pd.read_csv("gold_stocks_price.csv")

# view the oil data frame
print(oil.shape)
print(oil.dtypes)
print(oil.head())
print(oil.tail())


# In[4]:


# view the gold data frame
print(gold.shape)
print(gold.dtypes)
print(gold.head())
print(gold.tail())


# ### 2. Create a subset DataFrame based on `gold_stocks_price.csv`

# In[7]:


# subset gold dataframe
gold_subset = gold[['Date', 'Open', 'High', 'Low']]

# slice gold_subset to 500 rows
gold_subset = gold_subset.iloc[:500]

# view gold_subset
print(gold_subset.shape)
print(gold_subset.dtypes)


# In[8]:


# determine missing values
gold_subset.isna().sum()


# In[13]:


# Min and max value for column\ for subsetted gold dataframe:
print(gold_subset['Open'].min())
print(gold_subset['Open'].max())


# In[11]:


# Min and max value for column\ for subsetted gold dataframe:
print(gold_subset['High'].min())
print(gold_subset['High'].max())


# In[12]:


# Min and max value for column\ for subsetted gold dataframe:
print(gold_subset['Low'].min())
print(gold_subset['Low'].max())


# ### Alternate way using print statement: 

# In[14]:


print(f"The maximum value for open is the subsetted gold dataframe is {gold_subset['Open'].max()}")
print(f"The minimum value for open is the subsetted gold dataframe is {gold_subset['Open'].min()}")

print(f"The maximum value for high is the subsetted gold dataframe is {gold_subset['High'].max()}")
print(f"The minimum value for high is the subsetted gold dataframe is {gold_subset['High'].min()}")

print(f"The maximum value for low is the subsetted gold dataframe is {gold_subset['Low'].max()}")
print(f"The minimum value for low is the subsetted gold dataframe is {gold_subset['Low'].min()}")


# ### 3. Create a subset DataFrame based on `oil_price.csv`

# In[15]:


# subset oil dataframe
oil_subset = oil[['Date', 'Open', 'High', 'Low']]

# slice oil_subset to 500 rows
oil_subset = oil_subset.iloc[:500]

# view oil_subset
print(oil_subset.shape)
print(oil_subset.dtypes)


# In[16]:


# determine missing values
oil_subset.isna().sum()


# In[17]:


# Min and max value for column\ for subsetted oil dataframe:
print(oil_subset['Open'].min())
print(oil_subset['Open'].max())


# In[18]:


# Min and max value for column\ for subsetted oil dataframe:
print(oil_subset['High'].min())
print(oil_subset['High'].max())


# In[19]:


# Min and max value for column\ for subsetted oil dataframe:
print(oil_subset['Low'].min())
print(oil_subset['Low'].max())


# ### Alternate way using print statement: 

# In[20]:


print(f"The maximum value for open is the subsetted oil dataframe is {oil_subset['Open'].max()}")
print(f"The minimum value for open is the subsetted oil dataframe is {oil_subset['Open'].min()}")

print(f"The maximum value for high is the subsetted oil dataframe is {oil_subset['High'].max()}")
print(f"The minimum value for high is the subsetted oil dataframe is {oil_subset['High'].min()}")

print(f"The maximum value for low is the subsetted oil dataframe is {oil_subset['Low'].max()}")
print(f"The minimum value for low is the subsetted oil dataframe is {oil_subset['Low'].min()}")


# ### 4. Statistical analysis

# In[21]:


# use the describe() function
print(gold_subset.describe())
print(oil_subset.describe())


# In[ ]:




