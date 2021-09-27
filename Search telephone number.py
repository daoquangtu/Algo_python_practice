#!/usr/bin/env python
# coding: utf-8

# In[40]:


tel_number = [8438233938, 8438233939, 8438525977, 84948529796]
contact_name = ["U", "Nhà cũ", "Dũng", "Hĩm"]


# In[41]:


def search(number):
    lo = 0
    hi = len(tel_number) - 1
    while lo <= hi:
        mid = (lo + hi)//2
        if tel_number[mid] < number:
            lo = mid + 1
        elif tel_number[mid] > number:
            hi = mid + 1
        elif tel_number[mid] == number:
            print(tel_number[mid])
            print(contact_name[mid])
            break
    
    


    


# In[42]:


search(8438525977)


# In[ ]:




