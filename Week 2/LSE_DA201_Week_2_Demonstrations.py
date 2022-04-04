#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 2: Data Analytics with Python

# ## Week 2: Getting started with Pandas demonstrations

# The focus this week is on introducing, setting up, and exploring Pandas. You will use this notebook to follow along with the demonstrations throughout the week.
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelarate your learning!

# ## 2.1 Data ingestion with Pandas

# ### Series

# In[ ]:


# import Pandas library
import pandas as pd


# In[3]:


# create Pandas Series
colours = pd.Series(['green', 'red', 'yellow', 'blue', 'black', 'white'])

print(colours)


# In[5]:


# create a list
example_list = [1, 2, 3, 4, 5, 6]

# create series from a list
numbers = pd.Series(example_list)

print(numbers)


# In[10]:


# create dictionary
dict_1 = {'AU':'Australian Dollar',
         'US':'US Dollar',
         'IN':'Indian Rupee',
         'DK':'Danish Krone',
         'SW':'Swiss Franc'}

# create Series from dictionary
economics = pd.Series(dict_1)

print(economics)


# ### DataFrame

# In[13]:


#import Pandas
import pandas as pd

#create an empty DataFrame
df = pd.DataFrame()

print(df)

#create an empty Series
ser = pd.Series()

print(ser)


# In[22]:


# create a dictionary
data = {'Name' : ['Thando', 'Divya', 'Simon', 'Peter'], 
       'Conutry' : ['South Africa', 'Singapore' , 'United Kingdom', 'Australia'], 
       'Qualification' : ['PhD', 'Diploma', 'MBA', 'BSc'], 
       'Age' : ['29', '20', '25', '23']}

# create a DataFrame from the dictionary
students = pd.DataFrame(data)

students


# ### 1. Import NumPy and Pandas

# In[1]:


# import packages with standard conventions
import numpy as np
import pandas as pd


# ### 2. Upload CSV file as shown in video 

# ### 3. Read CSV file with Pandas

# In[2]:


# read CSV file with Pandas
fitness = pd.read_csv('daily_activity.csv')

fitness


# In[3]:


print(fitness.shape)
print(fitness.dtypes)


# In[4]:


print(fitness.head(3))
print(fitness.tail(3))


# In[5]:


print(fitness)


# In[6]:


#import Pandas and tabulate
import pandas as pd
import tabulate
from tabulate import tabulate

# displaying the DataFrame in plsql format
tabulate(fitness, headers = 'keys', tablefmt = 'psql')


# In[7]:


fitness.index.names = ['Observation']

fitness


# In[8]:


fitness.index.names = ['Repetitions']

fitness


# In[9]:


# create a hierarchical index
col_names2=['I1', 'I2', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
fitness = pd.read_csv("daily_activity.csv", names=col_names2,
index_col=['I1', 'I2'])

fitness


# In[10]:


# skip rows
fitness = pd.read_csv("daily_activity.csv", skiprows = [0, 1, 2, 5, 10])

fitness


# xxx.info(): gives you basic info of the DataFrame
# xxx.describe(): gives you numeric info of the DataFrame
# xxx.*column name*.hist(): gives you a histrogram
# or xxx["xxx"].hist()
# xxx.*column name*.plot(): gives you a scatter plot
# or xxx["xxx"].plot()
# 
# np.arange(1,10): use Numpy to create array from 1 to 9
# 
# xxx.__version__: check the version of a function(library)
# 
# xxx.shape: to get the total columns and rows of the data

# # 

# ## 2.2 Pandas built-in functions

# ### Subsetting data

# In[3]:


#import package
import pandas as pd

#import CSV file
fitness = pd.read_csv("daily_activity.csv")

fitness


# In[4]:


# use the head() function to subset data set
fitness.head()


# ### usecols() parameter

# In[5]:


# option 1
my_list = fitness.columns.values.tolist()

print(my_list)


# In[6]:


# option 2
my_list = list(fitness)

my_list


# In[8]:


# selecting few columns
fitness_fcol = pd.read_csv("daily_activity.csv", 
                          usecols = ['Id', 'ActivityDate', 'TotalSteps'])

fitness_fcol.head()


# ### nrows() parameter

# In[11]:


# only return the first 10 rows
fitness_nrows = pd.read_csv("daily_activity.csv", nrows = 10)

fitness_nrows


# ### skiprows() parameter

# In[12]:


# shape of data frame
print(fitness.shape)

# skiprows parameter
fitness_skiprows = pd.read_csv("daily_activity.csv", skiprows = 500)

print(fitness_skiprows.shape)


# ### skipfooter() parameter

# In[ ]:


# only for demonstration
# xxx = pd.read_csv(filename, skipfooter=1)

# xxx


# In[14]:


q2 = pd.read_csv("daily_activity.csv", 
                 usecols = ["VeryActiveDistance",
                            "ModeratelyActiveDistance", "LightActiveDistance", 
                            "SedentaryActiveDistance", 
                            "VeryActiveMinutes", 
                            "FairlyActiveMinutes", 
                            "LightlyActiveMinutes", 
                            "SedentaryMinutes"])

q2.head()


# In[17]:


q3 = pd.read_csv("daily_activity.csv",
                 nrows = 15,
                 usecols = ["Id", "Calories"])
                 
q3


# ### Add new columns to an existing DataFrame

# In[1]:


# import packages
import pandas as pd

# create dataframe for dr veldtman
data = {'Name' : ['Thiago', 'Divya', 'Simon', 'Peter'],
       'Country' : ['South Africa', 'Singapore', 'United Kingdom', 'Australia'],
       'Qualification' : ['Phd', 'Diploma', 'BSc', 'MBA'],
       'Age' : [29, 20, 25, 23]}

students = pd.DataFrame(data)

students


# In[2]:


# re-order the columns
students = pd.DataFrame(data, columns = ['Name', 'Age', 'Qualification', 'Country'])

students


# In[3]:


# add a column (Final mark)
students = pd.DataFrame (data, columns=['Name', 'Age', 'Qualification',
                                        'Country', 'Final mark'])
students


# In[4]:


# add a columns (Test 1, Tutorial 1, Test 2, Tutorial 2, Test 3, Tutorial 3)
students = pd.DataFrame (data, columns=['Name', 'Age', 'Qualification',
                                        'Country', 'Test 1', 'Tutorial 1', 
                                        'Test 2', 'Tutorial 2', 'Test 3', 
                                        'Tutorial 3', 'Final mark'])

students


# ### Add new rows to an existing DataFrame

# In[11]:


# create new DataFrame with new data
raw_data = {'Name' : ['Noncedo', 'David', 'Eugene', 'Amaira', 'Monica', 'Richard'],
           'Age' : [22, 23, 25, 24, 26, 22],
            'Qualification' : ['Diploma', 'BCom', 'Diploma', 'MCom', 'Phd', 'BCom'],
           'Country' : ['Lesotho', 'United Kingdom', 'Australia', 'India', 
                        'Poland', 'Germany']}

students_2 = pd.DataFrame(raw_data)

students_2


# In[12]:


# add rows with append()
students_final = students.append(students_2, ignore_index = True)

students_final


# In[13]:


# add rows with concat
students_concat = pd.concat([students, students_2], ignore_index = True)

students_concat


# #### Practice

# In[14]:


# prepare your workstation
import pandas as pd

fitness = pd.read_csv('daily_activity.csv')

# column names of data set
my_list = fitness.columns.values.tolist()

my_list


# In[15]:


# add column cal_cat to calculate the middle number of calories
fitness['cal_cat'] = fitness['Calories'] - fitness['Calories'].mean()

# sense-check values of cal_cat column
print(fitness['cal_cat'])

# print to sense-check column was added
print(fitness.head())


# In[16]:


# sort column from low to high to determine 
print(fitness['cal_cat'].sort_values())

# determine min value (statistical method)
print(fitness['cal_cat'].min())


# In[17]:


# determine max value (statistical method)
print(fitness['cal_cat'].max())


# In[18]:


# how many individuals per calory group (aggregate function to count the numbers)
fitness['cal_cat'].value_counts()


# In[19]:


# determine the descriptive statistics of the data set
fitness.describe()


# ### Missing data

# In[1]:


#import package
import pandas as pd

# read CSV file from the current working directory
fitness = pd.read_csv("daily_activity.csv")

fitness.head()


# In[2]:


# check for missing values
fitness_na = fitness[fitness.isna().any(axis = 1)]

fitness_na.shape


# In[4]:


# read CSV file from the current working directory
fitness_raw = pd.read_csv("daily_activity_raw.csv")

fitness_raw.head()


# In[5]:


# check for missing values
fitness_raw_na = fitness[fitness_raw.isna().any(axis = 1)]

fitness_raw_na.shape


# ### Replacing missing data

# #### Replace missing values with mean

# In[6]:


# number of missing values
fitness_raw['TotalSteps'].isnull()


# In[7]:


# sum of missing values
fitness_raw['TotalSteps'].isnull().sum()


# In[8]:


# replacing missing values with mean for TotalSteps
fitness_raw['TotalSteps'].fillna(fitness_raw['TotalSteps'].mean(), inplace = True)

fitness_raw['TotalSteps'].isnull().sum()


# In[9]:


fitness_raw['TotalDistance'].isnull().sum()


# In[10]:


fitness_raw['TotalDistance'].fillna(fitness_raw['TotalDistance'].mean(), inplace = True)

fitness_raw['TotalDistance'].isnull().sum()


# #### Replace missing values with 0

# In[11]:


# sum of missing values
fitness_raw['TrackerDistance'].isnull().sum()


# In[12]:


# replace the missing values with 0
fitness_raw['TrackerDistance'].fillna(0, inplace = True)

# sum of the missing values
fitness_raw['TrackerDistance'].isnull().sum()


# In[15]:


fitness_raw['LoggedActivitiesDistance'].isnull().sum()


# In[16]:


fitness_raw['LoggedActivitiesDistance'].fillna(0, inplace = True)

fitness_raw['LoggedActivitiesDistance'].isnull().sum()


# #### Replace missing values with forward fill

# In[17]:


# sum of missing values
fitness_raw['VeryActiveDistance'].isnull().sum()


# In[18]:


# replace missing values with forward fill
fitness_raw['VeryActiveDistance'] = fitness_raw['VeryActiveDistance'].fillna(method = 'ffill')

# sum of missing values
fitness_raw['VeryActiveDistance'].isnull().sum()


# In[19]:


# replace missing values with forward fill
fitness_raw['ModeratelyActiveDistance'] = fitness_raw['ModeratelyActiveDistance'].fillna(method = 'ffill')

# sum of missing values
fitness_raw['ModeratelyActiveDistance'].isnull().sum()


# #### Replace missing values with backward fill

# In[20]:


# sum of missing values
fitness_raw['LightActiveDistance'].isnull().sum()


# In[21]:


# replace missing values with backward fill
fitness_raw['LightActiveDistance'] = fitness_raw['LightActiveDistance'].fillna(method = 'bfill')

# sum of missing values
fitness_raw['LightActiveDistance'].isnull().sum()


# In[24]:


# replace missing values with backward fill
fitness_raw['SedentaryActiveDistance'] = fitness_raw['SedentaryActiveDistance'].fillna(method = 'ffill')

# sum of missing values
fitness_raw['SedentaryActiveDistance'].isnull().sum()


# #### Replace missing values with the minimum value

# In[25]:


# sum of missing values
fitness_raw['VeryActiveMinutes'].isnull().sum()


# In[26]:


# replace all the missing values with min
fitness_raw['VeryActiveMinutes'].fillna(fitness_raw['VeryActiveMinutes'].min(), 
                                       inplace = True)

# sum of missing values
fitness_raw['VeryActiveMinutes'].isnull().sum()


# In[27]:


# replace all the missing values with min
fitness_raw['FairlyActiveMinutes'].fillna(fitness_raw['FairlyActiveMinutes'].min(), 
                                       inplace = True)

# sum of missing values
fitness_raw['FairlyActiveMinutes'].isnull().sum()


# #### Replace missing values with the maximum value

# In[28]:


# sum of missing values
fitness_raw['LightlyActiveMinutes'].isnull().sum()


# In[29]:


# replace all the missing values with min
fitness_raw['LightlyActiveMinutes'].fillna(fitness_raw['LightlyActiveMinutes'].max(), 
                                       inplace = True)

# sum of missing values
fitness_raw['LightlyActiveMinutes'].isnull().sum()


# In[31]:


# sum of missing values
fitness_raw['SedentaryMinutes'].isnull().sum()


# In[32]:


# replace all the missing values with min
fitness_raw['SedentaryMinutes'].fillna(fitness_raw['SedentaryMinutes'].max(), 
                                       inplace = True)

# sum of missing values
fitness_raw['SedentaryMinutes'].isnull().sum()


# #### Replace all missing values with 0 since they are numeric

# In[42]:


# replace all missing values with 0 since they are numeric
# fitness_raw = fitness_raw.fillna(0)
# fitness_raw[fitness_raw.isna().any(axis = 1)]

fitness_raw.isnull().sum()


# In[ ]:





# ## 2.3 Analysing data in Pandas

# ### Indexing Pandas Series

# In[1]:


# importing Pandas package
import pandas as pd

# create series with explicit labelling
class_list = pd.Series(['Thando', 'Divya', 'Simon',
                        'Peter', 'Noncedo', 'David',
                        'Eugene', 'Amaira', 'Monica', 'Richard'],
                       index = ['2021/0562/3215', '2021/2136/2132',
                        '2021/0021/5987', '2021/3165/0468',
                        '2021/0132/5496', '2021/3698/1346',
                        '2021/0147/9632', '2021/6549/1324',
                        '2021/9513/3579', '2021/3491/7916'])

class_list


# ### Pandas Series: Indexing 

# In[2]:


# determine the values
print(class_list.values)

# determine the index
print(class_list.index)


# In[3]:


# retrieve values with an index
class_list['2021/2136/2132']


# ### Accessing values using indexes (default index or explicit index)

# In[6]:


# separate with comma
print(class_list['2021/2136/2132'], class_list['2021/3165/0468'], class_list['2021/3491/7916'])

# write as one code snippet
print(class_list[['2021/2136/2132', '2021/3165/0468', '2021/3491/7916']])


# ### Indexing a DataFrame

# In[7]:


# create a dictionary
# import Pandas if it is a new session
import pandas as pd

raw_data = {'Name' : ['Thando Sinuka', 'Divya Patterson',
                    'Simon de Wit', 'Peter Black',
                    'Noncedo Dlamini', 'David Ackerman',
                    'Eugene du Toit', 'Amaira Patteri',
                    'Monica Le Blanc', 'Richard Fortress'],
           'Age' : [29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
           'Qualification' : ['PhD', 'MSc', 'MBA', 'BSc',
                             'MCom', 'BCom', 'PhD', 'MBA',
                             'MCom', 'BCom'],
           'Country' : ['South Africa', 'Singapore', 'United Kingdom',
                       'Australia', 'Lesotho', 'United Kingdom',
                       'Canada', 'India', 'France', 'Canada']}

students = pd.DataFrame(raw_data)

students


# ### Specifying the row labels

# In[8]:


# create the data for the DataFrame
raw_data = {'Name':['Thando Sinuka', 'Divya Patterson',
                    'Simon De Wit', 'Peter Black',
                    'Noncedo Dlamini', 'David Ackerman',
                    'Eugene du Toit', 'Amaira Patteri',
                    'Monica Le Blanc', 'Richard Fortress'],
            'Age':[29, 26, 25, 23, 30, 35, 25, 27, 24, 32],
            'Qualification':['PhD', 'MSc', 'MBA', 'BSc',
                             'MCom', 'BCom', 'PhD', 'MBA', 
                             'MCom', 'BCom'],
            'Country':['South Africa', 'Singapore', 'United Kingdom',
                       'Australia', 'Lesotho', 'United Kingdom',
                       'Canada', 'India', 'France', 'Canada']}

# specify the row_lables
row_labels = ['2021/0562/3215', '2021/2136/2132',
              '2021/0021/5987', '2021/3165/0468',
              '2021/0132/5496', '2021/3698/1346',
              '2021/0147/9632', '2021/6549/1324',
              '2021/9513/3579', '2021/3491/7916']

# specify the column names
students_updated = pd.DataFrame(raw_data, columns = ['Name', 'Age', 'Qualification',
                                            'Country', 'Test 1', 'Tutorial 1',
                                            'Test 2', 'Tutorial 2', 'Test 3',
                                            'Tutorial 3', 'Final mark', 'Pass'],
                                # specify index = row_labels
                               index = row_labels)

students_updated


# ### Changing data in a particular column 

# In[11]:


# all students the same mark
students_updated['Test 1'] = 80

students_updated


# In[12]:


students_updated['Test 1'] = [82, 90, 75, 70, 88, 65, 72, 76, 85, 68]

students_updated


# In[13]:


students_updated['Tutorial 1'] = [80, 75, 79, 69, 82, 68, 90, 84, 83, 79]

students_updated


# ### Indexing: Retrieving columns from a DataFrame

# In[22]:


# option 1
print(students_updated [['Test 1', 'Tutorial 1']])

# option 2
print(students_updated.iloc[:, 4:6])


# ### Indexing: Retrieving rows from a DataFrame

# In[23]:


#option 1
print(students_updated.loc['2021/2136/2132'])

#option 2
Divya = students_updated.iloc[1]
print(Divya)


# ### Mapping values

# In[24]:


# students tutorial 2 mark
students_updated['Tutorial 2'] = [80, 75, 79, 69, 82, 68, 90, 84, 83, 79]

# map method on tut 2
# create new series
tut_2 = {80:80, 75:75, 79:76, 69:74, 82:80, 68:75,
         90:80, 84:84, 83:81, 79:80}

students_updated['tut_2'] = students_updated['Tutorial 2'].map(tut_2)

# reorder columns
students_updated = students_updated [['Name', 'Age', 'Qualification', 
                                     'Country', 'Test 1', 'Tutorial 1',
                                     'Test 2', 'Tutorial 2', 'tut_2', 
                                     'Test 3', 'Tutorial 3', 'Final mark',
                                     'Pass']]

students_updated


# ### Filtering values

# #### Filter a Series

# In[25]:


# create a class list with all the students 
class_list = pd.Series(['Thando', 'Divya', 'Simon',
                        'Peter', 'Noncedo', 'David',
                        'Eugene', 'Amaira', 'Monica', 'Richard'],
                       index=['2021/0562/3215', '2021/2136/2132',
                              '2021/0021/5987', '2021/3165/0468',
                              '2021/0132/5496', '2021/3698/1346',
                              '2021/0147/9632', '2021/6549/1324',
                              '2021/9513/3579', '2021/3491/7916'])

class_list

# filter series
class_list [class_list != 'Divya']


# #### Filter a column from a DataFrame

# In[26]:


# filter columns Tutorial 2 and tut_2
tuts_2 = students_updated [['Tutorial 2', 'tut_2']]

tuts_2


# #### Filter rows from a DataFrame

# In[28]:


# filter rows Tutorial 2 and tut_2
marks_adjusted = students_updated[students_updated['tut_2'] < 80]

marks_adjusted


# ### Sorting data

# #### Sorting a Series with index

# In[29]:


# sort index
class_list.sort_index()


# In[30]:


# sort index descending
class_list.sort_index(ascending = False)


# #### Sort data: single column (ascending and descending)

# In[32]:


#sorting: arranging the data in a certain order to derive better insights
students_updated.sort_values(by = 'Name', inplace = True)

students_updated


# In[33]:


#sorting descending
students_updated.sort_values(by = 'Name', inplace = True, ascending = False)

students_updated


# #### Sort data: multiple columns

# In[35]:


#sorting using multiple columns
students_updated.sort_values(by = ['Test 1', 'Tutorial 1'], inplace = True)

students_updated


# In[36]:


#sorting using multiple columns (descending)
students_updated.sort_values(by = ['Test 1', 'Tutorial 1'], inplace = True, ascending = False)

students_updated


# ### Descriptive statistics

# In[ ]:


# describe() function
# Python will return the count (number of observations), mean, standard deviation, 
# minimum value, maximum value, and quartiles (Q1, Q3)


# In[1]:


# count() method calculates the number of not-empty values and returns it as count


# ### Application of describe()

# In[3]:


# prepare your workstation
import pandas as pd

# read CSV file from the current working directory
fitness = pd.read_csv("daily_activity.csv")

print(fitness.shape)

# descriptive statistics
fitness.describe()


# #### Maximum, minimum, and sum of a column

# In[4]:


# max = Returns max of a column
print(fitness['TotalDistance'].max())

# min = Returns min of a column
print(fitness['TotalDistance'].min())

# sum = Returns sum of a column
print(fitness['TotalDistance'].sum())


# In[5]:


# max = Returns max of a column
print(fitness['TotalSteps'].max())

# min = Returns min of a column
print(fitness['TotalSteps'].min())

# sum = Returns sum of a column
print(fitness['TotalSteps'].sum())


# In[6]:


# max = Returns max of a column
print(fitness['Calories'].max())

# min = Returns min of a column
print(fitness['Calories'].min())

# sum = Returns sum of a column
print(fitness['Calories'].sum())


# #### Interquartile range

# In[7]:


q1 = fitness['TotalSteps'].quantile(0.25)

q3 = fitness['TotalSteps'].quantile(0.75)

iqr_TotalSteps = q3 - q1

iqr_TotalSteps


# In[8]:


q1 = fitness['Calories'].quantile(0.25)

q3 = fitness['Calories'].quantile(0.75)

iqr_Calories = q3 - q1

iqr_Calories


# In[12]:


q10th_TotalSteps = fitness['TotalSteps'].quantile(0.1)

q90th_TotalSteps = fitness['TotalSteps'].quantile(0.9)

print(q10th_TotalSteps)

print(q90th_TotalSteps)


# In[13]:


q10th_Calories = fitness['Calories'].quantile(0.1)

q90th_Calories = fitness['Calories'].quantile(0.9)

print(q10th_Calories)

print(q90th_Calories)


# #### Variance

# In[17]:


# variance of data frame
print(fitness.var())

# variance of total distance
print(fitness['TotalDistance'].var())

# variance of total steps
print(fitness['TotalSteps'].var())

# variance of calories
print(fitness['Calories'].var())


# ### Normalise a data set

# In[18]:


# prepare your workstation
import pandas as pd

# read CSV file from the current working directory
fitness = pd.read_csv('daily_activity.csv')
fitness.shape


# #### Maximum absolute scaling

# In[19]:


# values of total distance before scaling
fitness['TotalDistance']


# In[22]:


# apply the maximum absolute scaling in Pandas using the .abs() and .max() methods
def max_abs_scaling(df):
    # copy the dataframe
    df_scaled = df.copy()
    if isinstance(df_scaled, pd.DataFrame):
         # apply maximum absolute scaling
        for column in df_scaled.columns:
            df_scaled[column] = df_scaled[column] / df_scaled[column].abs().max()
    else:
        df_scaled = df_scaled / df_scaled.abs().max()
        
    return df_scaled    

# call the maximum_absolute_scaling function
fitness['TotalDistance'] = max_abs_scaling(fitness['TotalDistance'])

# call the new values of the total distance column
fitness['TotalDistance']


# #### Min-max feature scaling

# In[23]:


# values of sedentary minutes before
fitness['SedentaryMinutes']


# In[39]:


# apply the min-max scaling in Pandas using the .min() and .max() methods
def min_max_scaling(df):
    # copy the data frame
    df_scaled = df.copy()
    # apply min-max scaling
    if isinstance(df_scaled, pd.DataFrame):
        for column in df_scaled.columns:
            df_scaled[column] = (
                df_scaled[column] - df_scaled[column].min()) / (
                df_scaled[column].max() - df_scaled[column].min())
    else:
        df_scaled = (df_scaled - df_scaled.min()) / (df_scaled.max() - df_scaled.min())
    
        return df_scaled
    
# call the call the min_max_scaling function
fitness['SedentaryMinutes_new'] = min_max_scaling(fitness['SedentaryMinutes'])

# call the new values of the sedentary minutes column
fitness['SedentaryMinutes_new']


# In[42]:


# start with before
print(fitness['TrackerDistance'])

#Implementation of Maximum absolute scaling
# apply the maximum absolute scaling in Pandas using the .abs() and .max() methods
def max_abs_scaling(df):
    # copy the data frame
    df_scaled = df.copy()
    if isinstance(df_scaled, pd.DataFrame):
        # apply maximum absolute scaling
        for column in df_scaled.columns:
            df_scaled[column] = df_scaled[column] / df_scaled[column].abs().max()
    else:
        df_scaled = df_scaled / df_scaled.abs().max()
        
    return df_scaled

# call the maximum_absolute_scaling function
fitness['TrackerDistance'] = max_abs_scaling(fitness['TrackerDistance'])

fitness['TrackerDistance']


# In[44]:


# start with before
print(fitness['VeryActiveDistance'])

#Implementation of Maximum absolute scaling
# apply the maximum absolute scaling in Pandas using the .abs() and .max() methods
def max_abs_scaling(df):
    # copy the data frame
    df_scaled = df.copy()
    if isinstance(df_scaled, pd.DataFrame):
        # apply maximum absolute scaling
        for column in df_scaled.columns:
            df_scaled[column] = df_scaled[column] / df_scaled[column].abs().max()
    else:
        df_scaled = df_scaled / df_scaled.abs().max()
        
    return df_scaled

# call the maximum_absolute_scaling function
fitness['VeryActiveDistance'] = max_abs_scaling(fitness['VeryActiveDistance'])

fitness['VeryActiveDistance']


# In[52]:


# start with before
print(fitness['LightlyActiveMinutes'])

# apply the min-max scaling in Pandas using the .min() and .max() methods
def min_max_scaling(df):
    # copy the data frame
    df_scaled = df.copy()
    if isinstance(df_scaled, pd.DataFrame):
        # apply min-max scaling
        for column in df_scaled.columns:
            df_scaled[column] = (
            df_scaled[column] - df_scaled[column].min()) / (
            df_scaled[column].max() - df_scaled[column].min())
    else:
        df_scaled = (df_scaled - df_scaled.min()) / (df_scaled.max() - df_scaled.min())
                     
    return df_scaled    
                     
# call the call the min_max_scaling function
fitness['LightlyActiveMinutes_new'] = min_max_scaling(fitness['LightlyActiveMinutes'])
                     
fitness['LightlyActiveMinutes_new']


# In[54]:


# start with before
print(fitness['VeryActiveMinutes'])

# apply the min-max scaling in Pandas using the .min() and .max() methods
def min_max_scaling(df):
    # copy the data frame
    df_scaled = df.copy()
    if isinstance(df_scaled, pd.DataFrame):
        # apply min-max scaling
        for column in df_scaled.columns:
            df_scaled[column] = (
            df_scaled[column] - df_scaled[column].min()) / (
            df_scaled[column].max() - df_scaled[column].min())
    else:
        df_scaled = (df_scaled - df_scaled.min()) / (df_scaled.max() - df_scaled.min())
                     
    return df_scaled    
                     
# call the call the min_max_scaling function
fitness['VeryActiveMinutes_new'] = min_max_scaling(fitness['VeryActiveMinutes'])
                     
fitness['VeryActiveMinutes_new']


# In[ ]:




