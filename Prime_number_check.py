#!/usr/bin/env python
# coding: utf-8

# In[10]:


def check_prime_number(num):
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return False
    return True

num = int(input('Your number is:'))
result = check_prime_number(num)
if result:
    print('Your number is a prime')
else:
    print('Your number is not a prime')

