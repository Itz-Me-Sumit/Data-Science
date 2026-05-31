#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    a = 5
    b = int(input("Enter Number: "))
    print(a/b)
except ZeroDivisionError:
    print("You cant' divide by Zero")



# In[ ]:


try:
    for i in range(5):
        a = int(input("Enter Number: "))
        print(a)
except ValueError as VE:
    print("Enter Integer Only")


# In[ ]:


for i in range(5):
    try:
        a = int(input("Enter Number: "))
        print(a)
    except ValueError:
        print("Enter Integer Only")

