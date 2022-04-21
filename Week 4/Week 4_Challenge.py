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


# ## Week 4 Challenge starts below

# ### Prepare your workstation

# In[2]:


# import libraries
# Prepare your workstation
# import libarary
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import csv files
oil = pd.read_csv('oil_price.csv')
gold = pd.read_csv('gold_stocks_price.csv')

# view the oil DataFrames
print(oil.shape)
print(oil.dtypes)
print(oil.head())
# view the gold DataFrame
print(gold.shape)
print(gold.dtypes)
print(gold.head())


# In[10]:


# subset gold DataFrame
gold_plot = gold[['Date', 'Open', 'High', 'Low']]

# view gold_subset
print(gold_plot.shape)
print(gold_plot.dtypes)
print(gold_plot.head())


# In[11]:


# subset oil DataFrame
oil_plot = oil[["Date", "Open", "High", "Low"]]

# view DataFrames
print(oil_plot.shape)
print(oil_plot.dtypes)
print(oil_plot.head())


# In[12]:


# import the datatime module
import datetime

# Changing the Data column to date type
gold_plot['Date'] = pd.to_datetime(gold_plot['Date'])
oil_plot['Date'] = pd.to_datetime(oil_plot['Date'])

# check data types of two DataFrames
print(gold_plot.dtypes)
print(gold_plot.head())
print(oil_plot.dtypes)
print(oil_plot.head())


# ### Question 1: What is the distribution of the data?

# In[17]:


# plot pairplot for gold subset with KDE
sns.pairplot(gold_plot, diag_kind = 'kde', height = 2)


# In[16]:


# plot pairplot for oil subset with KDE
sns.pairplot(oil_plot, diag_kind = 'kde', height = 2)


# ### Question 2: Which performed the best in December 2015, gold or oil?

# In[22]:


# Filter the two datasets between the specified dates
# and save them as filtered_gold_df and filtered_oil_df
filtered_gold = gold_plot[(gold_plot["Date"] >= "2015-12-01")                           & (gold_plot["Date"] <= "2015-12-31")]
filtered_oil = oil_plot[(oil_plot["Date"] >= "2015-12-01")                        & (oil_plot["Date"] <= "2015-12-31")]

print(filtered_gold.head())
print(filtered_oil.head())


# In[24]:


# create barplot for gold and set plot size
plt.figure(figsize = (20, 6))

sns.barplot(x = 'High', y = 'Date', data = filtered_gold)


# In[25]:


# create barplot for oil and set plot size
plt.figure(figsize = (20, 6))

sns.barplot(x = 'High', y = 'Date', data = filtered_oil)


# ### Question 3: Are there any outliers in the opening value of both gold and oil?

# In[26]:


# create boxplot for gold and set plot size
plt.figure(figsize = (8, 6))
plt.title('Opening Value: Gold')

sns.boxplot(x = gold_plot['Open'])


# In[27]:


# create boxplot for oil and set plot size
plt.figure(figsize = (8, 6))
plt.title('Opening Value: Oil')

sns.boxplot(x = oil_plot['Open'])


# In[29]:


# create histogram for gold and set plot size
plt.figure(figsize = (8, 6))
plt.title('Opening Value: Gold')

sns.histplot(x = gold_plot['Open'], bins = 20)


# In[30]:


# create histogram for oil and set plot size
plt.figure(figsize = (8, 6))
plt.title('Opening Value: Oil')

sns.histplot(x = oil_plot['Open'], bins = 20)


# ### Question 4: What happened to gold and oil on the stock market during June 2016?

# In[32]:


# create lineplot for gold and subset for the month of June 2016 and set plot size
plt.figure(figsize = (12, 6))

filtered_gold = gold_plot[(gold_plot['Date'] >= '2016-06-01')                           & (gold_plot['Date'] <= '2016-06-30')]

sns.lineplot(data = filtered_gold, x = 'High', y = 'Date')


# In[33]:


# create lineplot for oil and subset for the month of June 2016 and set plot size
plt.figure(figsize = (12, 6))

filtered_oil = oil_plot[(oil_plot['Date'] >= '2016-06-01')                           & (oil_plot['Date'] <= '2016-06-30')]

sns.lineplot(data = filtered_oil, x = 'High', y = 'Date')


# In[38]:


# create scatterplots for both gold and oil and customise plots
g = sns.scatterplot(x = 'High', y = 'Date', data = filtered_gold)

g.set_xlabel('High')
g.set_ylabel('Date')
g.set_title('High Value: Gold (June 2016)', y = 1.02, fontsize = 16)


# In[39]:


o = sns.scatterplot(x = 'High', y = 'Date', data = filtered_oil)

o.set_xlabel('High')
o.set_ylabel('Date')
o.set_title('High Value: Oil (June 2016)', y = 1.02, fontsize = 16)


# In[ ]:




