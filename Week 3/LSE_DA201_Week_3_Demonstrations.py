#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 2: Data Analytics with Python

# ## Week 3: Data wrangling with Pandas

# The focus this week is on data ingestion and data wrangling. You will use this notebook to follow along with the demonstrations throughout the week.
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelarate your learning!

# ### 3.1 Wrangling data with Pandas

# #### Combining data sets with concat()

# In[4]:


# create a DataFrame for the car models
import pandas as pd

cars = pd.DataFrame({'VW' : ['Polo', 'T-Cross', 'Tiguan', 'Touareg'],
                    'Toyota' : ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                    'Honda' : ['Brio', 'Jazz', 'HRV', 'CRV'],
                    'BMW' : ['BMW1', 'BMW2', 'BMW3', 'BMW4']},
                   index = [0, 1, 2, 3])

cars


# In[5]:


# create a DataFrame for the motorcycle models
motorcycles = pd.DataFrame({'VW' : ['-', '-', '-', '-'],
                           'Toyota' : ['-', '-', '-', '-'],
                           'Honda' : ['Shine', 'Activa', 'Comfort Travel',
                                     'Adventure Sport'],
                           'BMW' : ['Sport', 'Roadster', 'Heritage', 'Adventure']},
                          index = [0, 1, 2, 3])

motorcycles


# In[6]:


# concatenate two DataFrames
products = pd.concat([cars, motorcycles])

products


# In[7]:


# create cars_2 DataFrame
cars_2 = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                       'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                       'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'], 
                       'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']},
                      index = ['car1', 'car2', 'car3', 'car4'])

# create motorcycles_2 DataFrame
motorcycles_2 = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                              'Toyota': ['-', '-', '-', '-'],
                              'Honda': ['Shine', 'Activa', 'Comfort Travel', 
                                        'Adventure Sport'],
                              'BMW': ['Sport', 'Roadster', 'Heritage', 'Adventure']},
                             index = ['mcycle1', 'mcycle2', 'mcycle3', 'mcycle4'])

# concatenate two DataFrames
products_2 = pd.concat([cars_2, motorcycles_2])

products_2


# #### Demonstration of the concat() function

# In[8]:


# import pandas
import pandas as pd

# read csv files
classlist_a = pd.read_csv("classlist_a.csv")

# determine shape of classlist
print(classlist_a.shape)

classlist_a.head()


# In[9]:


# read csv files
classlist_b = pd.read_csv("classlist_b.csv")

# determine shape of classlist
print(classlist_b.shape)

classlist_b.head()


# In[10]:


# read csv files
classlist_c = pd.read_csv("classlist_c.csv")

# determine shape of classlist
print(classlist_c.shape)

classlist_c.head()


# In[11]:


# read csv files
classlist_d = pd.read_csv("classlist_d.csv")

# determine shape of classlist
print(classlist_d.shape)

classlist_d.head()


# In[12]:


# concat class lists a and b
classlist_ab = pd.concat([classlist_a, classlist_b])

print(classlist_ab.shape)

classlist_ab


# In[13]:


# concat class lists c and d
classlist_cd = pd.concat([classlist_c, classlist_d])

print(classlist_cd.shape)

classlist_c


# In[14]:


# concat class lists ab and cd
classlist = pd.concat([classlist_ab, classlist_cd])

print(classlist.shape)

classlist


# #### A simpler concat() solution

# In[15]:


# concat class lists a, b, c and d
classlist_final = pd.concat([classlist_a, classlist_b, classlist_c,
                             classlist_d])

classlist_final


# In[17]:


# use sorting to organise the data set
classlist_final_sort = classlist_final.sort_values(by = 'Surname')

classlist_final_sort


# In[18]:


classlist_final_sort = classlist_final.sort_values(by = 'Student number')

classlist_final_sort


# In[19]:


# using sorted function
sorted(classlist_final.columns)


# In[20]:


# reverse sorted function
sorted(classlist_final.columns, reverse = True)


# #### Combining data sets with merge() 

# In[21]:


cars_3 = pd.DataFrame({'VW': ['Polo', 'T-Cross', 'Tiguan', 'Toureg'],
                       'Toyota': ['Agya', 'Corolla', 'Rav4', 'Land Cruiser'],
                       'Honda': ['Brio', 'Jazz', 'HRV', 'CRV'], 
                       'BMW': ['BMW1', 'BMW2', 'BMW3', 'BMW4']}, 
                     index=[0, 1, 2, 3])

cars_3


# In[22]:


motorcycles_3 = pd.DataFrame({'VW': ['-', '-', '-', '-'],
                              'Toyota': ['-', '-', '-', '-'],
                              'Honda': ['Shine', 'Activa', 'Comfort Travel',
                                        'Adventure Sport'], 
                              'BMW': ['Sport', 'Roadster', 'Heritage',
                                      'Adventure']}, 
                             index=[0, 1, 2, 3])

motorcycles_3


# In[24]:


# merge two DataFrames
products_3 = pd.merge(cars_3, motorcycles_3)

products_3


# #### Demonstration of the merge() function

# In[25]:


# merge class lists ab and cd
classlist_final = pd.merge(classlist_ab, classlist_cd,
                           how = 'outer', on = 'Student number')

print(classlist_final.shape)

classlist_final


# In[26]:


classlist_final.isna()


# ### Applying concat() and merge()

# In[1]:


# import pandas
import pandas as pd

# read CSV file from the current working directory
transactions_2010 = pd.read_csv("transactions_2010.csv")

# view the imported file
transactions_2010.head()


# In[2]:


# determine the shape and number of rows
print(transactions_2010.shape)
print(len(transactions_2010))

# how many rows?
transactions_2010


# In[3]:


# how many rows?
print(f"{transactions_2010.shape[0]} rows for transactions_2010")


# In[4]:


# read CSV file from the current working directory
transactions_2011 = pd.read_csv("transactions_2011.csv")

# how many rows?
print(f"{transactions_2011.shape[0]} rows for transactions_2011")

# view the imported file
transactions_2011.head()


# #### The concat() function

# In[15]:


# combined 2010 and 2011 transactions
transactions = pd.concat([transactions_2010, transactions_2011], axis = 0)

# view
transactions.shape

transactions


# In[8]:


# how many rows?
print(f"{transactions.shape[0]} rows for all transactions")


# #### Debug a code snippet

# In[9]:


# test if condition is true - if False will return an error message (AssertionError)
assert transactions.shape[0] == (transactions_2010.shape[0] + transactions_2011.shape[0])


# #### The merge() function

# In[10]:


# read CSV file from the current working directory
products = pd.read_csv("products.csv")

# left join
transactions_description = pd.merge(transactions, products,
                                   on = 'StockCode', how = 'left')

# view
transactions_description.head()


# #### Further uses of merge()

# In[11]:


# read CSV file from the current working directory
customers = pd.read_csv("customers.csv")

# view
customers.head()


# In[13]:


# left join
transactions_description_country = pd.merge(transactions_description, 
                                            customers, on = 'CustomerID',
                                           how = 'left')
# view
transactions_description_country.head()


# #### append() example

# In[14]:


# append two DataFrames
result_1 = transactions_2010.append(transactions_2011)

result_1


# ### The groupby() function

# In[1]:


# import Pandas
import pandas as pd

# read CSV files from the current working directory
classlist_a = pd.read_csv("classlist_a.csv")
classlist_b = pd.read_csv("classlist_b.csv")
classlist_c = pd.read_csv("classlist_c.csv")
classlist_d = pd.read_csv("classlist_d.csv")

# print the shape of each DataFrame
print(classlist_a.shape)
print(classlist_b.shape)
print(classlist_c.shape)
print(classlist_d.shape)


# In[2]:


# merge four data frames into one
classlist_final = pd.concat([classlist_a, classlist_b, classlist_c,
                            classlist_d])

classlist_final.shape


# In[3]:


# create group 1
group_surname = classlist_final.groupby("Surname")

group_surname


# In[4]:


# create group 2
group_marks = classlist_final.groupby("Final mark")

group_marks


# In[8]:


# create group 3
group_surname_marks = classlist_final.groupby(['Surname', 'Final mark'])

group_surname_marks


# In[9]:


# create splitting within groups
group_surname_marks.sum()


# ### The aggregate() function

# In[10]:


# use size()
group_surname_marks.size()


# In[11]:


# size() based on surname column
group_surname.size()


# In[14]:


# create a group based on initials
group_initials = classlist_final.groupby('Initials')

# create group_surname_initials based on columns surname and initials
group_surname_initials = classlist_final.groupby(['Surname', 'Initials'])

# size() based on initials and surname columns
group_surname_initials.size()


# In[18]:


group_student_numbers = classlist_final.groupby('Student number')

group_student_numbers.size()


# In[19]:


# use the count() function
group_surname_initials.count()


# In[24]:


group_surname_initials_marks = classlist_final.groupby(['Surname', 'Initials', 
                                                        'Final mark'])

group_surname_initials_marks.count()


# In[25]:


group_surname_marks.count()


# ### Grouping and aggregating data

# #### Preparing

# In[26]:


# import pandas
import pandas as pd

# read CSV files from the current working directory
transactions_2010 = pd.read_csv("transactions_2010.csv")
transactions_2011 = pd.read_csv("transactions_2011.csv")
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")

# print the shape of each data frame
print(transactions_2010.shape)
print(transactions_2011.shape)
print(products.shape)
print(customers.shape)


# In[28]:


# concat transactions_2010 and transactions_2011
transactions = pd.concat([transactions_2010, transactions_2011], axis = 0)
transactions.shape

# left join transactions with products
transactions_description = pd.merge(transactions, products, on = 'StockCode',
                                   how = 'left')

# left join transactions_description with customers
transactions_description_country = pd.merge(transactions_description, customers,
                                           on = 'CustomerID', how = 'left')

print(transactions_description_country.shape)
print(transactions_description_country.head())


# #### What are the total sales per country?

# In[38]:


# transaction total
transactions_description_country['SaleTotal'] = transactions_description_country['Quantity'] * transactions_description_country['UnitPrice']

# total sales by country
transactions_description_country.groupby('Country')[['SaleTotal']].sum()


# #### Which country has the most purchases?

# In[37]:


# total sales by country
# the \ indicates a line break without interrupting the code snippet
transactions_description_country.groupby('Country')[['SaleTotal']] .sum().sort_values('SaleTotal', ascending = False)


# #### What are the average sales per country?

# In[39]:


# total and mean sales by country
transactions_description_country.groupby('Country')[['SaleTotal']] .agg(['sum', 'mean'])


# #### What country has the most sales based on averages?

# In[40]:


# sort total and average sales by country
transactions_description_country.groupby('Country')[['SaleTotal']] .agg(['sum', 'mean']) .sort_values([('SaleTotal', 'sum')], ascending = False)


# In[41]:


# sort total and average sales by country
transactions_description_country.groupby('Country')[['SaleTotal']] .agg(['sum', 'mean']) .sort_values([('SaleTotal', 'mean')], ascending = False)


# #### What is the top-selling product?

# In[42]:


transactions_description_country.groupby('Description')[['SaleTotal']] .sum() .sort_values('SaleTotal', ascending = False)


# ### Reshaping the data set

# In[1]:


# import pandas
import pandas as pd

# read CSV files from the current working directory
transactions = pd.read_csv("transactions_2010.csv")
products = pd.read_csv("products.csv")

# view data set
print(transactions.shape)
print(transactions.columns)

print(products.shape)
print(products.columns)


# In[2]:


# merge the data
trans_prod = pd.merge(transactions, products, how = 'left', on = 'StockCode')

# DataFrames merged correctly?
print(trans_prod.columns)
print(trans_prod.shape)


# #### Stacking a DataFrame

# In[3]:


# stack transactions_2010.csv from DataFrame to Series
transactions_stack = transactions.stack()

transactions_stack


# In[4]:


# view data type
print(type(transactions_stack))

# view index
print(transactions_stack.index)


# #### Unstacking a DataFrame

# In[5]:


# unstack customers_stack df
transactions_1 = transactions_stack.unstack()

transactions_1.head()


# In[6]:


# view data type
print(type(transactions_1))

# view index
print(transactions_1.index)


# #### Melting a DataFrame

# In[7]:


# melt products
trans_prod.melt(id_vars = 'StockCode', value_vars = 'Description')


# In[11]:


# view data type
print(type(trans_prod))

# view index
print(trans_prod.index)


# #### Pivoting a DataFrame

# In[12]:


# import pandas
import pandas as pd

# read CSV file from the current working directory
astronauts = pd.read_csv("astronauts.csv")

#view
print(astronauts.shape)
print(astronauts.columns)


# In[13]:


# What is the status and number of space flights undertaken by
# each astraonaut?

# pivot astronauts df
astronauts.pivot(index = 'Name', columns = 'Status', values = 'Space Flights')


# In[14]:


# What is the status, number of spacewalks and spaceflight
# for each astronaut?

# pivot astronauts df
astronauts.pivot(index = 'Name', columns = 'Status', 
                 values = ['Space Walks', 'Space Flights'])


# In[ ]:





# ### 3.2 Pandas functions

# ### The map() function

# #### Mapping on a single column

# In[15]:


# import pandas as pd
import pandas as pd

# read CSV files from the current working directory
classlist_a = pd.read_csv("classlist_a.csv")
classlist_b = pd.read_csv("classlist_b.csv")
classlist_c = pd.read_csv("classlist_c.csv")
classlist_d = pd.read_csv("classlist_d.csv")

# concat the four class lists
classlist = pd.concat([classlist_a, classlist_b, classlist_c, classlist_d])

# view the DataFrame
print(classlist.shape)
print(classlist.columns)
print(classlist.dtypes)


# In[16]:


# map() function only on Pandas Series
classlist['Class_num'] = classlist.Class.map({'A' : 0, 'E' : 1})

print(classlist.shape)
classlist.head()


# #### Compare two columns

# In[17]:


# compare columns Class and Class_num with loc() function
print(classlist.loc[:, ['Class', 'Class_num']])

# compare columns Class and Class_num with iloc() function
classlist.iloc[:, 4 : 6]


# #### Change column name

# In[18]:


# rename column Final mark to Final_mark
classlist_final = classlist.rename(columns = {'Final mark' : 'Final_mark'})

classlist_final


# In[19]:


# average of Final_mark for the whole class list
classlist_final['Final_mark'].mean()


# ### The apply() function

# #### Pandas Series: apply()

# In[20]:


# apply() function applies a function to each element within a Series
classlist['Surname_length'] = classlist.Surname.apply(len)

classlist.head()


# #### Pandas DataFrame: apply()

# In[21]:


# import a CSV data set with a URL from a website
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.shape)
print(drinks.dtypes)
drinks.head()


# In[27]:


# add .apply() to the DataFrame
# use subset, all rows certain columns
drinks_country = drinks.loc[:, 'country' : 'wine_servings']

print(drinks_country)


# In[29]:


# apply a method to go downward direction and apply max and min function per column
print(drinks_country.loc[:, 'beer_servings' : 'wine_servings'].apply(max, axis = 0))
print(drinks_country.loc[:, 'beer_servings' : 'wine_servings'].apply(min, axis = 0))


# In[31]:


# total consumption by country
# sort total and consumption by country
drinks_country['country_total'] = drinks_country['beer_servings'] + drinks_country ['spirit_servings'] + drinks_country['wine_servings']

drinks_country.sort_values('country_total', ascending = False)


# #### Practice apply() function

# In[32]:


# import libraries
import pandas as pd
import numpy as np

# read CSV file from the current working directory
transactions_2010 = pd.read_csv('transactions_2010.csv')

# view DataFrame
print(transactions_2010.shape)

# mean quantity and price
transactions_2010[['Quantity', 'UnitPrice']].apply(np.mean)


# In[34]:


# max and min quantity and price
print(transactions_2010[['Quantity', 'UnitPrice']].apply(np.max))
print(transactions_2010[['Quantity', 'UnitPrice']].apply(np.min))


# In[35]:


# read CSV file from the current working directory
transactions_2011 = pd.read_csv('transactions_2011.csv')

# view DataFrame
print(transactions_2011.shape)

# mean quantity and price
transactions_2011[['Quantity', 'UnitPrice']].apply(np.mean)


# ### The applymap() function

# In[36]:


# import a CSV data set with a URL from a website
drinks = pd.read_csv('http://bit.ly/drinksbycountry')

print(drinks.shape)
print(drinks.dtypes)

# employ the applymap function to specified columns
drinks_new = drinks.loc[:, 'beer_servings' : 'wine_servings'].applymap(float)

drinks_new.dtypes


# #### Practice applymap() function

# In[38]:


# import libraries
import pandas as pd

# read CSV file from the current working directory
products = pd.read_csv('products.csv')

# view DataFrame
print(products.shape)

number_of_chars = products.applymap(len) .rename(columns = {'StockCode' : 'LenStockCode', 'Description' : 'LenDescription'})

number_of_chars.head()


# In[39]:


# concatenate the columns, sort by the length of the product description
pd.concat([products, number_of_chars], axis = 1).sort_values('LenDescription')


# In[7]:


import pandas as pd
import numpy as np

customers = pd.read_csv("customers.csv")

customers.dtypes


# In[9]:


number_of_chars_country = customers[['Country']].applymap(len) .rename(columns = {'Country' : 'LenCountry'}).apply([np.min, np.max])

print(number_of_chars_country)


# ### User-defined functions

# In[1]:


# import pandas
import pandas as pd

# read CSV file from the current working directory
products = pd.read_csv('products.csv')

products.shape


# In[2]:


# create an user-defined function
def contains_glass(x):
    """ Does the product contain glass? """
    y = x.lower()
    return "glass" in y

print(contains_glass(x = 'Glass bottle'))
print(contains_glass(x = 'glass bottle'))
print(contains_glass(x = 'bottle'))


# In[4]:


# apply the function with the apply() function
fc = products['Description'].apply(contains_glass)

# view
print(fc)

# filter
products[fc]


# # 

# ### lambda function

# #### one argument

# In[10]:


# basic lambda example
example = lambda x: x * 2

example(10)


# #### multiple arguments

# In[13]:


# basic lambda example, multiple arguments
example_2 = lambda x, y, z: x * 2 + y - z

example_2(5, 10, 15)


# #### lambda function and filter() function

# In[1]:


# create list
sequence = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]

# lambda and filter function
filter_answer = filter(lambda x: x > 6, sequence)

list(filter_answer)


# #### lambda function and map() function

# In[2]:


# create a list
sequence = [10, 2, 8, 7, 5, 4, 11]

# lambda and map function
squared_result = map(lambda x: x * x, sequence)

list(squared_result)


# #### lambda function: combine values

# In[5]:


# combine two values into one with lambda
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

full_name("         vincent", "      van gogh")


# In[ ]:




