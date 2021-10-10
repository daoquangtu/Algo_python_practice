#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Use for loop with index
list_text = input('Your list is:')
list_text = list_text.split(',')
list_num = [int(i) for i in list_text]
max = 0
for i in range(1,len(list_num)):
    if list_num[max] < list_num[i]:
        max = i
        
list_num.remove(list_num[max])

max = 0
for i in range(1,len(list_num)):
    if list_num[max] < list_num[i]:
        max = i

print(list_num[max])


# In[19]:


list_text = input('Your list is:')
list_text = list_text.split(',')
list_num = [int(i) for i in list_text]
print(list_num)

maximum = max(list_num)
print(maximum)


# In[24]:


nums = [2,1,3,4]
nums.remove(max(nums))
second_largest = max(nums)
print(second_largest)


# In[ ]:




