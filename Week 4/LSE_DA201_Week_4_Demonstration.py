#!/usr/bin/env python
# coding: utf-8

# #### **LSE Data Analytics Online Career Accelerator** 
# #### Course 2: Data Analytics with Python

# ## Week 4: Data visualisation with Python

# The focus this week is on data visualisation with Python. You will use this notebook to follow along with the demonstrations throughout the week.
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelarate your learning!

# ## 4.1 Data visualisation with Seaborn

# ### Matplotlib

# #### Create a single figure

# In[1]:


# import matplotlib library
import matplotlib.pyplot as plt

# create an empty plot
fig, ax = plt.subplots()


# In[2]:


# draw a line by specifying the axes
ax.plot([1, 2, 3, 4], [4, 3, 2, 1])

# view the figure
fig


# In[3]:


# draw a line by specifying the axes
ax.plot([1, 2, 3, 4], [1, 2, 3, 4])

# view the figure
fig


# #### Create a figure with multiple plots

# In[4]:


# create a 2x2 figure by specifying the nrols and ncols parameters
fig2, ((top_left, top_right), (bottom_left, bottom_right)) = plt.subplots(2, 2)


# In[7]:


# specify each variable
top_left.plot([1, 2, 3, 4], [1, 1, 1, 1], color = 'blue')
top_right.plot([1, 2, 3, 4], [1, 1, 1, 1], color = 'red')
bottom_left.plot([1, 2, 3, 4], [1, 1, 1, 1], color = 'black')
bottom_right.plot([1, 2, 3, 4], [1, 1, 1, 1], color = 'orange')

# view the figure
fig2


# In[9]:


# set background colour of figure
fig2.set_facecolor('grey')

# view the figure
fig2


# #### Plot function, colour, markers, and line styles

# In[10]:


# create an empty figure with two axes
fig, ax = plt.subplots()


# ##### One positional argument

# In[11]:


# specify only one argument = y-values
ax.plot([0, 10, 20, 30, 40])

# view the figure
fig


# ##### Two positional arguments

# In[12]:


# specify two arguments = y-values and x-values
ax.clear()
ax.plot([0, 1, 2, 3, 4], [4, 3, 2, 1, 0])

# view the figure
fig


# ##### Three positional arguments

# In[13]:


# speficy three arguments = y-values, x-values and marker
ax.clear()
ax.plot([0, 1, 2, 3, 4], [4, 3, 2, 1, 0], 'og-')

# view the figure
fig


# In[14]:


# speficy three arguments = y-values, x-values and marker
ax.clear()
ax.plot([0, 1, 2, 3, 4], [4, 3, 2, 1, 0], 'xb')

# view the figure
fig


# #### Named arguments

# In[17]:


# specify various named arguments
ax.clear()
ax.plot([0, 1, 2, 3, 4], 
        [4, 3, 2, 1, 0],
       color = '#94CEE4',
       marker = 'x',
       markeredgecolor = 'red',
       drawstyle = 'steps',
       linestyle = ':')

# view the figure
fig


# ### Matplotlib vs. Seaborn

# In[4]:


# Matplotlib
# import matplotlib library
import matplotlib.pyplot as plt

# draw a line by specifying the axes
ax.plot([1, 2, 3, 4], [4, 3, 2, 1])

# view the figure
fig


# In[6]:


# Seaborn
# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# create plot
sns.relplot(x = [0, 1, 2, 3, 4], y = [4, 3, 2, 1, 0], kind = 'line')


# ### Countplots with Seaborn

# In[7]:


# import matplotlib, seaborn and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Create a countplot

# In[8]:


# create a countplot with Seaborn
sns.countplot(x = 'island', data = penguins)


# In[9]:


# create a countplot with Seaborn (2)
sns.countplot(y = 'island', data = penguins)


# In[10]:


# create a countplot with Seaborn (3)
sns.countplot(x = 'island', hue = 'species', data = penguins)


# ### Pointplots with Seaborn

# In[11]:


# import matplotlib, seaborn and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
mpg = pd.read_csv("mpg.csv")

# view the DataFrame
print(mpg.shape)
print(mpg.dtypes)
print(mpg.columns)
mpg.head()


# #### Create a pointplot

# In[15]:


# correct method
# create a pointplot for fuel efficiency
sns.pointplot(x = 'model_year', y = 'mpg', data = mpg)


# In[16]:


# create a pointplot for fuel efficiency (2)
sns.pointplot(x = 'model_year', y = 'mpg', hue = 'origin', data = mpg)


# In[13]:


# incorrect method
# using lineplot instead of pointplot

# create a lintplot for fuel efficiency
sns.lineplot(x = 'model_year', y = 'mpg', data = mpg)


# In[14]:


# incorrect method (2)
# using barlot instead of pointplot

# create a barplot for fuel efficiency
sns.barplot(x = 'model_year', y = 'mpg', data = mpg)


# ### Barplots with Seaborn

# In[2]:


# import matplotlib, seaborn and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
fitness = pd.read_csv("daily_activity.csv")

# view the DataFrame
print(fitness.shape)
print(fitness.dtypes)
print(fitness.columns)
fitness.head()


# #### Simple barplots

# In[3]:


# create a DataFrame with specified columns
distance = fitness[['Id', 'ActivityDate', 'VeryActiveDistance',
                   'ModeratelyActiveDistance', 'LightActiveDistance',
                   'SedentaryActiveDistance']]

# view the DataFrame
print(distance.head())

# reshape the DataFrame from wide to long
distance_long = distance.melt(id_vars = ['Id', 'ActivityDate'],
                             var_name = 'DistanceType',
                             value_name = 'Distance')

# view the DataFrame
print(distance_long.head())

distance_long['DistanceType'] = distance_long['DistanceType'].str.replace('ActiveDistance', "")

# add a filter to identify logged-in user
individual = distance_long[distance_long['Id'] == 1503960366]

# create a barplot
sns.barplot(x = 'DistanceType', y = 'Distance', estimator = sum, data = individual)


# #### Stacked barplots

# In[4]:


# stacked barpltos with Pandas
individual.groupby('DistanceType')[['Distance']].sum().T.plot.bar(stacked = True)


# #### Grouped barplots

# In[5]:


# pair the data of two individuals
pair = distance_long[distance_long['Id'].isin([8877689391, 1503960366])]

# create a grouped barplot
sns.barplot(x = 'DistanceType', y = 'Distance', hue = 'Id', estimator = sum,
           data = pair)


# ### Histograms with Seaborn

# In[6]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
fitness = pd.read_csv("daily_activity.csv")

# view the DataFrame
print(fitness.shape)
print(fitness.dtypes)
print(fitness.columns)
fitness.head()


# #### Create histogram

# In[8]:


# create single_day variable
# specify a chosen day within the ActivityDate column and fitness DataFrame
single_day = fitness[fitness['ActivityDate'] == '4/12/2016']

# view the output
print(single_day.shape)

# create the histogram
sns.histplot(data = single_day, x = 'TotalDistance')


# In[14]:


# create single_day variable
# specify a chosen day within the ActivityDate column and fitness DataFrame
single_day_2 = fitness[fitness['ActivityDate'] == '5/12/2016']

# view the output
print(single_day_2.shape)

# create the histogram
sns.histplot(data = single_day_2, x = 'TotalSteps')


# #### Change bin size

# In[15]:


# create the histogram and set binwidth = 1
sns.histplot(data = single_day, x = 'TotalDistance', binwidth = 1)


# In[16]:


# set binwidth = 2
sns.histplot(data = single_day, x = 'TotalDistance', binwidth = 2)


# In[17]:


# set binwidth = 3
sns.histplot(data = single_day, x = 'TotalDistance', binwidth = 3)


# ### Scatterplots with Seaborn

# In[18]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
fitness = pd.read_csv("daily_activity.csv")

# view the DataFrame
print(fitness.shape)
print(fitness.dtypes)
print(fitness.columns)
fitness.head()


# #### Create a scatterplot with two variables

# In[19]:


# create single_day variable
# specify a chosen day within the ActivityDate column and fitness DataFrame
single_day = fitness[fitness['ActivityDate'] == '4/12/2016']

# view the output
print(single_day.shape)

# create the scatterplot
sns.scatterplot(x = 'TotalSteps', y = 'Calories', data = single_day)


# #### Create a scatterplot with three variables

# In[20]:


# create a scatterplot with three variables
sns.scatterplot(x = 'TotalDistance', y = 'Calories', marker = 'o',
               hue = 'VeryActiveMinutes', size = 'VeryActiveMinutes',
               legend = 'full', data = single_day)

# adjust legend position
plt.legend(bbox_to_anchor = (1.05, 1))


# #### Create a scatterplot with a regression line

# In[22]:


# create a scatterplot with a regression line
sns.regplot(x = 'TotalDistance', y = 'Calories', data = single_day)


# In[23]:


# create a scatterplot with a regression line
sns.regplot(x = 'TotalDistance', y = 'Calories', data = single_day, ci = None)


# ### Outlier analysis: Pairplots

# In[1]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Create a pairplot

# In[2]:


# create a simplt pairplot
sns.pairplot(penguins)


# #### Pairplot: Layered kernel density estimate

# In[3]:


# create a pairplot with KDE (kernel density estimate)
sns.pairplot(penguins, hue = 'species')


# #### Pairplot: Facetgrid method

# In[4]:


# create a pairplot with the facetgrid method
sns.pairplot(penguins, hue = 'species', diag_kind = 'hist')


# #### Pairplot: Adjusting size

# In[11]:


# create a pairplot and indicate the height
sns.pairplot(penguins, hue = 'species', diag_kind = 'hist', height = 2)


# In[12]:


# remove redundant plots
sns.pairplot(penguins,
            x_vars = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'],
            y_vars = ['bill_length_mm', 'bill_depth_mm'])


# ### Outlier analysis: Boxplots

# In[13]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Create a boxplot (1)

# In[14]:


# create a boxplot
sns.boxplot(data = penguins, x = 'species', y = 'body_mass_g')


# #### Create a boxplot (2)

# In[15]:


# create a boxplot with third variable
sns.boxplot(data = penguins, x = 'species', y = 'body_mass_g', hue = 'sex')


# #### Create a boxplot: Specified order of variables

# In[17]:


# specify the order of variables
my_order = penguins.groupby(by = ['species']).median('body_mass_g').iloc[: : -1].index

# create a boxplot based on the order of variables
sns.boxplot(x = 'species', y = 'body_mass_g', data = penguins, order = my_order)


# ### Lineplots with Seaborn

# In[18]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
fitness = pd.read_csv("daily_activity.csv")

# view the DataFrame
print(fitness.shape)
print(fitness.dtypes)
print(fitness.columns)
fitness.head()


# #### Create a lineplot

# In[20]:


# create a simple lineplot
sns.lineplot(x = 'ActivityDate', y = 'TotalSteps', data = fitness)


# #### Lineplots: Confidence interval

# In[22]:


# create a time series
steps_time_series = fitness .groupby('ActivityDate')[['TotalSteps']] .sum() .reset_index() .copy()

# format data with datetime() function
steps_time_series['ActivityDate'] = pd.to_datetime(steps_time_series['ActivityDate'])

# view the output
print(steps_time_series.head())

# create a lineplot with confidence level shade
sns.lineplot(x = 'ActivityDate', y = 'TotalSteps', data = steps_time_series)


# #### Lineplots: Remove confidence interval

# In[23]:


# create a simple lineplot
sns.lineplot(x = 'ActivityDate', y = 'TotalSteps', data = fitness, ci = None)


# #### Lineplots: Improve quality

# In[27]:


# create plot size
plt.figure(figsize = (18, 6))

# create a lineplot with specific date
sns.lineplot(x = 'ActivityDate', y = 'TotalSteps', 
             data = steps_time_series[steps_time_series['ActivityDate'] < '2016-05-01'])


# ### Relational plots with Seaborn

# In[28]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Create a relational lineplot

# In[29]:


# create a scatterplot
# difficult to interpret any relations
sns.scatterplot(x="bill_length_mm", y="flipper_length_mm", hue="sex", data=penguins)


# In[30]:


# set the size of the font
sns.set(font_scale = 2)

# create a relational plot
sns.relplot(x = 'bill_length_mm', y = 'flipper_length_mm', hue = 'sex',
            data = penguins, col = 'species')


# #### Relational lineplot: Refining

# In[31]:


# set the size of the plot
sns.set(font_scale = 1.5)

# create a relational plot
sns.relplot(x = 'bill_length_mm', y = 'flipper_length_mm', hue = 'sex',
           data = penguins, col = 'species', row = 'island')


# In[ ]:





# ## 4.2 Customising plots with Seaborn and Matplotlib

# ### Scatterplot with Matplotlib: plotting colours

# In[1]:


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# create three parameters
x = [1, 2, 3, 4]
y = [6, 7, 8, 9]
colors = ['red', 'orange', 'yellow', 'green']

# create scatterplot
plt.scatter(x, y, c = colors)


# In[2]:


# specify the cmap
colors = [0, 0.333, 0.667, 1.0]

# create figure
fig, ax = plt.subplots()

# create the colour (c) values with Numpy methods
# specify color as numbers
fig, ax.scatter(x, y, c = colors)


# In[3]:


# create two parameters
# create random variables with Numpy for x and y
np.random.seed(290465)
x = np.random.rand(400)
y = np.random.rand(400)

# create figure
fig, ax = plt.subplots()

# create the colour (c) values with Numpy methods
# specify cmap as gray
plt.scatter(x, y, cmap = 'gray', c = (np.sqrt(np.square(x) + np.square(y))))


# In[5]:


# create the colour (c) values with Numpy methods
# specify cmap as purple
plt.scatter(x, y, cmap = 'Purples', c = (np.sqrt(np.square(x) + np.square(y))))


# ### Barplot with Matplotlib: categorical palettes

# In[6]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Create barplot

# In[7]:


# create a variable
penguin_sample_size = 10

# create a second variable
random_penguins = penguins.sample(n = penguin_sample_size)

# create an empty plot
fig, ax = plt.subplots()

# set the figure size
fig.set_size_inches(8, 8)

# create a barplot and specify parameters
plt.bar(list(range(penguin_sample_size)),
       random_penguins['body_mass_g'],
       color = ['green', 'red'])

# specify ticks, labels, and title
ax.set_xticks(list(range(penguin_sample_size)))
ax.set_xlabel('Penguin Number')
ax.set_ylabel('Body Mass (g)')
ax.set_title('Penguins Masses')


# In[8]:


# create a variable
penguin_sample_size = 15

# create a second variable
random_penguins = penguins.sample(n = penguin_sample_size)

# create an empty plot
fig, ax = plt.subplots()

# set the figure size
fig.set_size_inches(8, 8)

# create a barplot and specify parameters
plt.bar(list(range(penguin_sample_size)),
       random_penguins['body_mass_g'],
       color = ['blue', 'yellow'])

# specify ticks, labels and title
ax.set_xticks(list(range(penguin_sample_size)))
ax.set_xlabel('Penguin Number')
ax.set_ylabel('Body Mass (g)')
ax.set_title('Penguins Masses')


# #### Named Colourmap: Pastel2 colourmap

# In[14]:


# create a variable
penguin_sample_size = 10

# create a second variable
random_penguins = penguins.sample(n = penguin_sample_size)

# create an empty plot
fig, ax = plt.subplots()

# set the plot size
fig.set_size_inches(8, 8)

# create a barplot
plt.bar(list(range(penguin_sample_size)),
       random_penguins['body_mass_g'],
       color = plt.cm.Pastel2(np.linspace(0, 1, 10)))

# specify the ticks, labels and title
ax.set_xticks(list(range(penguin_sample_size)))
ax.set_xlabel('Penguin Number')
ax.set_ylabel('Body Mass (g)')
ax.set_title('Penguins Masses')


# #### Cycle the colourmap

# In[19]:


# create a variable
plt.rcParams["axes.prop_cycle"] = plt.cycler('color', plt.cm.Paired(np.linspace(0, 4, 10)))

# create an empty plot
fig, ax = plt.subplots()

# specify the size of the plot
fig.set_size_inches(8, 8)

# create variables
penguins = penguins.sort_values('bill_length_mm')
male_penguins = penguins[penguins['sex'] == 'MALE']
adelie = male_penguins[male_penguins['species'] == 'Adelie']
gentoo = male_penguins[male_penguins['species'] == 'Gentoo']
chinstrap = male_penguins[male_penguins['species'] == 'Chinstrap']

# create plot
ax.plot(adelie['bill_length_mm'], adelie['flipper_length_mm'], label = 'Adelie')
ax.plot(gentoo['bill_length_mm'], gentoo['flipper_length_mm'], label = 'Gentoo')
ax.plot(chinstrap['bill_length_mm'], chinstrap['flipper_length_mm'], label = 'Chinstrap')

# add labels, legend, title, etc.
ax.legend()
ax.set_xlabel('Bill Length (mm)')
ax.set_ylabel('Flipper Length (mm)')
ax.set_title('Penguin Bill vs Flipper Length (Male)')


# ### Customising styles, colours, titles and labels

# ### Labels, ticks and tick labels for axes

# In[2]:


# import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# create an empty plot
fig, ax = plt.subplots()

# create variables
x = np.linspace(0, 10, 101)
y = np.exp(x)

# create plot
ax.plot(x, y)


# In[3]:


# set labels and title
ax.set_xlabel('Time Elapsed (minutes)')
ax.set_ylabel('Count')
ax.set_title('Bacteria Growth')

# view plot
fig


# #### Adjusting ticks

# In[4]:


# add ticks to x-axis
ax.set_xticks([0, 5, 10])
ax.set_xticks([1, 2, 3, 4, 6, 7, 8, 9], minor = True)

# view figure
fig


# #### Customising labels

# In[5]:


# add tick labels to x-axis
ax.set_xticklabels(['0.0', '5.0', '10.0'])

# view figure
fig


# In[6]:


# add tick labels to x-axis
ax.set_xticklabels(['1', '2', '3', '4', '6', '7', '8', '9'], minor = True)

# view figure
fig


# #### Generate legends

# In[7]:


# create new variables
y_no_food = np.exp(x)
y_food = np.exp(x + 1.01)

# create an empty plot
fig, ax = plt.subplots()

# plot the new variables and add the label to the legend
lines = ax.plot(x, y_no_food)
line = lines[0]

# set the line variable
line.set_label('No Food')

# add legend
ax.legend()


# #### Adjusting legends

# In[8]:


# plot second line
ax.plot(x, y_food, label = 'With Food')

# create legend
ax.legend()

# specify legend positioin
ax.legend(loc = 'center left')

# view figure
fig


# ### Changing plot style and colours with Seaborn

# In[9]:


# import matplotlib, seaborn, and pandas libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# read the CSV file
penguins = pd.read_csv("penguins.csv")

# view the DataFrame
print(penguins.shape)
print(penguins.dtypes)
print(penguins.columns)
penguins.head()


# #### Adjust figure size

# In[10]:


# set figure size
sns.set(rc = {'figure.figsize': (5, 5)})

# set the tick style
sns.set_style('ticks')

# set colour style
sns.set_style('darkgrid')

# plot scatterplot
sns.scatterplot(x = 'bill_length_mm', y = 'flipper_length_mm',
               data = penguins, hue = 'species')


# #### Customise individual attributes

# In[11]:


# set style of ticks
sns.set_style('ticks', {'axes.facecolor': '#dddddd',
                       'axes.spines.top': False,
                       'axes.spines.right': False})

# create scatterplot
sns.scatterplot(x = 'bill_length_mm', y = 'flipper_length_mm',
               data = penguins, hue = 'species')


# #### Change colour of a data series in Seaborn

# In[13]:


# set the style first
sns.set_style('ticks')

# specify Pastel palette in scatterplot
sns.scatterplot(x = 'bill_length_mm', y = 'flipper_length_mm',
               data = penguins, hue = 'species',
               palette = 'pastel')


# In[14]:


# set the style first
sns.set_style('ticks')

# specify Pastel palette in scatterplot
sns.scatterplot(x = 'bill_length_mm', y = 'flipper_length_mm',
               data = penguins, hue = 'species',
               palette = 'colorblind')


# #### Customise labels in Seaborn

# In[15]:


# plot the scatterplot
ax = sns.scatterplot(x = 'bill_length_mm', y = 'flipper_length_mm',
               data = penguins, hue = 'species',
               palette = 'colorblind')

# specify the labels
ax.set_xlabel('Bill length (mm)')
ax.set_ylabel('Flipper length (mm)')
ax.set_title('Penguin Bill vs Flipper Length')


# ### Highlighting and adding annotations

# #### Scatterplot

# In[24]:


# import libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# read file
fitness = pd.read_csv("daily_activity.csv")

# view DataFrame
fitness.shape

# create a variable to define the data
single_day = fitness[fitness['ActivityDate'] == '4/12/2016']

# create a scatterplot
sns.scatterplot(x = 'TotalSteps', y = 'Calories', data = single_day)

# create a copy of original data
single_day_highlights = single_day.copy()

# set a criteria as true or false
single_day_highlights['High Activity'] = single_day_highlights['TotalSteps'] > 15000

# create new scatterplot
sns.scatterplot(x = 'TotalSteps', y = 'Calories', hue = 'High Activity',
               data = single_day_highlights)


# #### Lineplot

# In[26]:


# create a time series
steps_time_series = fitness .groupby('ActivityDate')[['TotalSteps']] .sum() .reset_index() .copy()

# create variable
steps_time_series['ActivityDate'] = pd.to_datetime(steps_time_series['ActivityDate'])

# create a lineplot
sns.lineplot(x = 'ActivityDate', y = 'TotalSteps', data = steps_time_series)

# add annotation lines
plt.axhline(y = 250000, color = 'r', linestyle = '--')
plt.axhline(y = 260000, color = 'r', linestyle = '--')


# #### Barplots

# In[32]:


# import libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# read file
flights = pd.read_csv("flights.csv")

# view DataFrame
flights.shape

# create an empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

# create variable
august_flights = flights[flights['month'] == 'August']

# create barplot
bars = ax.bar(august_flights['year'], august_flights['passengers'], color = 'lightgrey')

# annotate a bar
ax.set_xticks(list(range(1949, 1961, 1)))
bars[1].set_color('red')
bars[3].set_color('yellow')
bars[4].set_color('blue')
bars[6].set_color('green')
bars[8].set_color('black')
bars[10].set_color('orange')


# #### Comparing groups: Lineplots and barplots

# ##### Lineplots

# In[42]:


# create an empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

# create a lineplot
for year in flights['year'].unique():
    flights_for_year = flights[flights['year'] == year]
    line_color = '#4472C4' if year == 1955 or year == 1958 else '#7F7F7F'
    ax.plot(flights_for_year['month'], flights_for_year['passengers'],
           color = line_color)


# ##### Barplots

# In[43]:


# create empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

# create variable
august_flights = flights[flights['month'] == 'August']

# create barplot
bars = ax.bar(august_flights['year'], august_flights['passengers'],
              color = 'lightgrey')

# annotate bars
bars[4].set_color('blue')
bars[7].set_color('blue')


# ### Placing annotations

# In[44]:


# plot a simple line
fig, ax = plt.subplots()
ax.plot([4, 3, 2, 1, 0])


# In[53]:


# set the annotation origin
data_ann = ax.annotate('Data 2, 2', xy = (2, 2))

pixel_ann = ax.annotate('Pixels 2, 2', xy = (2, 2), xycoords = 'axes pixels')

fig


# In[54]:


# fixing the text alighment
data_ann.remove()
pixel_ann.remove()
centered_ann = ax.annotate('Centered Data 2, 2',
                          xy = (2, 2), horizontalalignment = 'center',
                          verticalalignment = 'center')

fig


# In[55]:


# add arrows to the plot
centered_ann.remove()

ax.annotate('Look at point 1, 3', xy = (1, 3),
           xytext = (1, 1.5),
           arrowprops = {'facecolor': 'black', 'shrink': 0.05},
           horizontalalignment = 'center', verticalalignment = 'top')

fig


# #### Barplot

# In[57]:


# import libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# read file
flights = pd.read_csv("flights.csv")

# view DataFrame
flights.shape

# create empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(12, 8)

# create variable
august_flights = flights[flights["month"] == "August"]

# create barplot
bars = ax.bar(august_flights["year"], august_flights["passengers"],
              color="lightgrey")

# annotate bars
bars[4].set_color("blue")
bars[7].set_color("blue")


# In[71]:


