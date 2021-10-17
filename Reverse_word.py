#!/usr/bin/env python
# coding: utf-8

# In[12]:


def reverse_word(sentence):
    text_split = sentence.split()
    text_split.reverse()
    return ' '.join(text_split)

sentence = input('Your sentence is:')
result = reverse_word(sentence)
print(result)


# In[ ]:




