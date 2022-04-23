#!/usr/bin/env python
# coding: utf-8

# ## Practical_Activity_5.1.5

# ### 1. Import the libraries

# In[1]:


# import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# ### 2. Establish connection with URL

# In[2]:


# create a url variable
url = "https://www.worldometers.info/coronavirus/"

# create a requests variable
r = requests.get(url)

# make contact with website
if r.status_code == 200:
    html_doc = r.text
    
# get BeaurifulSoup object
soup = BeautifulSoup(html_doc)

# print output
print(soup.prettify())


# ### 3. Extract tabular data

# In[3]:


# Extracting the contents of the table with the table id:
table = soup.find('table', attrs = {'id': 'main_table_countries_today'})

table


# ### 4. Extract table headers

# In[5]:


# Now wee need to specify beautiful soup to go through the table and find 
# everything with a tr tag.
# note = th(table header), tr = (table row) and td = table column
rows = table.find_all('tr', attrs = {'style': ''})

rows


# In[6]:


# storage for the extracted data
output = []

# specify column names
column_names = ['Country, Other', 'Total Cases', 'New Cases', 'Total Deaths',
               'New Deaths', 'Total Recovered', 'New Recovered',
               'Active Cases', 'Serious, Critical', 'Tot Cases/ 1M pop',
               'Deaths/ 1M pop', 'Total Tests', 'Tests/ 1M pop', 'Population']

# specify for loop statement
for cases in rows:
    cases_data = cases.find_all('td')
    if cases_data:
        # extract the text within each element
        cases_text = [td.text for td in cases_data]
        output.append(dict(zip(column_names, cases_text)))
        
# create output
output


# ### 5. Convert extracted data into a Panda DataFrame

# In[7]:


# create DataFrame directly from output
data = pd.DataFrame(output)

# view DataFrame
data


# In[ ]:




