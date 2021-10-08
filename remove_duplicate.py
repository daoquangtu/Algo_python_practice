#!/usr/bin/env python
# coding: utf-8

# In[16]:


def remove_duplicate(text):
    unique = []
    for check in text:
        if check not in unique:
            unique.append(check)
    return unique


# In[17]:


test = [1,2,3,4,5,6,7,8,8,9]
print(remove_duplicate(test))


# In[ ]:




