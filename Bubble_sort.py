#!/usr/bin/env python
# coding: utf-8

# In[1]:


def bubbleSort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list

num = [64,34,25,12,22,11,90]
sort_num = bubbleSort(num)
print(sort_num)


# In[ ]:




