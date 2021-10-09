#!/usr/bin/env python
# coding: utf-8

# In[6]:


def fibonacci_series(number):
    fibonacci_sublist = [0,1]
    i = 2
    while i <= number:
        next_number = fibonacci_sublist[i-1] + fibonacci_sublist[i-2]
        fibonacci_sublist.append(next_number)
        i += 1
    return fibonacci_sublist


# In[7]:


print(fibonacci_series(9))


# In[ ]:




