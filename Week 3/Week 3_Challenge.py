#!/usr/bin/env python
# coding: utf-8

# ## Week 2 Challenge starts below

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


# ## Week 3 Challenge starts below

# ### 1.0 Prepare your workstation

# In[2]:


# import libarary
import pandas as pd

# import csv files
oil = pd.read_csv('oil_price.csv')
gold = pd.read_csv('gold_stocks_price.csv')

# view the DataFrames
print(oil.shape)
print(oil.dtypes)
# view the gold data frame
print(gold.shape)
print(gold.dtypes)


# ### 2.1 Create a subset DataFrame based on gold_stocks_price.csv

# In[4]:


# subset gold dataframe
gold_subset = gold[['Date', 'Open', 'High', 'Low']]

# slice gold_subset to 500 rows
gold_subset = gold_subset.iloc[:500]

# view gold_subset
print(gold_subset.shape)
print(gold.dtypes)


# In[5]:


# determine missing values
gold_subset.isna().sum()


# In[6]:


# Min and max value for column\ for subsetted gold dataframe:
print(gold_subset['Open'].max())
print(gold_subset['Open'].min())


# In[7]:


print(gold_subset['High'].min())
print(gold_subset['High'].max())


# In[8]:


print(gold_subset['Low'].min())
print(gold_subset['Low'].max())


# ### 2.2 Create a subset DataFrame based on oil_price.csv

# In[10]:


# subset oil dataframe
oil_subset = oil[['Date', 'Open', 'High', 'Low']]

# slice oil subset to 500 rows
oil_subset = oil_subset.iloc[:500]

# view oil subset
print(oil_subset.shape)
print(oil.dtypes)


# In[11]:


# determine missing values
oil_subset.isna().sum()


# In[12]:


# Min and max value for column\ for subsetted gold dataframe: 
print(oil_subset['Open'].min())
print(oil_subset['Open'].max())


# In[13]:


print(oil_subset['High'].min())
print(oil_subset['High'].max())


# In[14]:


print(oil_subset['Low'].min())
print(oil_subset['Low'].max())


# ### 2.3 Statistical analysis

# In[16]:


# use the describe() function
print(gold_subset.describe())
print(oil_subset.describe())


# ### 3.1 Determine the daily average price of gold and oil.

# In[17]:


# determine the average gold per day (user-defined function)
def avg_gpd(x, y, z):
    a = (x + y + z) / 3
    return a

# insert avg into new column
gold_subset['average_gold'] = avg_gpd(gold_subset['Open'], 
                                      gold_subset['High'], 
                                      gold_subset['Low'])

# view DataFrame
gold_subset


# In[18]:


# determine the average oil per day (user-defined function)
def avg_opd(x, y, z):
    a = (x + y + z) / 3
    return a

# insert avg into new column
oil_subset['average_oil'] = avg_opd(oil_subset['Open'], 
                                      oil_subset['High'], 
                                      oil_subset['Low'])

# view DataFrame
oil_subset


# ### 3.2 Convert the daily average price of gold and oil from US dollars to British Pound

# In[19]:


# employ lambda function to convert US dollars to British Pound
# where 1 US$ = 0.8 GBP
gold_subset['avg_gold_GBP'] = gold_subset['average_gold'].apply(lambda x: x * 0.8)

# view DataFrame
gold_subset


# In[21]:


# employ lambda function to convert US dollars to British Pound
# where 1 US$ = 0.8 GBP
oil_subset['avg_oil_GBP'] = oil_subset['average_oil'].apply(lambda x: x * 0.8)

# view DataFrame
oil_subset


# ### 3.3 Compare the average gold and oil price in GBP

# In[22]:


# subset the DataFrame to use the merge function and Date as ID
gold = gold_subset[['Date', 'avg_gold_GBP']]

gold


# In[23]:


# subset the DataFrame to use the merge function and Date as ID
oil = oil_subset[['Date', 'avg_oil_GBP']]

oil


# In[24]:


# merge
gold_oil = pd.merge(gold, oil, on = 'Date', how = 'left')

gold_oil


# In[ ]:




