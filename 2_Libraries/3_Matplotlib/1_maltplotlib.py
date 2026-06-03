#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from data import Data
obj = Data()
df = obj.get_data()


# In[ ]:


df


# In[ ]:


df["InvoiceNo"].str.startswith('C').sum()


# In[ ]:


print(df.shape)
print(df.columns)


# In[ ]:


df.info()


# In[ ]:


df.describe()

