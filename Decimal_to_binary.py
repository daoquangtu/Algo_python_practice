#!/usr/bin/env python
# coding: utf-8

# In[2]:


def deci_to_bina(n):
    if n > 1:
        deci_to_bina(n//2)
    print(n%2, end = '')

num = int(input("Your decimal number is:"))
deci_to_bina(num)
print('')


# In[ ]:




