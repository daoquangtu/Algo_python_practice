#!/usr/bin/env python
# coding: utf-8

# In[7]:


def is_prime(num): 
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def all_prime(num):
    list_result = []
    for n in range(2,num+1):
        if is_prime(n) is True:
            list_result.append(n)
    return list_result

num = int(input('Your number is:'))
primes = all_prime(num)
print(primes)


# In[5]:


print(num)


# In[6]:


print(type(num))


# In[ ]:




