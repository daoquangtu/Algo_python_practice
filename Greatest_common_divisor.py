#!/usr/bin/env python
# coding: utf-8

# In[3]:


list1=[]
list2=[]
list3=[]
def check_gcd(num1,num2):
    for i in range(1,num1+1):
        if num1 % i == 0:
            list1.append(i)
    for j in range(1,num2+2):
        if num2 % j == 0:
            list2.append(j)
    for k in list1:
        if k in list2:
            list3.append(k)
    return max(list3)

num1 = int(input('Your first number is:'))
num2 = int(input('Your second number is:'))
result = check_gcd(num1,num2)
print('The greatest common divisor between', num1, 'and', num2,'is:',result)


# In[4]:


def gcd(num1,num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2,num1%num2)
num1 = int(input('Your first number is:'))
num2 = int(input('Your second number is:'))
result = gcd(num1,num2)
print('The greatest common divisor between', num1, 'and', num2,'is:',result)


# In[ ]:




