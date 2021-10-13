#!/usr/bin/env python
# coding: utf-8

# In[3]:


money = float(input('Số tiền gửi ban đầu là:'))
interest_num = float(input('Lãi hàng năm là:'))
interest_rate = interest_num/100
term = int(input('Số năm vay là:'))    

compound_interest = money*(1+interest_rate)**term
print('Tổng tiền của bạn sau',term,'năm là:',compound_interest)


# In[4]:


def compound_interst(principal,interest_rate,time):
    total_money = principal * (pow((1 + interest_rate / 100), time))
    ci = total_money - principal
    return ci

compound_interst = compound_interst(10000000,8,3)
print('Your interest is:',compound_interst)


# In[ ]:




