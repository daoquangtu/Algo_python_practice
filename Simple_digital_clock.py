#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
print('Simple clock made by Tu:\n')
hour = int(input('Type in the current hour:'))
minute = int(input('Type in the current minute:'))
second = int(input('Type in the current second:'))

def display():
    print(hour, ':', minute, ':', second)

def add():
    global hour
    global minute
    global second
    
    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

print('\n')
while True:
    time.sleep(1)
    add()
    display()
    


# In[ ]:


import time
while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\n", end="", flush=True)
  time.sleep(1)


# In[ ]:


import time
while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result, flush = True)
    time.sleep(1)
    if result == '12:24:15 PM':
        print('Đi ngủ nào bé Quyên ^^')
        break

