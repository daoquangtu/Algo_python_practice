#!/usr/bin/env python
# coding: utf-8

# In[4]:


def reverse_text(text):
    reverse = ''
    for i in text:
        reverse = i + reverse
    return reverse

text = input('Your text is:')
result = reverse_text(text)
print(result)


# In[ ]:




