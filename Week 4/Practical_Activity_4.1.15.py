#!/usr/bin/env python
# coding: utf-8

# ## Previous Activity

# ## Practical Activity 4.1.9

# ### 1. Import the libraries

# In[1]:


#import necessary packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# ### 2. Import Excel file

# In[2]:


# import the excel file using pd.read_excel
ott = pd.read_excel("ott.xlsx")

print(ott.columns)


# ### 3. Import CSV file

# In[4]:


# import the CSV file using pd.read_csv
movies = pd.read_csv("movies.csv")

print(movies.columns)


# ### 4. Validate the DataFrames

# In[5]:


# data imported correctly?
print(movies.shape)
print(movies.dtypes)
print(movies.head())


# In[6]:


# data imported correctly?
print(ott.shape)
print(ott.dtypes)
print(ott.head())


# ### 5. Combine the two DataFrames

# In[7]:


# merge the two DataFrames
mov_ott = pd.merge(movies, ott, how = 'left', on = 'ID')

# view the DataFrame
print(mov_ott.shape)
mov_ott.head()


# ### 6. Create a countplot

# In[9]:


# create a countplot based on number of movies streamed by Netflix per age group
sns.countplot(x = 'Age', hue = 'Netflix', data = mov_ott)


# In[10]:


# the 18+ age group has the most-streamed movies
# even though the 18+ group has the most-streamed movies on Netflix
# they still need to add more movies under this age group has most
# of the movies overall


# ### 7. Create a histogram

# In[11]:


# create a histogram based IMDb
sns.histplot(data = mov_ott, x = 'IMDb', binwidth = 1)


# In[12]:


# most of the movies are between 6 and 7 in rating on IMDb
# the outliers are movies with rating between 1 and 2,
# and with rating between 9 and 10


# ### 8. Create a scatterplot

# In[13]:


# create scatterplot with two variables (IMDb and Rotten Tomatoes)
sns.scatterplot(x = 'IMDb', y = 'Rotten Tomatoes', data = mov_ott)


# In[14]:


# both websites have fairly similar rating for the same movie
# the correlation is a strong and positive linear relationship with a few outliers


# 

# ## Previous Activity (Practical Activity 4.1.12)

# ### 1. Import the libraries

# In[15]:


# import necessary packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ### 2. Import Excel file

# In[16]:


# import the excel file using pd.read_excel
ott = pd.read_excel("ott.xlsx")

print(ott.columns)


# ### 3. Import CSV file

# In[17]:


# import the csv file using pd.read_csv
movies = pd.read_csv("movies.csv")

print(movies.columns)


# ### 4. Validate the DataFrames

# In[18]:


# data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)


# In[19]:


# data imported correctly?
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# ### 5. Combine the two DataFrames

# In[20]:


# merge the two DataFrames
mov_ott = pd.merge(movies, ott, how='left', on = "ID")

# view the DataFrame
print(mov_ott.shape)
mov_ott.head()


# ### 6. Create a boxplot

# In[21]:


# create boxplot with two variables (Age and IMDb)
sns.boxplot(x = 'Age', y = 'IMDb', data = mov_ott)


# In[ ]:


# the outliers generally throughout all age groups are in lower ratings
# increase the height of the boxplot can maybe improve the quality of
# the figure, so the bottom of each plot does not cramped up


# ## New Activity Starts Here

# ## Practical Activity 4.1.15

# ### Create a lineplot

# In[23]:


# create a simple lineplot
sns.lineplot(x = 'Year', y = 'IMDb', data = mov_ott)


# In[24]:


# create a simple lineplot
sns.lineplot(x = 'Year', y = 'IMDb', data = mov_ott, ci = None)


# In[ ]:


# users' ratings for movies released between 1920 and 1920 has the highest
# group among all ratings on IMDb (apart from 1900 to 1910 group which started
# high and saw a dramatic drop and then significant increase and drop again)
# 1920 and 1940 overall has the highest ratings by average but ratings dropped
# significantly around 1930 from 1920 (which has the higher ratings in the group)

# the ratings show a strong positive linear growth from 1960 to 1980.


# In[26]:


# create an enhanced lineplot
sns.lineplot(x = 'Year', y = 'IMDb', hue = 'Age', 
             data = mov_ott[mov_ott['Age'].isin(['16+', '18+'])])


# In[27]:


# create an enhanced lineplot
sns.lineplot(x = 'Year', y = 'IMDb', hue = 'Age', 
             data = mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
            ci = None)


# In[ ]:


# I will look at adding genres and producing country in the lineplot

# movies with 18+ age limit has a strong negative linear drop
# movies with 16+ age limit has a mederate negative linear drop with a big
# bounce (dramatic drop and increase) around late 1990s to early 2000s

# film industry started making suitable movies for 16+ age group around 1970

