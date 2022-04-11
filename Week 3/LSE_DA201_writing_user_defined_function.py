#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 2: Data Analytics with Python

# ## Writing a user-defined function (demonstration video)

# Watch this video to understand the basics of how to write user-defined functions in Python. Feel free to pause the video when the code snippets are introduced. You can then try using them yourself. If you are sure you understand the code snippets, press play and continue to watch.
# 
# In this video, you will learn:
# - What is a user-defined function?
# - Why do you need to write a user-defined function?
# - What are the best practices for writing a user-defined function?

# ### Example of Python function

# In[2]:


# Python has basic building blocks
import pandas as pd

# create a DataFrame
data = [['John', 'Smith', '39'],
       ['Mary', 'Jane', '25'],
       ['Jennifer', 'Doe', '28']]

table = pd.DataFrame(data, columns = ['First Name', 'Last Name', 'Age'])

table


# # 

# ### user-defined function

# In[ ]:


# example of an user-defined function
# def function_name (parameter_1, parameter_2):
#     "function_docstring"
#     function_suite3
#     return[expression]


# In[4]:


# write your first user-defined function

def calculator(a, b):
    print('Addition', a+b)
    print('Subtract', a-b)
    print('Multiplication', a*b)
    print('Division', a/b)
    return;

calculator(25, 5)


# In[5]:


# write user-defined function
def f(x):
    y = (x * 2) + 10
    return y

# stipulate what to calculate
f(x=3)


# In[11]:


sum([1, 2, 4])


# In[ ]:




