#!/usr/bin/env python
# coding: utf-8

# In[2]:


def check_amstrong(num):
    order = len(str(num))
    
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order 
        temp //= 10
    return num == sum

num = int(input('Enter your number:'))
if check_amstrong(num):
    print(num,'is an Amstrong number')
else:
    print(num,'is not an Amstrong number')


# In[ ]:




