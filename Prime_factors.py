#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prime_factors(num):
    list_result = []
    so_bi_chia = 2
    while num > 2:
        if (num % so_bi_chia == 0):
            list_result.append(so_bi_chia)
            num = num/so_bi_chia
        else:
            so_bi_chia += 1
    return list_result

num = int(input('Your number is:'))
result = prime_factors(num)
print(result)    

