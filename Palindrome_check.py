#!/usr/bin/env python
# coding: utf-8

# In[6]:


def reverse_text(text):
    if len(text) == 0:
        return text
    else:
        return text[-1] + reverse_text(text[ :-1])

text = input('Your text is:')
reverse_text_result = reverse_text(text)

def Palindrome_check(reverse_text_result):
    if reverse_text_result == text:
        return print('Your text is Palindrome')
    else:
        return print('Your text is not Palindrome')

Palindrome_result = Palindrome_check(reverse_text_result)


# In[ ]:




