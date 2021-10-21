#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import random
first = input('Enter your first name: ')
last = input('Enter your last name: ')
num = int(input('Enter your password length: '))
all_chars = string.ascii_letters + string.digits + string.punctuation
email = first + last + '@gmail.com'
password = ''
for char in range(num):
    rand_char = random.choice(all_chars)
    password = password + rand_char

print('Your gmail ID: ' + email)
print('Your password: ' + password)


# In[ ]:




