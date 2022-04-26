#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 201: Data Analytics with Python

# ## Week 5: Data scraping with Python

# The focus this week is on web scraping and SQL databases with Python. You will use this notebook to follow along with the demonstrations throughout the week.
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelarate your learning!

# ## 5.1 Web scraping

# ### BeautifulSoup

# In[3]:


# install the Beautifulsoup library
get_ipython().system('pip install beautifulsoup4')

# import the requests and Beautifulshoup library
import requests
import bs4
from bs4 import BeautifulSoup

# specify the URL
URL = "https://en.wikipedia.org/wiki/Main_Page"

# create a variable
page = requests.get(URL)

# view the HTML
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.text)


# #### Return title: Solution

# In[4]:


# determine the title of page
soup.title


# #### Return headlines: Solution

# In[5]:


# find all the main headings on the website
soup.find_all('h1')


# #### Find all paragraphs: Solution

# In[6]:


# find all paragraphs
soup.find_all('p')


# #### Find all 'a' tags: Solution

# In[8]:


# for loop to find all the 'a' tags
for link in soup.find_all('a'):
    print(link.get('href'))


# #### Return all the text: Solution

# In[10]:


# extracting all the text from the page
print(soup.get_text())


# #### Return alt text: Solution

# In[11]:


# return all alt text of images
soup.find_all('img')


# ### Scraping a website with BeautifulSoup

# In[1]:


# install the necessary libraries
get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')
get_ipython().system('pip install lxml')


# In[2]:


# import libraries
import pandas as pd
import requests

from bs4 import BeautifulSoup


# In[3]:


# import the url
url = "https://www.worldometers.info/world-population/population-by-country/"

page = requests.get(url)

# make contact with website
page


# In[4]:


# get the information from the website
if page.status_code == 200:
    html_doc = page.text
    
# look at the html code    
soup = BeautifulSoup(html_doc)

# print the output in a readable format
print(soup.prettify())


# In[7]:


# navigate to website and determine the table ID (right click: inspect)
# extracting the contents of the table with the table id:
table = soup.find('table', attrs = {'id': 'example2'})

# view the information in a readable format
print(table.prettify())


# In[8]:


# all of the rows of the table
rows = table.find_all('tr')

# view the rows
rows


# In[10]:


# storage for the extracted data
output = []

column_names = ["ID", "Country (or dependency)", "Population (2020)",
                 "Yearly Change", "Net Change", "Density (P/Km2)",
                 "Land Area (Km2)", "Migrants (net)", "Fert. Rate",
                 "Med. Age", "Urbn Pop", "World Share"]

# create a for loop statement
for country in rows:
    country_data = country.find_all('td')
    if country_data:
        # extract the text within each element
        country_text = [td.text for td in country_data]
        output.append(dict(zip(column_names, country_text)))

# create output
output


# In[11]:


# create DataFrame directly from output
data = pd.DataFrame(output)

# view DataFrame
data.head()


# In[12]:


# save DataFrame as CSV file without index
data.to_csv("countries.csv", index = False)


# In[13]:


# create a JSON file
import json
output_json = json.dumps(output)

# view output
output_json


# In[14]:


# save the json file to .json
with open("countries.json", 'w') as f:
    json.dump(output, f)


# In[15]:


# read json using pandas, output to .csv
data = pd.read_json(output_json).to_csv("countries.csv", index=False)


# In[16]:


# import csv file with pandas
# data = pd.read_json("countries.json")
data = pd.read_csv("countries.csv")

# view
data.head()


# In[18]:


# open a JSON file with Pandas
data = pd.read_json('countries.json')

data.head()


# #### Establish a connection with the website

# In[21]:


# import libraries
import requests
from bs4 import BeautifulSoup

# create variable for url
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

r = requests.get(url)

# establish contact (status code) with the website by using if statement
if r.status_code == 200:
    html_doc = r.text
    
# view data
print(r)


# #### Extract data from the website

# In[23]:


# get BeautifulSoup object
soup = BeautifulSoup(html_doc)

# view the output
print(soup.prettify())


# #### Extract data from the table

# In[24]:


# find the table elemets
tables = soup.find_all('table')

# show all the tables
tables


# #### Setting the target table

# In[25]:


# the table we want is the first one
list_of_companies = tables[0]

# print
list_of_companies


# #### Extracting all the rows

# In[26]:


# all of the rows of the table
rows = list_of_companies.find_all('tr')

# storage for the extracted data
output = []

# specify column names
column_names = ["Name", "Industry", "Revenue", "Profit",
                "Employees", "Headquarters", "Ref"]

# create a for loop statement
for company in rows:
    company_data = company.find_all('td')
    if company_data:
        company_text = [td.text for td in company_data]
        output.append(dict(zip(column_names, company_text)))
        
# view output
output


# #### Create a Pandas DataFrame

# In[27]:


# import pandas
import pandas as pd

# create a DataFrame
data = pd.DataFrame(output)

# create subset of relevant columns
data_companies = data[['Name', 'Revenue', 'Headquarters']]

# view DataFrame
data_companies


# ### Scraping data from multiple sources

# In[29]:


# specify the urls
urls = ["https://en.wikipedia.org/wiki/Walmart",
       "https://en.wikipedia.org/wiki/State_Grid_Corporation_of_China"]

# write a for loop statement
for url in urls:
    r = requests.get(url)
    if r.status_code == 200:
        html_doc = r.text
        
# create BeautifulSoup object
soup = BeautifulSoup(html_doc)

# create a for loop statement
for image_url in soup.find_all('img'):
    lower_case_text = str(image_url).lower()
    if 'logo' in lower_case_text:
        print('https:' + image_url['src'])


# ### Transforming scraped data

# In[1]:


# import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup

# create variable for url
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"

r = requests.get(url)

# establish contact (status code) with the website by using if statement
if r.status_code == 200:
    html_doc = r.text
    
# get BeautifulSoup object
soup = BeautifulSoup(html_doc)

# find the table elemets
tables = soup.find_all('table')

# the table we want is the first one
list_of_companies = tables[0]

# all of the rows of the table
rows = list_of_companies.find_all('tr')

# storage for the extracted data
output = []

# specify column names
column_names = ["Name", "Industry", "Revenue", "Profit",
                "Employees", "Headquarters", "Ref"]

# create a for loop statement
for company in rows:
    company_data = company.find_all('td')
    if company_data:
        company_text = [td.text for td in company_data]
        output.append(dict(zip(column_names, company_text)))
        
# create a DataFrame
data = pd.DataFrame(output)

# subset data set to only relevant columns
data_companies = data[['Name', 'Revenue', 'Headquarters']]

# view DataFrame
data_companies


# #### Extracting Pandas DataFrame: JSON and CSV

# In[2]:


# import JSON library
import json

# export the output as a JSON file
output_json = json.dumps(output)

# view the output
print(output_json)


# In[8]:


# read json using pandas, output to .csv
pd.read_json(output_json).to_csv("list_of_companies.csv", index = False)

# save the json file to .json
with open("list_of_companies.json", "w") as f:
    json.dump(output, f)


# #### Importing CSV and JSON files

# In[10]:


# import and read CSV file
data_csv = pd.read_csv("list_of_companies.csv")

# view the data
print(data_csv.head())

# import and read JSON file
data_json = pd.read_json("list_of_companies.json")

# view the data
data_json.head()


# In[ ]:





# # 

# ## 5.2 What is an API?

# ### HTTP

# #### HTTP: Example

# In[2]:


# import libraries
import requests
import json

# create a variable
response = requests.get("https://swapi.dev/api/people/1/")

# print the status code
print(response.status_code)

# print the json response
print(response.json())


# In[ ]:


# create a function
def print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)
    
# view output
print(response.json())


# #### HTTP: Headers

# In[3]:


# HTTP headers
info = requests.head("https://swapi.dev/api/people/1/")

print(info.headers)


# In[5]:


# create a variable
response_1 = requests.get("https://swapi.dev/api_people/")

# print the status code
print(response_1.status_code)


# ### API: Connecting and retrieving

# #### Request Access

# In[6]:


# import libraries
import requests
import json

# identify the URL to connect to
URL = "https://api.coingecko.com/api/v3/exchange_rates"

# send connection request
response = requests.get(url = URL)

# view response from URL
print(response)


# #### Retrieve headers

# In[7]:


# if and else statementto get information and status code
if response.status_code == 200:
    print(response.headers)
else:
    print(response.status_code)
    response.headers['Content-Encoding']


# #### Retrieve header values

# In[9]:


# retrieving header values with key
print(response.headers['Content-Encoding'])


# In[10]:


print(response.headers['Date'])


# In[11]:


print(response.headers['Cache-control'])


# In[12]:


print(response.headers['X-Runtime'])


# In[13]:


print(response.headers['Alternate-Protocol'])


# #### JSON response

# In[15]:


# retrieve the payload of API
response.text


# In[16]:


# type of content
print(type(response))


# In[17]:


# change response to json
response.json()


# #### Formatting JSON

# In[18]:


# get the information again from the API
r = requests.get("https://api.coingecko.com/api/v3/exchange_rates")

# view the information
print(type(r.text))
print(r.text)


# In[19]:


# parse JSON data with loads()
content = json.loads(r.text)

# view the information
print(type(content))
print(content['rates'])


# In[20]:


# formatting JSON
print(json.dumps(content, indent = 4))


# In[22]:


# formatting JSON
print(json.dumps(content, indent = 4, separators = (". ", "=")))


# ### Twitter API

# #### 1. Create YAML file

# #### 2. Import YAML file into Jupyter Notebook

# #### 3. Install the Twitter API module

# In[ ]:





# # 

# ### 5.3 Working with databases

# ### Dynamic duo: SQL and Python (Part 1)

# #### ipython-sql

# In[7]:


# % is a magic command in Jupyter Notebook, it helps to load packages.
# It will not work in a regular Python environment, only in Jupyter Notebook.
# When the % is used in front, it indicates the use of SQL.
get_ipython().run_line_magic('load_ext', 'sql')

# import operating system and the Anaconda exnvironment
import os

# PostgreSQL credentials
host = "localhost"
database = "Chinook"
user = "postgres"
# your own password
password = "x" # specify your own password

# test connection between PostgreSQL and Jupyter Notebook
connection_string = f'postgresql://{"postgres"}:{"x"}@{"localhost"}/{"Chinook"}'
    
# determine connection status
get_ipython().run_line_magic('sql', '$connection_string')


# #### Confirm connection

# In[8]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM "Album" LIMIT 10\n')


# In[10]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM "Artist" LIMIT 15\n')


# In[11]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM "Customer" LIMIT 10\n')


# In[12]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM "Genre" LIMIT 15\n')


# #### sqlalchemy

# In[4]:


# import necessary libraries to create an engine
from sqlalchemy import create_engine

# name the engine
engine = create_engine(connection_string)

# import inspect
from sqlalchemy import inspect

insp = inspect(engine)
insp.get_table_names()


# #### Confirm connection 2

# In[14]:


# import pandas
import pandas as pd

# create DataFrame
df = pd.read_sql('SELECT * FROM "Artist" LIMIT 10', engine)

df


# In[19]:


df = pd.read_sql('SELECT * FROM "Customer" LIMIT 10', engine)

df

df.to_csv("Customer.csv")


# In[20]:


df = pd.read_sql('SELECT * FROM "Genre" LIMIT 10', engine)

df

df.to_csv("Genre.csv")


# #### Practice

# In[23]:


get_ipython().run_cell_magic('sql', '', '\nSELECT "FirstName", "LastName", "Country"\nFROM "Customer"\nLIMIT 10\n')


# In[26]:


get_ipython().run_cell_magic('sql', '', '\nSELECT CONCAT("FirstName", "LastName")\nAS "FullName"\nFROM "Customer"\nLIMIT 10\n')


# #### Practice 2

# In[27]:


get_ipython().run_cell_magic('sql', '', '\nSELECT SUM("Total")\nFROM "Invoice"\nWHERE "InvoiceDate"\nBETWEEN \'2009-12-01\' AND \'2009-12-31\'\n')


# #### Practice 3

# In[28]:


get_ipython().run_cell_magic('sql', '', '\nSELECT "Name", "Composer", "Milliseconds"\nFROM "Track"\nGROUP BY "Name", "Composer", "Milliseconds"\nORDER BY "Composer" DESC\nLIMIT 10\n')


# ### Dynamic Duo: SQL and Python (Part 2)

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')

# import operating system and the Anaconda exnvironment
import os

# PostgreSQL credentials
host = "localhost"
database = "Chinook"
user = "postgres"
# your own password
password = "x" # specify your own password

# test connection between PostgreSQL and Jupyter Notebook
connection_string = f'postgresql://{"postgres"}:{"x"}@{"localhost"}/{"Chinook"}'
    
# determine connection status
get_ipython().run_line_magic('sql', '$connection_string')


# #### Practice 1

# In[2]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE most_popular_tracks AS\nSELECT ar."ArtistId", ar."Name", al."Title",\nCOUNT(*),\nSUM(ar."ArtistId")\nFROM "Artist" ar\nJOIN "Album" al USING ("ArtistId")\nJOIN "Track" tr USING ("AlbumId")\nJOIN "InvoiceLine" i USING ("TrackId")\nGROUP BY ar."ArtistId", ar."Name", al."Title"\nORDER BY COUNT(ar."ArtistId") DESC;\n')


# In[5]:


import pandas as pd

q1 = pd.read_sql('SELECT * FROM most_popular_tracks', engine)

q1


# In[6]:


# export data as csv
q1.to_csv("q1.csv")


# #### Practice 2

# In[8]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE most_popular_genres AS\nSELECT g."GenreId", g."Name", m."Name" AS media,\nCOUNT(*),\nSUM(g."GenreId")\nFROM "Genre" g\nJOIN "Track" t USING ("GenreId")\nJOIN "MediaType" m USING ("MediaTypeId")\nGROUP BY g."GenreId", g."Name", media\nORDER BY COUNT(g."GenreId") DESC;\n')


# In[9]:


q2 = pd.read_sql('SELECT * FROM most_popular_genres', engine)

q2


# In[10]:


# export data as csv
q2.to_csv("q2.csv")


# #### Practice 3

# In[11]:


get_ipython().run_cell_magic('sql', '', '\nCREATE TABLE most_popular_artist_genre AS\nSELECT ar."ArtistId", ar."Name" AS artist, g."Name" AS genre,\nCOUNT(*),\nSUM(ar."ArtistId")\nFROM "Artist" ar\nJOIN "Album" al USING ("ArtistId")\nJOIN "Track" t USING ("AlbumId")\nJOIN "Genre" g USING ("GenreId")\nGROUP BY ar."ArtistId", artist, genre\nORDER BY COUNT(ar."ArtistId") DESC;\n')


# In[12]:


q3 = pd.read_sql('SELECT * FROM most_popular_artist_genre', engine)

q3


# In[13]:


# export data as csv
q3.to_csv("q3.csv")


# In[ ]:




