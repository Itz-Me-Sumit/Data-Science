#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = {
    'a':10,
    'b':20,
    'c':30,
    'd':40,
    'e':50
}

s1 = pd.Series(data)
print(s1)


# In[ ]:


print(s1.index)
print(s1.values)
print(s1.shape)


# #### Slicing and Indexing
# 

# In[ ]:


# if i want index 0
print(s1['a'])


# ### native and positional Indexing

# In[ ]:


# native Indexing
print(s1.loc['b'])
print(s1.loc[['a','b']])

# positional Indexing
print(s1.iloc[2])
print(s1.iloc[[1,2]])



# ### Slicing

# In[ ]:


# native slicing
print(s1.loc['a':'d'])  # final index is inclusive

# positional slicing
print(s1.iloc[1:2])  # final index is exclusive

