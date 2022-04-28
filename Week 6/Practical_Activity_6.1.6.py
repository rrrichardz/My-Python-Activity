#!/usr/bin/env python
# coding: utf-8

# ## Practical Activity 6.1.6

# ### Prepare workstation

# In[1]:


# Import libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')

# Get multiple outputs in the same cell.
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Read the data file.
data = pd.read_csv("raw_sales.csv", index_col = ['datesold'], parse_dates = ['datesold'])

# View the DataFrame.
print(data.shape)
data.head()


# In[2]:


# Simple hacks to make plots look better: 

# # Colour pallete to make charts look better
blue, = sns.color_palette("muted", 1) 

# darkgrid, white grid, dark, white and ticks
sns.set_style('whitegrid') 

# fontsize of the axes title
plt.rc('axes', titlesize=18) 

# fontsize of the x and y labels
plt.rc('axes', labelsize=14)    

# fontsize of the tick labels
plt.rc('xtick', labelsize=13,color='#4f4e4e') 

# fontsize of the tick labels
plt.rc('ytick', labelsize=13,color='#4f4e4e')  

# legend fontsize
plt.rc('legend', fontsize=13)

# controls default text sizes
plt.rc('font', size=13)       


# ### Get to know the data

# In[3]:


# Plot the house prices as a time series.
# Plot the size.
data.plot(figsize = (12, 4))

# Specify the legend and title of the plot.
plt.legend(loc = 'best')
plt.title('House Prices')
plt.show(block = False)

# Check for missing values.
data.isnull().sum()


# ### Checking the dataset for the count of houses based on their bedrooms

# In[4]:


# Count the number of values in a specified column in the DataFrame.
print(data['bedrooms'].value_counts())

# Create a plot.
plt.title('Count the number of bedrooms')

sns.despine(left = True)
sns.countplot(x = 'bedrooms', data = data)


# ### Define sub-data sets

# In[5]:


# Create a copy of the original data for convinience.
data_sub = data.copy()


# Data set cosnsisting of houses with 1 bedroom: 
df_1 = data_sub[data_sub['bedrooms'] == 1]
print(df_1.shape)


# Data set cosnsisting of houses with 2 bedrooms: 
df_2 = data_sub[data_sub['bedrooms'] == 2]
print(df_2.shape)


# Data set cosnsisting of houses with 3 bedrooms: 
df_3 = data_sub[data_sub['bedrooms'] == 3]
print(df_3.shape)


# Data set cosnsisting of houses with 4 bedrooms: 
df_4 = data_sub[data_sub['bedrooms'] == 4]
print(df_4.shape)


# Data set cosnsisting of houses with 5 bedrooms: 
df_5 = data_sub[data_sub['bedrooms'] == 5]
print(df_5.shape)


# ### Detect outliers

# In[6]:


# Set the plot size.
fig, axes = plt.subplots(nrows = 3, ncols = 2, figsize = (20, 20))

# 1 bedroom:
axes[0][0].hist(df_1['price'])
axes[0][0].title.set_text('1 bedroom price histogram')

# 2 bedrooms:
axes[0][1].hist(df_2['price'])
axes[0][1].title.set_text('2 bedrooms price histogram')

# 3 bedrooms:
axes[1][0].hist(df_3['price'])
axes[1][0].title.set_text('3 bedrooms price histogram')

# 4 bedrooms:
axes[1][1].hist(df_4['price'])
axes[1][1].title.set_text('4 bedrooms price histogram')

# 5 bedrooms:
axes[2][0].hist(df_5['price'])
axes[2][0].title.set_text('5 bedrooms price histogram')

fig.delaxes(axes[2][1])

plt.show()


# In[7]:


# Create a boxplot for 1 bedroom.
# Set figure size.
fig = plt.figure(figsize = (18, 4))

# Create a boxplot.
ax = sns.boxplot(x = df_1['price'], whis = 1.5)


# ### Remove outliers

# In[8]:


# Remove outliers for houses with 1 bedroom.
# The columns you want to search for outiers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0, 1) and not (0, 100)
Q1 = df_1[cols].quantile(0.25)
Q3 = df_1[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_1[cols] < (Q1 - 1.5 * IQR)) | (df_1[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our DataFrame based on condition.
df_1_non_outlier = df_1[condition]
df_1_non_outlier.shape


# In[9]:


# Plot to see if outliers have been removed:
# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_1_non_outlier['price'], whis = 1.5)


# ### Dataset with 2 bedroom (df_2)

# In[10]:


# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_2['price'], whis = 1.5)


# In[12]:


# Histogram plot
fig = df_2.price.hist(figsize = (12,4))


# In[13]:


# Remove outliers for houses with 2 bedrooms.
# The columns you want to search for outiers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0, 1) and not (0, 100)
Q1 = df_2[cols].quantile(0.25)
Q3 = df_2[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_2[cols] < (Q1 - 1.5 * IQR)) | (df_2[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our DataFrame based on condition.
df_2_non_outlier = df_2[condition]
df_2_non_outlier.shape


# In[14]:


# Plot to see if outliers have been removed:
# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_2_non_outlier['price'], whis = 1.5)


# ### Dataset with 3 bedroom (df_3)

# In[15]:


# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_3['price'], whis = 1.5)


# In[16]:


# Histogram plot
fig = df_3.price.hist(figsize = (12,4))


# In[17]:


# Remove outliers for houses with 3 bedrooms.
# The columns you want to search for outiers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0, 1) and not (0, 100)
Q1 = df_3[cols].quantile(0.25)
Q3 = df_3[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_3[cols] < (Q1 - 1.5 * IQR)) | (df_3[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our DataFrame based on condition.
df_3_non_outlier = df_3[condition]
df_3_non_outlier.shape


# In[18]:


# Plot to see if outliers have been removed:
# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_3_non_outlier['price'], whis = 1.5)


# ### Dataset with 4 bedroom (df_4)

# In[19]:


# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_4['price'], whis = 1.5)


# In[20]:


# Histogram plot
fig = df_4.price.hist(figsize = (12,4))


# In[21]:


# Remove outliers for houses with 4 bedrooms.
# The columns you want to search for outiers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0, 1) and not (0, 100)
Q1 = df_4[cols].quantile(0.25)
Q3 = df_4[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_4[cols] < (Q1 - 1.5 * IQR)) | (df_4[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our DataFrame based on condition.
df_4_non_outlier = df_4[condition]
df_4_non_outlier.shape


# In[22]:


# Plot to see if outliers have been removed:
# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_4_non_outlier['price'], whis = 1.5)


# ### Dataset with 5 bedroom (df_5)

# In[23]:


# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_5['price'], whis = 1.5)


# In[24]:


# Histogram plot
fig = df_5.price.hist(figsize = (12,4))


# In[25]:


# Remove outliers for houses with 5 bedrooms.
# The columns you want to search for outiers in.
cols = ['price']

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0, 1) and not (0, 100)
Q1 = df_5[cols].quantile(0.25)
Q3 = df_5[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_5[cols] < (Q1 - 1.5 * IQR)) | (df_5[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our DataFrame based on condition.
df_5_non_outlier = df_5[condition]
df_5_non_outlier.shape


# In[26]:


# Plot to see if outliers have been removed:
# whis = multiplicative factor.
fig = plt.subplots(figsize = (12, 2))

ax = sns.boxplot(x = df_5_non_outlier['price'], whis = 1.5)


# In[ ]:




