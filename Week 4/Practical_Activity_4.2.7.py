#!/usr/bin/env python
# coding: utf-8

# ## Practical Activity 4.2.7

# ### 1. Import the libraries

# In[35]:


# import necessary packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# ### 2. Import file

# In[37]:


# import the CSV and Excel file
ott = pd.read_excel("ott.xlsx")
movies = pd.read_csv("movies.csv")

print(ott.columns)
print(movies.columns)


# ### 3. Validate the DataFrames

# In[38]:


# data imported correctly?
print(movies.head())
print(movies.shape)
print(movies.dtypes)
print(ott.head())
print(ott.dtypes)
print(ott.shape)


# ### 4. Combine the two DataFrames

# In[39]:


# merge the two DataFrames
mov_ott = pd.merge(movies, ott, how = 'left', on = "ID")

# view the DataFrame
print(mov_ott.shape)
mov_ott.head()


# ### 5. Create a countplot

# In[40]:


# create a countplot based on number of movies streamed by Netflix per age group
sns.countplot(x = "Age", hue = "Netflix", data = mov_ott)


# ### 6. Create a histogram

# In[41]:


# create a histogram based IMDb 
sns.histplot(data = mov_ott, x = "IMDb", binwidth = 1)


# ### 7. Create a scatterplot

# In[42]:


# create scatterplot with two variables (IMDb and Rotten Tomatoes)
sns.scatterplot(x = "IMDb", y = "Rotten Tomatoes", data = mov_ott)


# ### 8. Create a lineplot

# In[43]:


# create a simple lineplot
sns.lineplot(x = "Year", y = "IMDb", data = mov_ott)


# In[44]:


# create a simple lineplot
sns.lineplot(x = "Year", y = "IMDb", data = mov_ott, ci = None)


# In[45]:


# create lineplots with specification
sns.lineplot(x = "Year", y = "IMDb",
             data = mov_ott[mov_ott["Age"].isin(["16+","18+"])],
             hue = "Age")


# In[46]:


# create lineplots with specification
sns.lineplot(x = "Year", y = "IMDb",
             data = mov_ott[mov_ott["Age"].isin(["16+","18+"])],
             hue = "Age", ci = None)


# ### 9. Customise plots

# #### Barplot

# In[47]:


mov_ott_2010 = mov_ott[mov_ott['Year'] >= 2010]

ax = sns.countplot(x = "Year", data = mov_ott_2010)

ax.set(ylabel = "Percent")

total = len(mov_ott_2010["Year"])

for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height() / total)
    x = p.get_x()
    y = p.get_y() + p.get_height()
    ax.annotate(percentage, (x, y))

plt.xticks(rotation = 90)
plt.show()


# #### Histogram

# In[48]:


ax = sns.displot(data = mov_ott, x = "IMDb", bins = 10,kind = 'hist', 
                 palette = 'GnBu', aspect = 1.4, kde = True)

plt.show()


# ### 10. Highlight and annotate plots

# #### Scatterplot

# In[49]:


sns.scatterplot(data = mov_ott, x = 'IMDb', y = 'Rotten Tomatoes', hue = 'Netflix')

plt.show()


# #### Boxplot

# In[53]:


sns.boxplot(data = mov_ott, x = 'Age', y = 'IMDb', linewidth = 2,
            notch = True, hue = 'Netflix', palette = 'Set3')

plt.show()


# #### Lineplot

# In[54]:


sns.lineplot(x = 'Year', y = 'IMDb', data = mov_ott, linewidth = 0)

sns.lineplot(x = 'Year', y = 'IMDb',
            data = mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
            hue = 'Age')

sns.lineplot(x = 'Year', y = 'IMDb',
            data = mov_ott[mov_ott['Age'].isin(['16+', '18+'])],
            hue = 'Age', style = 'Age', markers = True, ci = 0)


# In[ ]:




