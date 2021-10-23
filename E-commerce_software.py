#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Shopping:
    def __init__(self):
        self.cart = []
        self.total = 0
    
    def add_to_cart(self,item,price):
        self.cart.append(item)
        self.total = self.total+price
    
    def check_out(self, amount):
        if amount < self.total:
            extra_money = self.total - amount
            print('You need to pay extra money! Your extra money is:', extra_money)
        elif amount > self.total:
            back_money =  amount - self.total
            print('Your back money is:',back_money)
            print('You got',self.cart)
            print('Thanks for wasting your money ahihi')
            self.total = 0
            self.cart = []
        else:
            print('You got',self.cart)
            print('Thanks for wasting your money ahihi')
            self.total = 0
            self.cart = []
            
my_cart = Shopping()
my_cart.add_to_cart('T-Shirt', 30)
my_cart.add_to_cart('Shoes', 90)
result = my_cart.check_out(100)


# In[ ]:




