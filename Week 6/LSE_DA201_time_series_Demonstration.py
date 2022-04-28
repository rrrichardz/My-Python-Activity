#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 201: Data Analytics with Python

# # Time-series forecasting (tutorial video)

# This Jupyter Notebook is based on the time-series forecasting with Python tutorial video. Watch the video to explore time series forecasting with the simple moving average method in Python. In the video, you will explore:
# 
# - What is a simple moving average.
# - How to calculate a simple moving average.
# - How to identify moving average data set.

# # 

# ## Prepare your workstation

# In[1]:


# import libraries
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

# get multiple outputs in the same cell
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


# Simple hacks to make plots look better: 

# Colour pallete to make charts look better
blue, = sns.color_palette("muted", 1) 

# darkgrid, white grid, dark, white and ticks
sns.set_style('whitegrid') 

# fontsize of the axes title
plt.rc('axes', titlesize = 18) 

# fontsize of the x and y labels
plt.rc('axes', labelsize = 14)    

# fontsize of the tick labels
plt.rc('xtick', labelsize = 13, color = '#4f4e4e') 

# fontsize of the tick labels
plt.rc('ytick', labelsize = 13, color = '#4f4e4e')  

# legend fontsize
plt.rc('legend', fontsize = 13)

# controls default text sizes
plt.rc('font', size = 13)          


# In[3]:


# import csv file with pandas
data = pd.read_csv("raw_sales.csv", index_col = ['datesold'], parse_dates = ['datesold'])

# view DataFrame
print(data.shape)
data.head()


# In[4]:


# Creating a copy of the original data for convinience : 
data_sub = data.copy()

# Data set cosnsisting of houses with 5 bedroom : 
df_5 = data_sub[data_sub['bedrooms'] == 5]

df_5.head


# In[5]:


# determine outliers for 5 bedrooms
#whis=multiplicative factor
import seaborn as sns
fig = plt.subplots(figsize = (12, 2))
ax = sns.boxplot(x = df_5['price'], whis = 1.5);


# In[7]:


# histogram of data set (5 bedrooms only)
fig = df_5.price.hist(figsize = (12,4))


# In[6]:


# outlier removal
# Removing outlier from dataset with 2 bedrooms : 
cols = ['price'] # The columns you want to search for outliers in

# Calculate quantiles and IQR
Q1 = df_5[cols].quantile(0.25) # Same as np.percentile but maps (0,1) and not (0,100)
Q3 = df_5[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# # Return a boolean array of the rows with (any) non-outlier column values
condition = ~((df_5[cols] < (Q1 - 1.5 * IQR)) | (df_5[cols] > (Q3 + 1.5 * IQR))).any(axis = 1)

# Filter our dataframe based on condition
df_5_non_outlier = df_5[condition]
df_5_non_outlier.shape


# In[7]:


# Plot to see if outliers have been removed : 

#whis=multiplicative factor
import seaborn as sns
fig = plt.subplots(figsize = (12, 2))
ax = sns.boxplot(x = df_5_non_outlier['price'], whis = 1.5);


# In[8]:


# Plotting the time series data
df_5_non_outlier.plot(figsize = (12, 4))
plt.legend(loc = 'best')
plt.title('Time-series plot for house with 5 bedrooms')
plt.show(block = False);


# In[9]:


# Resampling dataset with 5 bedroom : 
df_5_res = df_5_non_outlier.resample('M').mean()

# view DataFrame
df_5_res.head()


# In[11]:


# Dropping the missing values : 
df_5_res.dropna(inplace = True)
df_5_res.isna().sum()


# In[12]:


# Plotting the time series data
df_5_res.plot(figsize = (12, 4))
plt.legend(loc = 'best')
plt.title('Time-series plot after resampling')
plt.show(block = False);


# # 

# ## Calculate the Simple Moving Average (SMA) for houses with 5 bedrooms

# In[16]:


# This is a function to calculate and plot the simple moving average : 
def plot_moving_average(series, window, plot_intervals = False, scale = 1.96):

    rolling_mean = series.rolling(window = window).mean()
    
    plt.figure(figsize = (12,4))
    plt.title('Moving Average\n Window Size = {}'.format(window))
    plt.plot(rolling_mean, 'g', label = 'Simple Moving Average (SMA) Trend')
    
    #Plot confidence intervals for smoothed values
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bound, 'r--', label = 'Upper Bound / Lower Bound')
        plt.plot(lower_bound, 'r--')
            
    plt.plot(series[window:], label = 'Actual Values')
    plt.legend(loc = 'best')
    plt.grid(True)


# In[14]:


# calculate SMA for a window size of 5
df_5_res['SMA_5'] = df_5_res.iloc[:,1].rolling(window = 5).mean()

# print the first 15 rows of data
print(df_5_res.head(15))


# In[32]:


# smooth by the previous 5 days
plot_moving_average(df_5_res.price, 5, plot_intervals = True)

plt.rc('legend', fontsize = 10)


# In[33]:


# calculate SMA for a window size of 5
df_5_res['SMA_30'] = df_5_res.iloc[:,1].rolling(window = 30).mean()

# calculate SMA for a window size of 5
df_5_res['SMA_90'] = df_5_res.iloc[:,1].rolling(window = 90).mean()


# print the first 100 rows of data
print(df_5_res.head(100))


# In[34]:


# smooth by the previous month (30 days)
plot_moving_average(df_5_res.price, 30, plot_intervals = True)


# In[35]:


# smooth by the previous quarter (90 days)
plot_moving_average(df_5_res.price, 90, plot_intervals = True)


# In[ ]:




