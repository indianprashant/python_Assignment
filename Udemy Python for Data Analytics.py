#!/usr/bin/env python
# coding: utf-8

# # Python Programming language

# In[2]:


## Variable in python

age= 20
name="Prashant"
height=6.1
is_student=True

## Print the variable

print("age:",age)
print("name:",name)
print("height:",height)


## Case sensitivity
name="prashant"
Name="kumar"

name==Name

age=20
print(type(age))

## Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))


# In[9]:


age=20
int(age)


# In[10]:


print(type(int(age)))


# In[11]:


height=5.11
type(height)


# In[12]:


## Convert float to int

height=2.11
int(height)


# In[13]:


## Convert int to float

height=55
float(height)


# In[15]:


var=11
print(var,type(var))

var="Prashant"
print(var,type(var))

var=3.12
print(var,type(var))


# In[17]:


age=int(input("what is the age"))
print(type(age))


# In[18]:


## Simple calculator

num1=float(input("Enter your first number"))
num2=float(input("Enput your second number"))


sum= num1 + num2
difference= num1 - num2
multi= num1 * num2
division= num1 / num2

print("Sum:",sum)
print("Difference:",difference)
print("Multi:",multi)
print("Division:",division)

# In[19]:


## Arthematics operations

a=10
b=5

add_result = a + b ## Addition
sub_result = a - b ## Substraction
mul_result = a * b  ## Multiplication
div_result = a / b  ## Division
floor_result = a // b ## Flooring
modulus_result = a % b  ## Modulues
exponent_result = a ** b

print(add_result)
print(sub_result)
print(mul_result)
print(div_result)
print(floor_result)
print(modulus_result)
print(exponent_result)


# In[26]:


str1 = "prashant"
str2 = "Prashant"

str1==str2


# In[31]:


str1 = "prashant"
str2 = "Prashant"

str1!=str2


# In[28]:


## Not equal to symbol !

str_name = "Prashant"
str_name1 = "Prashant"

str_name == str_name1


# In[29]:


num1 = 42
num2 = 40

## Greater than >
num1>num2


# In[30]:


## Less than <
num1<num2


# In[33]:


##  Simple calculator

number1= float(input("Enput here number"))
number2= float(input("Enput here second number"))

addition = number1 + number2
substraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2
floor_divison = number1 // number2
modulus = number1 % number2
exponentiation = number1 ** number2

## performing arthemathecial operators
print("Addition:",addition)
print("Substraction:",substraction)
print("Multiplication:",multiplication)
print("Division:",division)
print("Floor_divison:",floor_divison)
print("Modulus:",modulus)
print("Exponentiation:",exponentiation)


# # Assignment question answer

# # **Question 1:** Write a Python program to print "Hello, World!".

# In[35]:


print("Hello, World!")


# # **Question 2:** Write a Python program that takes a user input and prints it.

# In[36]:


user_input= input("Put input value")
print("User_input:",user_input)


# # **Question 3:** Write a Python program to check if a number is positive, negative, or zero.
# 

# In[40]:


number=float(input("Enter the number"))
if number>0:
    print("This number is positive.")
elif number<0:
    print("This number is negative.")
else :
    print("This number is zero")


# # **Question 4:** Write a Python program to find the largest of three numbers.
# 

# In[42]:


num1=float(input("Enter your first number."))
num2=float(input("Enput your seccond number."))
num3=float(input("Enput your third number."))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else :
    largest = num3
print("the largest number is")


# # **Question 5:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.
# 

# In[46]:


integer_var=10
float_var=10.1
string_var="Hello"
boolean_var=True

## Print data type
print(type(integer_var))
print(type(float_var))
print(type(string_var))
print(type(boolean_var))

## print the value
print(integer_var)
print(float_var)
print(string_var)
print(boolean_var)


# # Practice By Prashant

# In[47]:


x = True
y = False

result = x and y
print(result)


# In[48]:


x = True
y = True

result = x and y
print(result)


# In[49]:


x = True
y = False

result = x or y
print(result)


# In[50]:


x = True 
y = True

result = x or y
print(result)


# # If Statement

# In[9]:


age = 20

if age>=18:
    print("you are allowed to voat in the election ")


# In[10]:


age>=18


# In[12]:


num=int(input("Enter the number"))

if num<0:
    if num>0:
        print("Allow to visit")
    else :
        print("no more time to visite")
    print("Not money")
else :
    print("Age is not define")


# In[13]:


## else
## The else statement executes a block of code if the condition in the if statement is False.

age=16

if age>=18:
    print("you are eligilable for voating")
else :
    print("you are a minor")


# In[15]:


## elif
## The elif statement allows you to check multiple conditions. It stands for "else if"

age=17

if age<13:
    print("you are a child")
elif age<19:
    print("you are a teenage")
else :
    print("you are an adult")


# In[20]:


## Nested Condiitonal Statements

# You can place one or more if, elif, or else statements inside another if, elif, or else statement to create nested conditional statements.

## number even ,odd,negative

number=int(input("enter the number"))

if number>0:
    print("the number is positive")
    if number%2==0:
        print("the number is even")
    else:
        print("the number is odd")
else:
    print("the number is negative and zero")
        


# In[23]:


num=int(input("Any number will be odd"))

if num>0:
    print("this number is positive ")
    if num%3==0:
        print("this number is odd")
    else:
        print("no any number is even")
else:
    print("Number is not given")


# In[24]:


## Practical Examples

## Determine if a year is a leap year using nested condition statement

year=int(input("Enter the year"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
    else:
        print(year,"is a leap year")
else:
    print(year,"is not a leap year")


# In[28]:


## Assignment
## Simple Calculator program
# Take user input

num1=float(input("Enter the number"))
num2=float(input("enter the second number"))
operation= input("input operation(+,-,*,/):")

# Perform the requested operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = " Error ! divided by zero"
else:
    result = "invalid error"
    
print("result:"),result
    


# In[3]:


### Determine the ticket price based on age and whether the person is a student.
# Ticket pricing based on age and student status

## Take user input
age = int(input("Enter your age"))
is_student = input("Are you a student ? (Yes/No):").lower()

## Determine ticket price

if age < 5:
    price = "free"
elif age <= 12:
    price = "$10"
elif age <= 17:
    if is_student == "Yes":
        price = "$12"
    else:
        price = "$15"
elif age <=64:
    if is_student == "Yes":
        price = "$18"
    else:
        price = "$25"
else:
    price = "$20"
    
print("Ticket price :",price)


# # Complex Example 3: Employee Bonus Calculation
# 
# Calculate an employee's bonus based on their performance rating and years of service.

# In[5]:


## Take user input
year_of_service = int(input("Enter year of service"))
performance_rating = float(input("Enter performance rating (1.0 to 5.0):"))

## Determine bonus 

if performance_rating >= 4.5:
    if year_of_service > 10:
        bonus_percentage = 20
    elif year_of_service > 5:
        bonus_percentage = 15
    else :
        bonus_percentage = 10
elif performance_rating >= 3.5:
    if year_of_service > 10:
        bonus_percentage = 15
    elif year_of_service > 5:
        bonus_percentage = 10
    else:
        bonus_percentage = 15
else :
    bonus_percentage = 0
    
    
## Calculate bonus 
salary = float(input("Enter your bonus"))
bonus_amount = salary * bonus_percentage / 100
print("Bonus Amount: ${:.2f}".format(bonus_amount))
        


# # Complex Example 4: User Login System
# A simple user login system that checks the username and password.

# In[7]:


## User login system

## predefine username and password
stored_username = "admin"
stored_password = "password123"

## take user input

username= input("Enter your name")
password = input("Enter here password")

## Check login

if username == stored_username:
    if password == stored_password:
        print("Login successfull!")
    else:
        print("Incorrect password.")
else:
    print("username not defined.")


# In[ ]:




