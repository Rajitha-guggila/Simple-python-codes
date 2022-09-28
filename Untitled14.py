#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Python3 program to add two numbers

num1 = 15
num2 = 12

sum = num1 + num2

# printing values
print(sum)


# In[4]:


num1=int(input())
num2=int(input())
c=num1+num2
print(c)


# In[7]:


# Python3 program to add two numbers

number1 = str("First number: ")
number2 = str("\nSecond number: ")

sum = number1 + number2

print(sum)


# In[10]:


a=5
b=6
maximum=min(a,b)
print(maximum)


# In[2]:


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


# In[1]:


a = 2
b = 4
  
maximum = max(a, b)

print(maximum)


# In[ ]:




