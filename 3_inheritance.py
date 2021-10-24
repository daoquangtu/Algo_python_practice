#!/usr/bin/env python
# coding: utf-8

# In[1]:


class A:
    def call_me(self):
        print('I am A')
class B(A):
    def call_me(self):
        print('I am B')
        A.call_me(self) #name of class.name of function in the class. (parameter)
class C(B):
    def call_me(self):
        print('I am C')
        B.call_me(self)

caller = C()
caller.call_me()


# In[ ]:




