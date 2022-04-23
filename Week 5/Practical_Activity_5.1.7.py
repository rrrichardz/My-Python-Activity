#!/usr/bin/env python
# coding: utf-8

# ## Previous Activity

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

# In[4]:


# Now wee need to specify beautiful soup to go through the table and find 
# everything with a tr tag.
# note = th(table header), tr = (table row) and td = table column
rows = table.find_all('tr', attrs = {'style': ''})

rows


# In[5]:


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

# In[6]:


# create DataFrame directly from output
data = pd.DataFrame(output)

# view DataFrame
data


# ## New Activity Starts Here

# ## Practical Activity 5.1.7

# ### 6. Convert, clean and analyse the data

# In[13]:


# save DataFrame as CSV file without index
data.to_csv('cases.csv', index = False)


# In[8]:


# create a JSON file
import json

output_json = json.dumps(output)

# view output
output_json


# In[9]:


# save the json file to .json
with open("cases_json.json", "w") as f:
    json.dump(output, f)


# In[11]:


# read json using pandas, output to .csv
pd.read_json(output_json).to_csv("cases_csv.csv", index = False)


# In[14]:


# import and read CSV file
data_csv = pd.read_csv("cases_csv.csv")

# view the data
print(data_csv.head())

# import and read JSON file
data_json = pd.read_json("cases_json.json")

# view the data
data_json.head()


# In[15]:


# view CSV and JSON DataFrames
print(data_csv.dtypes)
print(data_csv.columns)

print(data_json.dtypes)
print(data_json.columns)


# In[17]:


# create a subset
data_report = data_csv[['Country, Other', 'Total Cases', 'Total Deaths',
                        'Total Recovered', 'Active Cases', 'Serious, Critical']]

data_report.columns


# In[18]:


# determine missing values
data_report.isnull().sum()


# In[19]:


# save DataFrame as CSV file without index
data_report.to_csv("cases_report.csv", index = False)


# In[20]:


# view saved CSV
cases_report = pd.read_csv('cases_report.csv')

cases_report.head()


# In[ ]:




