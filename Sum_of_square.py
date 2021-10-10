#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Prob: Square sum of a random list input:
def square_sum(nums):
    sum_list = []
    for i in nums:
        square_num = i**2
        sum_list.append(square_num)
    
    result = sum(sum_list)
    return result

list_nums = [1,2,3,4,9]
total = square_sum(list_nums)
print('Square sum of your list is:',total)


# In[ ]:


#Prob: Take a number as input. Then get the sum of the numbers. If the numbers is n, then get:
# 0^2 + 1^2 + 2^2 + ..... + n^2
def square_sum (nums):
    sum_of_list = 0
    for i in range(nums+1):
        square_num = i**2
        sum_of_list = sum_of_list + square_num
        
    return sum_of_list

total = square_sum(5)
print('Square sum of your list is:',total)


# In[ ]:





# In[ ]:




