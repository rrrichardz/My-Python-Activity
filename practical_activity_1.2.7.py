#!/usr/bin/env python
# coding: utf-8

# ### Error codes

# In[5]:


# Code 1
# Print the price
sales_price = 24500

print(total_price)


# In[2]:


# Code 2
# Print a text string verbatim
print "My name is James Bond"


# In[3]:


# Code 3
# Determine if x is greater than 10
x = 11 

if x > 10:
print('X is greater than 10')
else: 
    print('x is not greater than 10')


# In[4]:


# Code 4
# Create the variable list_a
list_a = [1,2,3,4,'Ayaan', 'Hirsi']

list_a[11]


# ### Corrected codes

# In[7]:


# There is a naming error as 'total_price' is not defined
sales_price = 24500
# I will define total_price
total_price = sales_price + 2000

print(total_price)


# In[8]:


# Parentheses are missing around the text
print("My name is James Bond")


# In[10]:


# There is an indention error
x = 11 

if x > 10:
# I have added 4 spaces before both 'print' functions
    print('X is greater than 10')
else: 
    print('x is not greater than 10')


# In[13]:


# The list does not incude '11' so it's out of range, also in the list it can only contain integers or slices, not strings.
# So I removed the strings and added integers up to index position 11
list_a = [1,2,3,4,5,6,7,8,9,10,11,12]

list_a[11]


# In[ ]:




