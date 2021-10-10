#!/usr/bin/env python
# coding: utf-8

# In[16]:


# Use for loop with index
list_text = input('Your list is:')
list_text = list_text.split(',')
list_num = [int(i) for i in list_text]
max = 0
for i in range(1,len(list_num)):
    if list_num[max] < list_num[i]:
        max = i

print(list_num[i])


# In[17]:


# Use for loop with number
list_text = input('Your list is:')
list_text = list_text.split(',')
my_nums = [int(i) for i in list_text]

def max_number(nums):
    largest = nums[0]
    for num in nums: #cách này num là 1 số trong list luôn, không phải là index nữa
        if num > largest:
            largest = num
    return largest

largest = max_number(my_nums)
print('The largest number is:', largest)


# In[18]:


#Thử giải với vòng lặp while - không ổn vì không biết số phần tử cần phải loop qua
# Dùng while thì trong trường hợp này, phải dùng index
def max_number(nums):
    largest = nums[0]
    num = 0
    while num <= nums: #cách này num là 1 số trong list luôn, không phải là index nữa
        if num > largest:
            largest = num
    return largest
my_num = [1,2,3,4,5,6]
largest = max_number(my_num)
print('The largest number is:', largest)


# In[28]:


# Dùng while thì trong trường hợp này, phải dùng index
list_text = input('Your list is:')
list_text = list_text.split(',')
my_nums = [int(i) for i in list_text]

def max_number(nums):
    i = 1
    max = 0
    while i < len(nums):
        if nums[max] < nums[i]:
            max = i
        i += 1
    return nums[max]
        
largest = max_number(my_nums)
print('The largest number is:', largest)

