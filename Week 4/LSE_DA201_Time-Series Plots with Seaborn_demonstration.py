#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 201: Data Analytics with Python

# ## Time-series plots with Seaborn (Python) (demonstration video)

# Time-series are an excellent example of lineplots assisting us to identify trends. Watch this video where your course convener, Dr Milena Tsvetkova, will illustrate how to create a time-series plot using Seaborn. In this video, you will learn:
# 
# - how to apply time-series in a real-life scenario to identify trends
# - how to create a time-series plot in Seaborn
# - how to understand/read a time-series plot.
# 
# Before you watch the video, prepare your workstation so that you can follow along with the demonstration.

# ## Prepare your workstation

# In[1]:


# import matplotlib, seaborn, and pandas libraries
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import *

# read the CSV file
weather = pd.read_csv("ny_hourly.csv")

# view the DataFrame
print(weather.shape)
print(weather.dtypes)
print(weather.columns)
weather.head()


# In[3]:


# import data again with parse
weather = pd.read_csv("ny_hourly.csv",
                     parse_dates = [["date", "TimeEST"]],
                     usecols = ["date", "TimeEST", "TemperatureF", "Dew PointF", "Humidity"])

weather


# In[4]:


# use describe function
weather.describe()


# In[5]:


# only values bigger than -100
weather = weather[weather["TemperatureF"] > -100]

# sort data
weather = weather.sort_values("date_TimeEST")

# view DataFrame
weather


# In[13]:


# How temperature changes over time
# Seaborn lineplots
sns.lineplot(x = "date_TimeEST", y = "TemperatureF",
            data = weather).set_title("Hourly Temperature (ºF) in New York")


# In[12]:


# dew point
sns.lineplot(x = "date_TimeEST", y = "Dew PointF",
            data = weather).set_title("Hourly Dew Point (ºF) in New York")


# In[14]:


# humidity
sns.lineplot(x = "date_TimeEST", y = "Humidity",
            data = weather).set_title("Hourly Humidity (%) in New York")


# In[11]:


# format dates
fig, ax = plt.subplots()

sns.lineplot(x = "date_TimeEST", y = "TemperatureF",
             data = weather).set_title("Hourly Temperature (ºF) in New York")

x_labels = weather["date_TimeEST"].dt.strftime("%Y-%m-%d")

ax.set_xticklabels(x_labels, rotation = 45)

plt.show()


# In[15]:


# plotting different variables
january_data = weather[weather.date_TimeEST < np.datetime64('2016-01-03')]

fig, temp_ax = plt.subplots()
fig.set_size_inches(14, 8)

humidity_ax = temp_ax.twinx()

# add labels
temp_ax.set_title("Hourly Temperature in NYC")
temp_ax.set_xlabel("Date & Time")
temp_ax.set_ylabel("Temperature (ºF)")

humidity_ax.set_ylabel("Humidity (%)")

# change date and time
major_locator = AutoDateLocator()
formatter = ConciseDateFormatter(major_locator)
humidity_ax.xaxis.set_major_formatter(formatter)
temp_ax.xaxis.set_major_formatter(formatter)

temp_lines = temp_ax.plot(january_data.date_TimeEST, january_data.TemperatureF, 'r')
humidity_lines = humidity_ax.plot(january_data.date_TimeEST, january_data.Humidity, 'c')


# In[19]:


# plot multiple variables with the same x-axis
fig, axes = plt.subplots(nrows = 3)
nyc_fig = fig
fig.set_size_inches(14, 10)

temp_lines = axes[0].plot(weather.date_TimeEST, weather.TemperatureF, "r")
humidity_lines = axes[1].plot(weather.date_TimeEST, weather.Humidity, "y")
dew_point_lines = axes[2].plot(weather.date_TimeEST, weather["Dew PointF"], "g")

axes[0].set_xticklabels([])
axes[1].set_xticklabels([])

major_locator = AutoDateLocator()
formatter = ConciseDateFormatter(major_locator)
axes[2].xaxis.set_major_formatter(formatter)
axes[0].set_ylabel("Temperature (ºF)")
axes[1].set_ylabel("Humidity (%)")
axes[2].set_ylabel("Dew Point (ºF)")
axes[2].set_xlabel("Date")
fig.suptitle("Weather in New York City", fontsize = 16, y = 0.92)
axes[2].legend(temp_lines + humidity_lines + dew_point_lines, 
              ["Temperature", "Humidity", "Dew Point"],
               loc = "lower right", ncol = 3)


# In[22]:


# alternative methods
fig, ax = plt.subplots(3)
fig.set_size_inches(14, 10)

sns.lineplot(x = "date_TimeEST", y = "TemperatureF", ax = ax[0], data = weather)
sns.lineplot(x = "date_TimeEST", y = "Dew PointF", ax = ax[1], data = weather)
sns.lineplot(x = "date_TimeEST", y = "Humidity", ax = ax[2], data = weather)

plt.show()


# In[ ]:




