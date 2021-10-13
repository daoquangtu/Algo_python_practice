#!/usr/bin/env python
# coding: utf-8

# In[3]:


money = float(input('The amount of money you want to borrow:'))
interst_rate = float(input('The interest is:'))
term = float(input('The term (year) is:'))

interest = (money*interst_rate/100)*term
print('Your interest is:', interest)


# In[ ]:




