#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
print('To stop anytime, enter: q')
score = 0
while True:
    num = random.randint(0,10)
    guess = input('Guess a number between 0 and 10:')
    if guess == 'q':
        print('Game over')
        break
    guess_num = int(guess)
    if guess_num is num:
        print('You guessed it correctly')
        score =+ 10
        print('Your new score is:',score)
    else:
        print('You guessed did not match')
        print('The number was',num)

