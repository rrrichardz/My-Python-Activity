#!/usr/bin/env python
# coding: utf-8

# ### Peer Review 1.3.8 - Li Chen Zhou

# In[2]:


# Program To Make Simple Calculator
# This function adds 2numbers
def add( x, y ):
    return x + y
# wrong use of white space


#This function subtracts  2numbers
def subtract(x, y):
    return x - y
# extra spacing not needed, only 2 is needed



       #This function multipliers 2numbers
def multiply(x, y):
   return x * y
# incorrect indentation & use of comments mark '#'


##This function divides  2numbers #
def divide(x, y):
   return x / y
# incorreect use of indentation and comments mark '#'

# comments excess 76 characters
# excessive spaces below
# incorrect use of blank space between lines
# incorrect indentation (which will cause errors)
# incorrect spelling & capitalisation of characters
print ( "Select operation.")
print ( "1.Add")
print ( "2.Subtract")
print ( "3.Multiply")
print ( "4.Divide")

while True:
   
   choice = input  ("Enter choice(1/2/3/4): ")# Take input from the  user
    
    
   # Check if choice is 1 of the four options by completing the following code in the IDE of your choice or noteboolk
   if choice in ('1', '2', '3', '4'):
      Num1   = float(input("Enter first number: "))
      Num2   = float(input("Enter second number: "))

       if CHOICE == '1':
           print(Num1, "+", Num2, "=", add( Num1, Num2 ))

       elif CHOICE == '2':
           print (Num1, "-", Num2, "=", subtract( Num1, Num2 ))

       elif CHOICE == '3':
           print (Num1, "*", Num2, "=", multiply( Num1, Num2 ))

       elif CHOICE == '4':
           print (Num1, "/", Num2, "=", divide( Num1, Num2 ))
       break
   else:

       Print( "Invalid Input" )#this prints the invalid input....
        
# users should follow PEP 8 guildlines or at least know the basic or most
# important ones, and then to practice and get in a good habit.


# ### Cleaned version

# In[ ]:


# Program To Make Simple Calculator
# This function adds 2numbers
def add(x, y):
    return x + y


#This function subtracts  2numbers
def subtract(x, y):
    return x - y


#This function multipliers 2numbers
def multiply(x, y):
    return x * y


print ( "Select operation.")
print ( "1.Add")
print ( "2.Subtract")
print ( "3.Multiply")
print ( "4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4):")# Take input from the  user
    
    
# Check if choice is 1 of the four options by completing the following code
# in the IDE of your choice or notebook
    if choice in ('1', '2', '3', '4'):
        Num1 = float(input("Enter first number:"))
        Num2 = float(input("Enter second number:"))

    if CHOICE == '1':
        print(Num1, "+", Num2, "=", add(Num1, Num2))

    elif CHOICE == '2':
        print(Num1, "-", Num2, "=", subtract(Num1, Num2))

    elif CHOICE == '3':
        print(Num1, "*", Num2, "=", multiply(Num1, Num2))

    elif CHOICE == '4':
        print(Num1, "/", Num2, "=", divide(Num1, Num2))
        break
    
    else:
        print("Invalid Input")#this prints the invalid input....


# In[ ]:




