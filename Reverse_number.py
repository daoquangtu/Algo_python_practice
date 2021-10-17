#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def reverse_number(num):
    reverse = 0
    while(num) > 0:
        last_digit = num%10
        reverse = reverse * 10 + last_digit
        num = num//10
    return reverse

n = int(input('Your number is:'))
result = reverse_number(n)
print(result)

