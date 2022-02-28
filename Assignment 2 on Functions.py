#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Create a function to find out number is even or odd

def even_odd(number):
    if number%2==0:
        print(number, "is even")
    else:
        print(number, "is odd")


# In[5]:


even_odd(14)


# In[6]:


#Create a function to find if number is even
def if_even(number):
    if number%2==0:
        return True
    else:
        return False


# In[7]:


if_even(8)


# In[9]:


#Create a function to find if number is prime or not
def if_prime(number):
    dummy = 0
    for i in range(2,number):
        if number%i==0:
            dummy = dummy + 1
    if dummy>0:
        print("Not Prime")
    else:
        print("Prime")


# In[13]:


if_prime(37)


# In[1]:


#Create a function to Combine two strings
def combine_str(str1, str2):
    return str1+str2


# In[2]:


combine_str("hello","world")


# In[11]:


#Create a function to accept a list and return only odd values as a list
def ret_odd(list1):
    list2 = list()
    for i in list1:
        if i%2!=0:
            list2.append(i)
        else:
            continue
    return list2


# In[12]:


ret_odd([23, 12, 45, 31,90, 10])


# In[9]:


#Create a function to check if string has vowel in it
def if_vowel(str1):
    vowels = 'aeiouAEIOU'
    for i in str1:
        if i in vowels:
            return True


# In[10]:


if_vowel("coffee")


# In[ ]:




