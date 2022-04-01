#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 2: Data Analytics with Python

# ## Practical activity: Create a DataFrame from the dictionary

# **This is the start to the activity.**
# 
# A peer has come to you for help. They have started building a dictionary using Jupyter Notebook. Below you will find their incomplete code. 
# 
# Now that you have learned to add values and keys using a DataFrame, make changes to the code to complete the following:
# 
# - Import the dictionary into a DataFrame and add two more rows to the state and capital columns.
# - Sense-check the code that was presented to you is accurate and free from errors.

# ### Raw data
# - states = ["Acre", "Alogoas", "Amapa", "Amazonas", "Bahia", "Ceara", "Distrito Federal", 
#             "Espirito Santo", "Goiás", "Maranhao", "Mato grosso", "Mato grosso do sul", 
#             "Minas gerais", "Para", "Paraiba", "Parana", "Pernambuco", "Piaui", "Rio de Janeiro", 
#             "Rio Grande do norte", "Rio Grande do Sul", "Rondonia", "Roraima", "Santa Catarina", 
#             "Sao Paulo", "Sergipe", "Tocantins"]
# 
# - capitals = ["Rio Branco", "Maceió" "Macapá", "Manaus", "Salvador", "Fortaleza", "Brasília", 
#               "Vitória", "Goiânia", "São Luís", "Cuiabá", "Campo Grande","Belo Horizonte","Belém",
#               "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro", "Natal", "Porto Alegre", 
#               "Porto Velho", "Boa Vista", "Florianópolis", "São Paulo", "Aracaju", "Palmas"]

# ### Incomplete Dictionary

# In[1]:


# enter your own code here


# In[1]:


import pandas as pd


# In[3]:


# create a dictionary
Brazil = {'States' : ["Acre","Alogoas", "Amapa", "Amazonas", 
                     "Bahia", "Ceara", "Distrito Federal", 
                     "Espirito Santo", "Goiás", "Maranhao", 
                     "Mato grosso", "Mato grosso do sul", 
                     "Minas gerais", "Para", "Paraiba", 
                     "Parana", "Pernambuco", "Piaui", 
                     "Rio de Janeiro", "Rio Grande do norte", 
                     "Rio Grande do Sul", "Rondonia", "Roraima", 
                     "Santa Catarina", "Sao Paulo", "Sergipe", "Tocantins"],
          'Capitals' : ["Rio Branco", "Maceió", "Macapá", "Manaus", 
                     "Salvador", "Fortaleza", "Brasília", "Vitória",
                     "Goiânia", "São Luís", "Cuiabá", "Campo Grande",
                     "Belo Horizonte","Belém","João Pessoa", "Curitiba", 
                     "Recife", "Teresina", "Rio de Janeiro", "Natal", 
                     "Porto Alegre", "Porto Velho", "Boa Vista", 
                     "Florianópolis", "São Paulo", "Aracaju", "Palmas"]}

# create a DataFrame from the dictionary
Brazil_fires = pd.DataFrame(Brazil)

Brazil_fires


# In[4]:


# insert extra two states
Brazil_2 = {'States' : ['state1', 'state2'],
           'Capitals' : ['capital1', 'capital2']}

Brazil_2_fires = pd.DataFrame(Brazil_2)

Brazil_2_fires


# In[5]:


Brazil_final = Brazil_fires.append(Brazil_2_fires, ignore_index = True)

print(Brazil_final)

print(Brazil_final.shape)


# In[ ]:




