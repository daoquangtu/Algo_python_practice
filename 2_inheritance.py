#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Athlete:
    def __init__(self,sport):
        self.sport = sport
    def get_sport(self):
        print(self.sport)

Ronaldo = Athlete('Soccer')
Ronaldo.get_sport()

class Student:
    def __init__(self,name,Id):
        self.name = name
        self.Id = Id
    def getId(self):
        print(self.Id)

class Person(Athlete,Student):
    def __init__(self,sport,name,Id):
        Athlete.__init__(self,sport)
        Student.__init__(self,name,Id)
        
Athlete1 = Person('Soccer','7 đĩ','07')
print(Athlete1.sport)
print(Athlete1.name)
print(Athlete1.getId())

