#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Smart_device:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def recharge(self):
        print('Eat Electricity :)')
        print('Electrons are Yummy!!')

class Watch(Smart_device):
    def __init__(self,brand,price,has_gps):
        Smart_device.__init__(self,brand,price)
        self.has_gps = has_gps

my_watch = Watch('Fibit',700,False)
my_watch.recharge()