# set ticks
ax.set_xticks(list(range(1949, 1961, 1)))

# insert labels
ax.set_title('Air Tracel For August')
ax.set_xlabel('Year')
ax.set_ylabel('Passengers')

# select bars to highlight
for bar_index in [4, 7]:
    bars[bar_index].set_color('#4472C4')
    row = august_flights.iloc[bar_index]
    passenger_count = row['passengers']
    year = row['year']
    xy = (year, passenger_count)
    
    # draw a circle on top of bar
    if bar_index == 7:
        bbox = {'boxstyle': 'circle, pad = 0.5', 'fill': False, 'edgecolor': 'black'}
    else:
        bbox = None
        
# create plot
ax.annotate('{}'.format(passenger_count),
           xy = xy,
           verticalalignment = 'bottom',
           horizontalalignment = 'center',
           bbox = bbox)

fig


# In[70]:


# draw a perfectly sized circle
xy = (year, passenger_count - 10)
ax.annotate(" ",
           xy = xy,
           verticalalignment = 'bottom',
           horizontalalignment = 'center',
           bbox = {'boxstyle': 'circle, pad = 3', 'fill': False, 'edgecolor': 'black'})

fig


# ### Preparing high-quality visualisations for sharing

# #### Print and pixel

# In[73]:


# setting the resolution

# import libraries
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(dpi = 150)

fig.set_size_inches(6, 4)


# In[74]:


fig, ax = plt.subplots(dpi=100)

fig.set_size_inches(8, 6)


# In[75]:


fig, ax = plt.subplots(dpi=5)

fig.set_size_inches(120, 80)


# #### Saving visualisation

# In[76]:


fig.savefig("my_plot.png")

fig.savefig("my_plot.jpg")


# In[77]:


fig.savefig("my_plot_print.png", dpi=300)

fig.savefig("my_plot_web.png", dpi=72)


# In[ ]:





# # 

# ## 4.3 Visualisation workflow

# ### Exploring the data set

# In[78]:


# Import matplotlib, Seaborn, NumPy and Pandas libraries.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import datetime

# Read the CSV file.
marathon = pd.read_csv("marathon_results.csv")

# View the DataFrame.
print(marathon.shape)
print(marathon.columns)
marathon.head()


# #### Q1: What is the spread of the data?

# In[79]:


# Ensure the variables of interest are numeric
marathon['official_time'] = pd.to_timedelta(marathon['Official Time'])

# how many seconds
marathon['official_time_seconds'] = marathon['official_time'].dt.seconds

# how many minutes
marathon['official_time_minutes'] = marathon['official_time_seconds'] / 60

# view the DataFrame
marathon.head()


# In[80]:


# create an empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(16, 8)

# create a histogram
ax.hist(marathon['Official Time'], bins = 20)


# #### Q2: What is the spread of males?

# In[81]:


# create an empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(16, 8)

# create variable for x values
male = marathon[marathon['M/F'] == 'M']

# create histogram
ax.hist(male['Official Time'], bins = 20)


# #### Q3: What is the spread of females?

# In[82]:


# create an empty plot and set plot size
fig, ax = plt.subplots()
fig.set_size_inches(16, 8)

# create variable for x values
female = marathon[marathon['M/F'] == 'F']

# create histogram
ax.hist(female['Official Time'], bins = 20)


# #### Q4: How does gender influence race times?

# In[83]:


# create a data set for males and females to use in the matplotlib boxplot
males = marathon[marathon['M/F'] == 'M']

females = marathon[marathon['M/F'] == 'F']

males = males['official_time_minutes']

females = females['official_time_minutes']

plt.boxplot([males, females], labels = ['M', 'F'], patch_artist = True)

plt.show()


# #### Conclusion (with Seaborn)

# In[84]:


# seaborn boxplot
sns.boxplot(x = 'M/F', y = 'official_time_minutes', data = marathon)


# ### Making effective visualisations

# #### Enhancing histograms

# In[85]:


# create a histogram
sns.histplot(x = 'official_time_minutes', data = marathon, hue = 'M/F', bins = 20)

# add legend
plt.legend(loc = 'upper right', title = 'Gender', labels = ['Female', 'Male'])

# view plot
plt.show()


# In[ ]:




