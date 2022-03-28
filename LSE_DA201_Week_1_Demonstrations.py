#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator 
# 
# # DA201:  Data Analytics with Python

# ## Week 1: Introduction to Python programming!

# The focus this week is on introducing, setting up, and exploring Python. You will use this notebook to follow along with the demonstrations throughout the week. If you are using Jupyter Notebook for the first time refer to the documentation to leran about the interface and how best to use your notebook. 
# 
# Learn about using you Jupyter Notebook here: https://jupyter-notebook.readthedocs.io/en/latest/ui_components.html
# 
# This is your notebook. Use it to follow along with the demonstrations, test ideas and explore what is possible. The hands-on experience of writing your own code will accelarate your learning!

# ### 1.1 Python for data analysis 

# There are no Jupyter Notebook demonstrations in this section.

# 

# ### 1.2 Basics of Python programming

# #Starting first exercise following 1.2.1

# In[1]:


# integer vs float data types
value_a = 1299
value_b = 10.29

print(type(value_a))
print(type(value_b))


# In[4]:


# string data type
a = "This is a string value"
b = 'This is a string with single quotes'

print(type(a))
print(type(b))


# In[5]:


# boolean data type
a = True
b = False

print(type(a))
print(type(b))


# In[8]:


# Create a variable
n = 300

# view the variable with the print() function
print(n)


# In[9]:


# create three variables
var_a = 100
var_b = 100.5
name = "Soni"
print(var_a, var_b, name)


# In[10]:


# print a single variable
print(var_a)
print(var_b)
print(name)


# In[11]:


# assign same value to multiple variables
a = b = c = 50 

print(a)
print(b)
print(c)
print(a, b, c)


# In[12]:


# assign multiple values to multiple variables
a, b, c = 50, 50, 50 

print(a)
print(b)
print(c)
print(a, b, c)

# stipulate a single value (common error!)
a, b, c = 50

print(a, b, c)


# In[13]:


# multiple variables with different values and data types
a, b, c = 5, 50.25, "Python"

print(a, b, c)
print(a)
print(b)
print(c)


# In[14]:


# view the list of keywords
import keyword

print(keyword.kwlist)


# In[16]:


# question 1
jedi = warrior = saviour = "Luke Skywalker"

print(jedi)
print(warrior)
print(saviour)
print(jedi, warrior, saviour)


# In[17]:


# question 2
a = b = c = "Darth Vader"

print(a)
print(b)
print(c)
print(a, b, c)


# In[18]:


# demonstrating the 'and' operator
a = 15
b = 20

if a > 10 and b > 15:
    print('a and b satisfies the above statements.')


# In[19]:


# demonstrating the 'and' operator
a = 15
b = 20

if a > 10 and b > 20 :
    print('a and b satisfies the above statements.')
    
else :
    print('This line is printed as b is not greater than 20.')


# In[20]:


# demonstrating the 'or' operator
a = 10
b = -20

if a > 0 or b > 0:
    print("Either number is greater than 0.")
    
else:
    print("No number is greater than 0.")


# In[21]:


# demonstrating the 'not' operator
x = 10

if not (x > 10):
    print('Yes')
else:
    print('No')


# ### Functions

# In[3]:


# define a function to welcome new members to the program
# no arguments in the parenthesis, include the colon
def new_member():
    # the function code statement
   print('Hello and welcome to the programme') 

# call the function
new_member() 


# In[7]:


# trying out a function myself
def programme_complete():
    print('Congratulations for finishing the programme')
    
programme_complete()


# In[8]:


# define an output variable
output = new_member()
# check if the function returns a value
output is None


# In[9]:


# assign the function output to a variable
# function must return explicitly
def new_member(): 
    return 'Hello and welcome to the program'

# define an output variable
output = new_member()
# check if the function returns a value
output is None


# In[10]:


# example using f-string interpolation
def new_member(name): 
    return f'Hello and welcome to the program, {name}!' # notice the 'f'

# the print function allows you to easily preview the output
print(new_member('Sarah'))


# In[13]:


# example using f-string interpolation
def new_member(name): 
# alternative line for the previous example
    return 'Hello and welcome to the program,'' '+ name + '!'

# the print function allows you to easily preview the output
print(new_member('Sarah'))


# In[14]:


# example of adding two positional arguments
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d
add_optional_bonus(5, 6)


# In[15]:


# example of adding two positional arguments and a keyword argument
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d
add_optional_bonus(5, 6, c=5) # include the keyword c


# In[16]:


# example of adding two positional arguments and a keyword argument out of sequence
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d
add_optional_bonus(5, 6, d=6) # including the keyword d


# In[17]:


# example of adding two positional arguments and multiple keyword arguments
def add_optional_bonus(a, b, c=0, d=0):
    return a + b + c + d
add_optional_bonus(5, 6, d=6, c=5) # including both d and c (out of sequence)


# Positional arguments need to be in front of keyword arguments

# In[34]:


# returning multiple values
def membership_number(x):
    a = x + 1
    b = x + 2
    c = x + 3
    return a, b, c

x, y, z = membership_number(5) # to show the membership numbers
print(x, y, z) 


# In[35]:


# using the * for a variable argument
def workout_time(*reported):
    total_minutes = sum(reported) 
    if total_minutes < 60:
        return f'Total weekly workout time is {total_minutes} minutes.'
    else: 
        return f'Total weekly workout time is {total_minutes/60} hours.' 

# the function passes any number of minutes
print(workout_time(10, 10, 20))

# the function passes any number of minutes
print(workout_time(60, 60, 20, 40))


# ### Troubleshooting errors

# In[38]:


# example of missing colon at the end of the 'if' statement
x =  10
if x< 10


# In[39]:


# example of zero division error
marks = 50

# perform division with 0
a = marks / 0

print(a)


# In[40]:


# example of indentation error
a = 50
if a>0:

print('True')


# In[41]:


# example of index error
list_1=(1,2,3,4,5,6)
        
list_1[10] # Trying to access element present at index position 10.


# In[42]:


# example of ModuleNotFoundError
import Pluto_planet


# In[43]:


# example of KeyError 
dict_1={'name':"John", '2': "Age", 'Amount':200} # a dictionary with 3 key pairs
dict_1['4']


# In[44]:


# here we try to import the cube function from the math library, 
# which is a readily available library in Python.
# example of import error
from math import cube


# In[45]:


# example of performing an operation that makes no sense
100 + 'John'


# In[46]:


# example of adding an integer to a list
list_a = [1,2,3,4,5]
list_a += 1


# In[47]:


# example of assigning values to the wrong type
int("John")


# In[48]:


# example of a name error
# first we declare variable list_1
list_1 = [1,2,3,4,5]

# now we try to access list_2 which is not defined
print(list_2)


# ### Python data structures: Lists

# In[49]:


# example of creating a list
# notice the square brackets
new_list = ['Python', 'Java', 'Ruby'] 

print(new_list)


# In[50]:


# list can also store different data types such as strings, integers and float
# notice the square brackets
list_2 = ['cat', 12, 15.2]

print(list_2)


# In[51]:


# example of a list with duplicates
list_a = ['apple', 'banana', 5, 2, 5, 10.2, 8, 10.2, 'banana', 'apple']

print(list_a)


# In[52]:


# example of a list with duplicate items
list_a = ['apple', 'banana', 5, 2, 10.2, 8.3, ['apple', 'banana', 5, 2, 10.2, 8.3]]

print(list_a)


# ### Counting items in a list

# In[53]:


# example of the len() function
# start with a list 
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", 
           "Saturn", "Uranus", "Neptune"]

# measure the length of the list
len(planets)


# ### Adding items to a list

# In[54]:


# example of the append() method
# add new item at the end of the list
planets.append("Pluto")

print(planets)
print(len(planets))


# In[55]:


# example of the insert() method
# here "1" is the index position
# note: index position in Python starts at 0.
planets.insert(1, "Pluto")

print(planets)
print(len(planets))


# In[56]:


# example of the extend() method
# create a second list
pluto = ["Pluto"]

# second list is appended to starting list
planets.extend(pluto) 

print(planets)
print(len(planets))


# ### Removing items from a list

# In[57]:


# example of the remove() method
# remove the first instance of an item from the list
planets.remove("Pluto") 

print(planets)
print(len(planets))


# In[58]:


# example of the remove() method
# remove the first instance of an item from the list
planets.remove("Maro") 

print(planets)
print(len(planets))


# In[59]:


# example of the pop() method
# remove an item at a specific index position from the list
# note: index position in Python starts at 0, Pluto is planet number 9, thus index 8
planets.pop(8) 

print(planets)
print(len(planets))


# In[60]:


# example of the pop() method
# no index specified
planets.pop() 

print(planets)
print(len(planets))


# ### Joining two lists (concatenate)

# In[61]:


# create 2 lists
fruit_1 = ['apple', 'strawberry', 'pear', 'raspberry']
fruit_2 = ['apricot', 'peach', 'fig', 'plum']

# join the two lists with the + operator
fruit = fruit_1 + fruit_2

print(fruit)
print(len(fruit))


# In[62]:


# create a list
veg = ['carrot', 'lettuce', 'spinach', 'pumpkin']

# add another list with the extend operator
# notice the square brackets
veg.extend(['onion', 'cabbage', 'broccoli', 'asparagus'])

print(veg)
print(len(veg))


# In[63]:


# create a list
colour = ['red', 'yellow', 'orange', 'pink']

# add another list with the append
# notice the square brackets
colour.append(['blue', 'green', 'black', 'purple'])

print(colour)
print(len(colour))

# .append() method only adds a single item to the list


# ### Sorting lists

# In[64]:


# example of the sort() method
# the default is to sort in ascending order
veg.sort() 

print(veg)
print(len(veg))


# In[65]:


# example of the sort() method
# to sort in descending order reverse is true
veg.sort(reverse = True) 

print(veg)
print(len(veg))


# ### Slicing

# In[66]:


# example of selecting a range of elements
# slicing with index position is inclusive of start index position
# slicing with index position is exclusive of the stop index position
# in the example 2:6 the elements from index position 2 to 5 are included
# notice we are not using the print() function

veg[2:6] 


# In[67]:


# example of selecting a range of elements and changing default parameters
# note: index position in Python starts at 0
# list name[start index : stop index : step size]

veg[1:7:2]


# In[68]:


# example of selecting a range of elements and changing default step parameter
# the syntax is: list name[start index : stop index : step size]
# notice the empty values in the first two spaces? This will use the defaults.

veg[::2]


# In[69]:


# example of using a negative index
# pass -2 to reverse the list

veg[::-2]


# ### Python data structures: Tuples

# In[70]:


# create a tuple
tuple_1 = ("Python", "Java", "Ruby")

# print tuple and count length
print(tuple_1)


# In[71]:


# example of a list with different data types
tuple_a = ('apple', 'banana', 5, 2, 10.2, 8.3)

print(tuple_a)


# In[72]:


# example of a list with duplicate items
tuple_b = ('apple', 'banana', 5, 2, 10.2, 8.3,
           'apple', 'banana', 5, 2, 10.2, 8.3)

print(tuple_b)


# In[73]:


# example of a nested tupple 
tuple_c = ('apple', 'banana', 5, 2, 10.2, 8.3,
           ('apple', 'banana', 5, 2, 10.2, 8.3))

print(tuple_c)


# ### Methods of a tuple

# In[74]:


# example of the len() function
# start with a tuple 
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", 
           "Saturn", "Uranus", "Neptune")

# measure the length of the tuple
len(planets)


# In[75]:


# example of the tuple() constructor 
# notice the round brackets 
tup_1 = tuple(["Venus", 1, "Mars"]) 

tup_1


# ### Accessing tuple items

# In[78]:


# example of indexing
# note: index position in Python starts at 0
# locate item at index position 1
tuple_1[2]

print(tuple_1[2])


# In[79]:


# example of nesting tuples within tuples
nested_tup = (1, 2, 3, (4, 5, 6))

# print the length of the nested tuple
print(len(nested_tup))

# this will show item at index position 1
print(nested_tup[1])

# this will show item at index position 3
print(nested_tup[3])


# ### Combining tuples

# In[80]:


# example of using the + operator
tuple_d = planets + tuple_1

# this will show the concatenated tuple
print(tuple_d)
print(len(tuple_d))


# In[81]:


# example of using the * operator
# this will make three copies of the tuple
nested_tup * 3


# ### Max and Min functions (Tuples)

# In[82]:


# example of using max() and min()
a = (1, 13, 44, 23)

# this will show the highest value
print(max(a))

# this will show the lowest value
print(min(a))


# ### Tuple unpacking

# In[83]:


# example of assigning values to objects
celestial_objects = ("Earth", "Saturn", "Pluto")

# notice the sequence
planet, gas_giant, dwarf_planet = celestial_objects

# each of these will output the corresponding object from the tuple
print(planet)
print(gas_giant)
print(dwarf_planet)
print(dwarf_planet, gas_giant, planet)


# In[84]:


# example when the number of variables isn't equal
celestial_objects = ("Earth", "Saturn", "Pluto")

# notice two variables, while the tuple contains three objects
# this will result in an error
planet, gas_giant = celestial_objects


# In[85]:


# example of modifying a list within a tuple
tup = (1, 2, 'Pluto', [1, 2, 3])

# identify the index position of the list and make the modification
# appending 4 to the list
tup[3].append(4)

print(tup)
print(len(tup))


# In[86]:


tup_1 = (1, 1.0, 5, 5.1, 6.8)

print(tup_1)
print(len(tup_1))
print(min(tup_1))
print(max(tup_1))
print(tup_1[0])
print(tup_1[2])


# ### Dictionaries

# In[87]:


# example of the dictionary data structure
# notice how each key has a value joined by :
# notice the curly brackets
dict_1 = {"key1":"Name",
          "key2":"Age",
          "key3": 1964} 

print(dict_1)


# ### Methods of a dictionary

# In[88]:


# change the value of key 2
dict_1['key2'] = "new_value"

print(dict_1)


# In[91]:


# add a new key value pair
dict_1['key4'] = "address"

print(dict_1)


# In[92]:


# example of changing and replacing values in a dictionary
dict_1['key4'] = ["48 Mainstreet"]

print(dict_1)


# In[96]:


dict_1['key1'] = 'Richard'
dict_1['key2'] = '25'
dict_1['key3'] = '1997'
dict_1['key4'] = ['23 Arlington Green']

print(dict_1)


# ### Deleting the entry from a dictionary

# In[97]:


# example of deleting an entry from a dictionary
# delete an entry
del dict_1["key1"]

print(dict_1)


# In[98]:


# example of deleting an entry from a dictionary using the pop() method
# delete key 3
dict_1.pop("key3")

print(dict_1)


# ### Key and value iterators

# In[101]:


dict_2 = {"key1":"Name", "key2":"Initials", "key3":"Age", "key4":"Occupation", "key5":"Address"}
# show keys only
print(dict_2.keys())

# show values only
print(dict_2.values())


# ### Creating a dictionary from sequence

# In[102]:


# example of creating a dictionary from a sequence
key_list = ['key1', 'key2', 'key3', 'key4', 'key5']
value_list = ['Apple', 'Fruit', 'Red', 'Juicy', 'Firm']

# view keys
print(key_list)

# view values
print(value_list)

# Creating new dictionary 
dict_3 = dict(zip(key_list, value_list))

# view dictionary
print(dict_3)


# In[104]:


key_list = ['key1', 'key2', 'key3', 'key4', 'key5']
value_tuple = ('Apple', 'Fruit', 'Red', 'Juicy', 'Firm')

print(key_list)

print(value_tuple)

dict_3 = dict(zip(key_list, value_tuple))

print(dict_3)


# ### Sets

# In[105]:


# example of a set
set1 = set([1, 2, 3, 4, 4, 2])

# view the set
print(set1)

# view the data type
print(type(set1))


# In[106]:


# example of a set
set2 = {5, 6, 7, 7, 6, 5}

# view the set
print(set2)

# view the data type
print(type(set2))


# ### Methods of a set

# In[107]:


# example of adding an item to a set
# use the .add() method
set1.add("cake")

# view the set
print(set1)

# view the data type
print(type(set1))


# In[108]:


# example of adding an item to a set
# use the .update() method
set1.update(set2)

# view the set
print(set1)

# view the data type
print(type(set1))


# In[109]:


# example of the union() method
# create two new sets
set3 = {"apple", "banana", "cherry"}
set4 = {"google", "microsoft", "apple"}

# syntax : set.union(set1, set2...)
set5 = set1.union(set3, set4)

# view the set
print(set5)

# view the data type
print(type(set5))


# In[110]:


# example of the intersection() method
# use the intersection() method
# syntax : set.intersection(set1, set2 ... etc)
z = set3.intersection(set4)

# view the set
print(z)

# view the data type
print(type(z))


# In[111]:


# example of the intersection() method
# use the intersection() method
# syntax : set.intersection(set1, set2 ... etc)
z = set1.intersection(set2)

# view the set
print(z)

# view the data type
print(type(z))


# In[112]:


# example of the .difference() method
# syntax : set.difference(set)
x = set4.difference(set3)

# view the set
print(x)

# view the data type
print(type(x))


# In[113]:


# example of the symmetric_difference() method
# syntax : set.symmetric_difference(set)
a = set1.symmetric_difference(set2)

# view the set
print(a)

# view the data type
print(type(a))


# In[114]:


# example of the symmetric_difference() method
# syntax : set.symmetric_difference(set)
a = set3.symmetric_difference(set4)

# view the set
print(a)

# view the data type
print(type(a))


# In[116]:


# find the intersection
fruit = {'apple', 'pear', 'watermelon', 'tomato'}
vegetables = {'carrot', 'tomato', 'parsnip', 'leek'}

print(fruit.intersection(vegetables))


# In[119]:


# Question 1:
# add beetroot to vegetables with add()
vegetables.add('beetroot')
# view set vegetable
print(vegetables)

# Question 2:
# combine two sets with union()#
# name the variable edible_plants
edible_plants = vegetables.union(fruit)
# view the vegetables set
print(edible_plants)

# Question 3:
# identify the vegetables in the edible_plants set
# use .difference()
print(edible_plants.difference(fruit))


# ### Control Flow Expressions (structures)

# ### The if statement

# In[126]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a > b:
# note the indention
# view the output as a string
    print("a is greater than b")


# In[127]:


# create two variables
a = 2
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a > b:
   # note the indention
   # view the output as a string
    print("a is greater than b")


# ### The elif statement

# In[130]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a < b:
    # note the indention
    # view the output as a string
    print("a is smaller than b")
# use the elif statement
# specify the test expression as a < b
# note the colon (:)
elif a > b:
    # note the indention
    # view the output as a string
    print("a is greater than b")


# In[131]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a > b:
    # note the indention
    # view the output as a string
    print("a is smaller than b")
# use the elif statement
# specify the test expression as a < b
# note the colon (:)
elif a < b:
    # note the indention
    # view the output as a string
    print("a is greater than b")


# ### The else statement

# In[132]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a == b:
    # note the indention
    # view the output as a string
    print("a is equal to b")
# use the elif statement
# specify the test expression as a < b
# note the colon (:)
elif a == b:
    # note the indention
    # view the output as a string
    print("a is equal to b")
# use the else statement
# note the colon (:)    
else:
    # note the indention
    # view the output as a string
    print("a is not equal to b")


# In[133]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a > b:
    # note the indention
    # view the output as a string
    print("a is bigger than b")
# use the elif statement
# specify the test expression as a < b
# note the colon (:)
elif a == b:
    # note the indention
    # view the output as a string
    print("a is equal to b")
# use the else statement
# note the colon (:)    
else:
    # note the indention
    # view the output as a string
    print("a is not equal to b")


# In[134]:


# create two variables
a = 20
b = 5

# use the if statement
# specify the test expression as a > b
# note the colon (:)
if a == b:
    # note the indention
    # view the output as a string
    print("a is bigger than b")
# use the elif statement
# specify the test expression as a < b
# note the colon (:)
elif a < b:
    # note the indention
    # view the output as a string
    print("a is equal to b")
# use the else statement
# note the colon (:)    
else:
    # note the indention
    # view the output as a string
    print("a is not equal to b")


# ### Control flow expressions: Loops

# ### 'For' loops

# In[138]:


# Print each item in the list
cities = ['London', 'Paris', 'New York City','Singapore']

# 'item' in this line is an object in the list
for item in cities:
    # view the list
    print(item)


# In[144]:


# Print each item in the string
a = 'Top Cities'

# i is a variable
for i in a: 
    # view the list
    print(i)


# In[145]:


# Print each item in a tuple
tup_a = ('London', 'Paris', 'New York City')
# Print each item inside a tuple
for i in tup_a:
    print(i)


# In[146]:


# Print each item in a tuple
a_dict = {'city': 'London', 'age': 2000, 'population': 8.9} 
# Age given in years and pop. in millions.
for i in a_dict:
    print(i)


# ### 'While' loops

# In[147]:


# create a variable
i = 1
# specify the condition
while i < 9:
    # This is the loop body - the += operator is adding 1 to i.
    i += 1
    # view the output
    print(i)


# In[3]:


# define the variable
count = 0
# specify the condition
while count < 5:
    count = count + 1
    # specify the docstring with f""
    print(f"Count : {count}")
    # view the output
    print("Python is fun!")


# In[8]:


i = 0
a = "aeroplane"
while i < len(a): #the len function returns the length of an object
    if a[i] == 'a' or a[i] == 'n':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1


# In[7]:


i = 0
a = "Gundam"
while i < len(a):
    if a[i] == '' or a[i] == '':
        i += 1
        continue
    print('Current Letter:', a[i])
    i += 1


# In[10]:


# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


# In[14]:


# Exit the loop when 'x' is New York City
cities = ['London', 'Paris', 'New York City','Singapore']
for x in cities:
    print(x)

    if x == 'New York City':
        break


# In[17]:


# Do not stop at New York City
cities = ['London', 'Paris', 'New York City','Singapore', 'Hong Kong', 'Milan', 'Sydney', 'Shenzhen', 'Shanghai', 
          'Dubai', 'Berlin', 'Tokyo']
for x in cities:
    print(x)
    
    if x == "New York City":
        continue
        print(x)


# In[18]:


cities = ['London', 'Paris', 'New York City', 'Singapore']
             
for i in cities:
    pass


# In[28]:


# create a list of five cars
cars = ["Nissan", "Ford", "Toyota", "Fiat", "VW"]

# create a for loop
for i in cars:
    # create a statement
    print(i)
    
    # create an if statement
    if i== 'Toyota':
        # insert a break statement
        break


# ### 1.3 Python libraries and reproducibility of code

# ### 1.3.2 Objects and classes in Python

# In[3]:


class Person:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language
    def introduce(self):
        print(f'Hello my name is {self.name}, I\'m {self.age} years old and I speak {self.language}.')
        
person_object = Person('Richard', '25', 'Chinese')
person_object.introduce()


# In[6]:


class Person:
    def __init__(self, name, age, language, city):
        self.name = name
        self.age = age
        self.language = language
        self.city = city
    def introduce(self):
        print(f'Hello my name is {self.name}, I\'m {self.age} years old, I speak {self.language} and I live in {self.city}.')
        
person_object = Person('Richard', '25', 'Chinese', 'London')
person_object.introduce()

person_object_2 = Person('Paul', '73', 'English', 'London')
person_object_3 = Person('Kira Yamato', '17', 'Japanese', 'P.L.A.N.T.')
person_object_4 = Person('Joseph', '17', 'Chinese', 'Shenzhen')

person_object_2.introduce()
person_object_3.introduce()
person_object_4.introduce()



# ### The hasattr() function

# In[7]:


class Person:
    name = 'Richard'
    age = '25'
    
x = hasattr(Person, 'age')
print(x)


# In[8]:


class Person:
    name = 'Richard'
    
x = hasattr(Person, 'age')
print(x)


# ### The getattr() function

# In[9]:


class Person:
    name = 'Richard'
    age = '25'
    
x = getattr(Person, 'age')
print(x)


# In[11]:


class Person:
    name = 'Richard'
    
x = getattr(Person, 'age')
print(x)


# ### The setattr() function

# In[12]:


class Person:
    name = 'Richard'
    age = '25'
    
setattr(Person, 'age', 35)

x = getattr(Person, 'age')
print(x)


# ### The delattr() function

# In[13]:


class Person:
    name = 'Richard'
    age = '25'
    
delattr(Person, 'age')

x = getattr(Person, 'age')
print(x)


# ### Inheritance

# In[14]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'Hello my name is {self.name} and I\'m {self.age} years old.')

class Student(Person):
    pass

person_object = Student('Richard', '25')
person_object.introduce()


# In[16]:


class Weather:
    def __init__(self, temperature, wind_speed, wind_direction):
        self.temp = temperature
        self.wspeed = wind_speed
        self.wdirec = wind_direction
    def introduce(self):
        print(f'Hello! The weather today is {self.temp}, {self.wspeed} and {self.wdirec}.')
        
person_object = Weather('30 degrees Celsius', '30 km/h', 'SSE')
person_object.introduce()


# ### The DateTime Module

# ### Date class

# In[ ]:


# printing a specific date
import datetime
d = datetime.date(2022, 3, 28)

print(d)
print(type(d))


# ### Date class: specific class

# In[19]:


# import the datetime module and date class
from datetime import date

d = date(2022, 3, 28)
print(d)
print(type(d))


# In[22]:


x = datetime.datetime.now()
print(x)


# ### Date class: daily data

# In[24]:


#printing current year, month and day
from datetime import date
#date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


# In[25]:


#printing current year, month and day
from datetime import date
#date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)


# ### Time class

# In[27]:


# import module
from datetime import time

#Creating a time object
#time(hour, minute, second, microsecond) 
t = time(1, 23, 45, 67890) 

print("time =",t)


# In[32]:


# creating a time object
# time (hour, minute, second, microsecond) 
t = time (6, 45, 25, 234566)

print("hour =", t.hour)
print("minute =", t.minute)
print("second =", t.second)
print("microsecond =", t.microsecond)


# ### DateTime class

# In[36]:


# import module and class
from datetime import datetime

t = datetime(2022, 3, 28, 20, 31, 50, 123456)
print("year =", t.year)
print("month =", t.month)
print("day =", t.day)
print("hour =", t.hour)
print("minute =", t.minute)
print("seconds =", t.second)
print("micro seconds =", t.microsecond)

print("The date and time is =", t)


# ### Timedelta class

# In[37]:


from datetime import datetime, date
# you can import more than one class or object at a time from a module

t1 = datetime(year=2021, month=12, day=15, hour=5, minute=45, second=25)
t2 = datetime(year=2019, month=10, day=28, hour=12, minute=55, second=13)
t3 = t1 - t2
print("time difference =", t3)
print("type of t3 =", type(t3))


# In[38]:


t1 = datetime(year=2021, month=12, day=15, hour= 5, minute=45, second=25)
t2 = datetime(year=2019, month=10, day=28, hour= 12, minute=55, second=13)
t3 = t1 - t2

print("time difference in seconds =", t3.total_seconds())
print("type of t3 =", type(t3))


# ### Formatting dates

# ### strftime()

# In[45]:


# current date and time 
now = datetime.now()
print('Current Time', now)

# Using strftime to only print hours, minutes and seconds 
t = now.strftime("%H:%M:%S")
print("Time with only hours, minutes and seconds", t)

# Changing the separators: 
t1 = now.strftime("%m/%d/%Y")
# mm/dd/YY format
print("Date with / seperators:", t1)


# ### strptime()

# In[46]:


date_string = "30 October 2021"#

print("date_string=", date_string)
print("Data type of date-string -->" , type(date_string))


# In[47]:


#this is the date format
date_object = datetime.strptime(date_string, "%d %B %Y")

print("date_object =", date_object) 
print("Datatype of the date_string after formating with strptime -->",
      type(date_object))


# ### Formatting demonstration

# In[55]:


# import modules and classes
import datetime 
from datetime import datetime, date 
import pytz

local = datetime.now()
print("Local:", local.strftime ("%d/%m/%Y, %H:%M:%S"))

#Here, datetime_NY and datetime_London are datetime objects containing the 
#current date and time of their respective time zones.
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY:", datetime_NY.strftime("%d/%m/%Y, %H:%M:%S"))

tz_London = pytz.timezone('Europe/London') 
datetime_London = datetime.now(tz_London)
print("London:", datetime_London.strftime ("%d/%m/%Y, %H:%M:%S"))


# In[59]:


import this


# In[ ]:





# In[ ]:




