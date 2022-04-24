#!/usr/bin/env python
# coding: utf-8

# ## Practical_Activity_5.2.4

# ### 1. Import the libraries

# In[1]:


# import libraries
import requests
import json
import pandas as pd


# ###  Bitcoin Price Index

# In[2]:


# create a requests variable
bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# print the status_code
print(bitcoin.status_code)

# print the JSON response
print(bitcoin.json())


# In[3]:


# retrieve headers
bitcoin.headers


# In[4]:


# parse JSON data with loads()
bitcoin_content = json.loads(bitcoin.text)

# view the content
print(type(bitcoin_content))
print(bitcoin_content)


# In[5]:


# formatting JSON
print(json.dumps(bitcoin_content, indent = 4))


# In[6]:


# create DataFrame directly from output
bitcoin = pd.DataFrame(bitcoin_content)

# view DataFrame
bitcoin.head()


# In[7]:


# save the json file to .json
# create JSON file
bitcoin_json = json.dumps(bitcoin_content)

with open("bitcoin_json.json", "w") as f:
    json.dump(bitcoin_content, f)
    
# save as CSV file without index
bitcoin.to_csv("bitcoin_csv.csv", index = False)


# ###  USA population data

# In[8]:


# import libraries
import requests
import pandas as pd
import json


# In[9]:


# create a requests variable
usa = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")

# print the status code
print(usa.status_code)

# print the JSON response
print(usa.json())


# In[10]:


# retrieve headers
usa.headers


# In[11]:


# parse JSON data with loads()
usa_content = json.loads(usa.text)

# view the content
print(type(usa_content))
print(usa_content)


# In[12]:


# formatting JSON
print(json.dumps(usa_content, indent = 4))


# In[ ]:




