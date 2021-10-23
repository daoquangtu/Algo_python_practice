#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bank:
    def __init__(self):
        self.balance = 1000
        self.minimum = 100
    
    def with_draw(self, amount):
        if amount < self.minimum:
            print('Your money that needs to withdraw is too small!!')
        elif amount > self.balance:
            print('Your withdraw money is greater than the balance')
        else:
            self.balance = self.balance - amount
            return amount
    
    def get_balance(self):
        return self.balance

my_bank = Bank()
my_bank.with_draw(1250)
result = my_bank.get_balance()
print('Your balance is: ', result)


# In[ ]:





# In[ ]:




