#!/usr/bin/env python
# coding: utf-8

# ## Practical_Activity_5.2.8

# ### 1. Import YAML file and libraries

# In[13]:


# copy the YAML file and your Twitter keys over before you start to work
import yaml
from yaml.loader import SafeLoader
from twitter import *

# import the yaml file - remember to specify the whole path
twitter_creds = yaml.safe_load(open('twitter.yaml', 'r').read())

# pass your twitter credentials
twitter_api = Twitter(auth = OAuth(twitter_creds['access_token'],
                                 twitter_creds['access_token_secret'], 
                                 twitter_creds['api_key'],
                                 twitter_creds['api_secret_key'] ))


# In[14]:


# see if you are connected
print(twitter_api)


# In[15]:


# run a test with #python
python_tweets = twitter_api.search.tweets(q = '#python')

# view output
print(python_tweets)


# ### 2. Identify New York and London

# In[16]:


# determine worldwide trends
trends_worldwide = twitter_api.trends.available()

# how many trends available
print(len(trends_worldwide))

# example of trends_worldwide
trends_worldwide[0]


# #### New York

# In[23]:


# find New York
our_city = 'New York'

# create variable
list_of_names_our_city = [_ for _ in trends_worldwide if _['name'] == our_city]

# view output
print(len(list_of_names_our_city))

# use index to find New York
print(list_of_names_our_city[0])

# list of where on earth identifies (woeid)
list_of_names_our_city[0]['woeid']


# #### London

# In[22]:


# find London
our_city_2 = 'London'

# create variable
list_of_names_our_city_2 = [_ for _ in trends_worldwide if _['name'] == our_city_2]

# view output
print(len(list_of_names_our_city_2))

# use index to find London
print(list_of_names_our_city_2[0])

# list of where on earch identifies (woeid)
list_of_names_our_city_2[0]['woeid']


# ### 3. Common trends

# #### New York

# In[24]:


# look at trends in New York
our_city_trends = twitter_api.trends.place(_id = list_of_names_our_city[0]['woeid'])

# view output
our_city_trends


# In[25]:


# look at output as DataFrame
# import Pandas
import pandas as pd

# create DataFrame
our_city_trends_pd = pd.DataFrame(our_city_trends[0]['trends'])

# view DataFrame
our_city_trends_pd


# In[26]:


# narrow list down to 50,000 tweets
our_city_trends_over50k_pd = our_city_trends_pd[our_city_trends_pd['tweet_volume'] > 50000] .sort_values('tweet_volume', ascending = False)

# view the output
print(our_city_trends_over50k_pd.shape)
our_city_trends_over50k_pd


# In[27]:


# save output as CSV file
our_city_trends_over50k_pd.to_csv('NY_our_city_trends_over50k.csv', index=False)


# #### London

# In[28]:


# look at trends in London
our_city_trends_2 = twitter_api.trends.place(_id = list_of_names_our_city_2[0]['woeid'])

# view output
our_city_trends_2


# In[29]:


# look at output as a DataFrame
# import Pandas
import pandas as pd

# create DataFrame
our_city_trends_2_pd = pd.DataFrame(our_city_trends_2[0]['trends'])

# view DataFrame
our_city_trends_2_pd


# In[30]:


# narrow list down to 50 000 tweets
our_city_trends_2_over50k_pd = our_city_trends_2_pd[our_city_trends_2_pd['tweet_volume'] > 50000].sort_values('tweet_volume', ascending=False)

# view the output
print(our_city_trends_2_over50k_pd.shape)
our_city_trends_2_over50k_pd


# In[31]:


# save output as CSV file
our_city_trends_2_over50k_pd.to_csv('_London_our_city_trends_2_over50k.csv', index=False)


# ### Compare cities

# In[32]:


# find New York
our_city = 'New York'

# create variable
list_of_names_our_city = [_ for _ in trends_worldwide if _['name'] == our_city]

# view output
list_of_names_our_city[0]['woeid']


# In[33]:


# find London
our_city_2 = 'London'

# create variable
list_of_names_our_city_2 = [_ for _ in trends_worldwide if _['name'] == our_city_2]

# view output
list_of_names_our_city_2[0]['woeid']


# In[34]:


# search for each city
# import json
import json

# search for New York
new_york_trends = twitter_api.trends.place(_id = 2459115)

# view JSON output
print(json.dumps(new_york_trends, indent = 4))


# In[35]:


# search for each city
# import json
import json

# search for London
london_trends = twitter_api.trends.place(_id = 44418)

# view JSON output
print(json.dumps(london_trends, indent = 4))


# In[36]:


# find common topics
new_york_trends_list = [trend['name'] for trend in new_york_trends[0]['trends']]

# view output
print(new_york_trends_list)


# In[37]:


# find common topics
london_trends_list = [trend['name'] for trend in london_trends[0]['trends']]

# view output
print(london_trends_list)


# In[38]:


# find trends between cities
new_york_trends_set = set(new_york_trends_list)
london_trends_set = set(london_trends_list)

# set variable
common_trends = new_york_trends_set.intersection(london_trends_set)

# view output
print(common_trends)


# ### Search for #Bitcoin

# In[40]:


# run a test with #Bitcoin
bitcoin_tweets = twitter_api.search.tweets(q = '#Bitcoin')

# view JSON output
print(json.dumps(bitcoin_tweets, indent = 4))


# In[ ]:




