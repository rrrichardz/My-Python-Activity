#!/usr/bin/env python
# coding: utf-8

# ## Practical_Activity_5.3.1

# ### 1. Import the libraries and data set

# In[2]:


# import necessary packages
import pandas as pd

# import excel file
transport = pd.read_excel("transport_costs.xlsx")

# view DataFrame
print(transport.shape)
print(transport.dtypes)
transport


# In[3]:


# drop columns 'currency' and 'distance unit'
transport_final = transport[['region', 'country', 'port',
                            'sea freight cost', 'road transport cost per km']]

transport_final


# In[9]:


# create new columns with calculated values
transport_final['total_sea_freight_costs'] = transport_final['sea freight cost'] * 2 * 4
transport_final['total_road_transport_costs'] = transport_final['road transport cost per km'] * 10000
transport_final['total_export_costs'] = transport_final['total_sea_freight_costs'] + transport_final['total_road_transport_costs']

# rearrange column orders
transport_final = transport_final[['region', 'country', 'port',
                                  'sea freight cost', 'total_sea_freight_costs',
                                  'road transport cost per km', 'total_road_transport_costs',
                                  'total_export_costs']]

# view DataFrame
transport_final


# In[10]:


# save file as CSV
transport_final.to_csv("transport_final_python.csv")


# In[ ]:




