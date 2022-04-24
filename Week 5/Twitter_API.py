#!/usr/bin/env python
# coding: utf-8

# ### Twitter API

# #### 1. Create YAML file

# #### 2. Import YAML file into Jupyter Notebook

# In[1]:


# install and import YAML library
get_ipython().system('pip install pyyaml')

# import yaml
import yaml
from yaml.loader import SafeLoader

# import the yaml file - remember to specify the whole path
twitter_creds = yaml.safe_load(open('Twitter.yaml', 'r').read())


# In[2]:


# view the keys in the dictionary
twitter_creds.keys()


# #### 3. Install the Twitter API module

# In[3]:


# install twitter api
get_ipython().system('pip install twitter')

# import library
from twitter import *


# In[5]:


# pass the twitter credentials
twitter_api = Twitter(auth = OAuth(twitter_creds['access_token'],
                                  twitter_creds['access_token_secret'],
                                  twitter_creds['api_key'],
                                  twitter_creds['api_secret_key']))


# #### Connecting to Twitter

# In[6]:


# see if you are connected
print(twitter_api)


# In[8]:


# run a test with #python
some_python_tweets = twitter_api.search.tweets(q = '#python')

# view output
print(some_python_tweets)


# #### Worldwide trends

# In[9]:


# determine worldwide trends
trends_worldwide = twitter_api.trends.available(q = '#python')

# how many trends available
print(len(trends_worldwide))

# example of trends_worldwide
trends_worldwide[0]


# In[10]:


# write a twitter request
list_of_names = [_['name'] for _ in trends_worldwide]

# list of first 10
list_of_names[0:10]


# In[20]:


# find London
our_city = 'London'

# create variable
list_of_names_our_city = [_ for _ in trends_worldwide if _['name'] == our_city]

# view output
print(len(list_of_names_our_city))

# use index to find London
list_of_names_our_city[0]


# In[14]:


# list of where on earth identifies (woeid)
list_of_names_our_city[0]['woeid']


# #### Trends per city

# In[21]:


# look at trends in London
our_city_trends = twitter_api.trends.place(_id = list_of_names_our_city[0]['woeid'])

# view output
our_city_trends


# In[22]:


# look at output as DataFrame
# import Pandas
import pandas as pd

# create DataFrame
our_city_trends_pd = pd.DataFrame(our_city_trends[0]['trends'])

# view DataFrame
our_city_trends_pd


# In[23]:


# narrow list down to 100,000 tweets
our_city_trends_over100k_pd = our_city_trends_pd[our_city_trends_pd['tweet_volume'] > 100000] .sort_values('tweet_volume', ascending = False)

# view the output
print(our_city_trends_over100k_pd.shape)
our_city_trends_over100k_pd


# In[24]:


# save output as CSV file
our_city_trends_over100k_pd.to_csv('our_city_trends_over100k.csv', index = False)


# #### Common trends

# In[25]:


# find Paris
our_city = 'Paris'

# create variable
list_of_names_our_city = [_ for _ in trends_worldwide if _['name'] == our_city]

# view output
list_of_names_our_city[0]['woeid']


# In[26]:


# search for each city
# import json
import json

# search for London
london_trends = twitter_api.trends.place(_id = 44418)

# view JSON output
print(json.dumps(london_trends, indent = 4))


# In[27]:


# search for Paris
paris_trends = twitter_api.trends.place(_id = 615702)

# view JSON output
print(json.dumps(paris_trends, indent = 4))


# #### Common topics between cities

# In[28]:


# find common topics
london_trends_list = [trend['name'] for trend in london_trends[0]['trends']]

# view output
print(london_trends_list)


# In[29]:


# find common topics
paris_trends_list = [trend['name'] for trend in paris_trends[0]['trends']]

# view output
print(paris_trends_list)


# In[30]:


# find trends between cities
london_trends_set = set(london_trends_list)
paris_trends_set = set(paris_trends_list)

# set variable
common_trends = london_trends_set.intersection(paris_trends_set)

# view output
print(common_trends)


# ### Search for tweets

# #### Step 1

# In[37]:


# search a common trend
v = '#Vive la France'

# set count to 100
Count = 100


# In[39]:


# read some tweets
search_results = twitter_api.search.tweets(q = v, count = 100)

statuses = search_results['statuses']


# In[41]:


# create loop statement
for _ in range(5):
    print("Length of statuses", len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError: # no more results when next_results doesn't exist
        break
        
# create a dictionary from next_results
kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])

search_results = twitter_api.search.tweets(**kwargs)
statuses += search_results['statuses']

# print output as JSON
print(json.dumps(statuses[1], indent = 1))


# #### Step 2

# In[42]:


# check statuses
t = statuses[0]

# print the keys
t.keys()


# In[43]:


# find the id
print(t['id'])

# view the output in text
print(t['text'])

# view entities
t['entities']


# In[ ]:




