#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Smart_device:
    def recharge(self):
        print('Eat Electricity :)')
        print('Electrons are Yummy!!')

class Phone(Smart_device):
    video_call = True
    def __init__(self,brand,price,network):
        self.brand = brand
        self.price = price
        self.network = network

my_phone = Phone('Apple',700,'Vinaphone')
my_phone.recharge()


# In[ ]:




