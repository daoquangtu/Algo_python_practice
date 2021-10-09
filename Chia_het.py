#!/usr/bin/env python
# coding: utf-8

# In[1]:


def print_number(a):
    i = 0
    result = []
    while i < a:
        if i % 3 == 0 and i % 5 == 0:
            result.append(i)
        i += 1
    print(result)


# In[2]:


print(print_number(25))


# In[ ]:


def print_number(num):
    result = []
    for i in range(num):
        if i%3 == 0 and i%5 == 0:
            result.append(i)
    return result
num = int(input('Day so cua ban la:'))
result = print_number(num)
print(result)

