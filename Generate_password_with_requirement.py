#!/usr/bin/env python
# coding: utf-8

# In[3]:


import string
import random

def random_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
    
    for i in range(size-4):
        password += random.choice(all_chars)
    return password

pass_len = int(input('Your password length is: '))
print('Your password is:', random_password(pass_len))


# In[ ]:




