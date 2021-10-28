#!/usr/bin/env python
# coding: utf-8

# In[25]:


import sqlite3
conn = sqlite3.connect('facebook.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM User")

#select all row
user = cursor.fetchall()

#select column by index
for i in user:
    print(i[3])

#caculate total friends
total = 0
for i in user:
    total += i[3]
print(total)

#update and delete
cursor.execute("UPDATE User SET Friends = 500 WHERE Id = 3")
cursor.execute("DELETE FROM User WHERE Id = 3")


conn.commit()
conn.close()


# In[ ]:





# In[ ]:




