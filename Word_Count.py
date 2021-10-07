#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Input text:
text = input("Text what you want (50 words maximum):")

#To count the word in text, we will count space appeard in the text. 
count = 0
for space in text:
    if space == ' ':
        count = count + 1
        
#Add 1 for the last word
count = count + 1

if count > 50: 
    print("Your text has more than 50 words")
else:
    print(count)


# In[ ]:




