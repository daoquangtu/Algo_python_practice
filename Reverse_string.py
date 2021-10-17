#!/usr/bin/env python
# coding: utf-8

# In[3]:


def reverse_text(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + reverse_text(text[:-1])

text = input('Your text is:')
result = reverse_text(text)
print(result)


# In[ ]:




