#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sum_amstrong_number(n):
    total = 0
    number_len = len(n)
    for i in n:
        total = total + pow(int(i),number_len)
    return total

#Input your number:
n = input('Your number is:')

#Calculate sum of amstrong number
total_amstrong_number = sum_amstrong_number(n)
print(total_amstrong_number)

#Check the input number is an Amstrong number or not
if total_amstrong_number == int(n):
    print('Your number is an Amstrong number')
else:
    print('Your number is not an Amstrong number')


# In[ ]:




