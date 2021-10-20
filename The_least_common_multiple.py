#!/usr/bin/env python
# coding: utf-8

# In[1]:


def check_lcm(num1,num2):
    lcm = max(num1,num2)
    while lcm % num1 != 0 or lcm % num2 != 0:
        lcm += 1
    return lcm

num1 = int(input('Your 1st number is:'))
num2 = int(input('Your 2nd number is:'))
result = check_lcm(num1,num2)
print(result)

