#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from data import Data
obj = Data()
df = obj.get_data()
clean_data = obj.get_clean_data()


# In[ ]:


clean_data.head()


# In[ ]:


monthly_revenue = clean_data.groupby('Month')["Revenue"].sum().sort_index()
monthly_revenue.head()


# In[ ]:


monthly_revenue.index


# In[ ]:


monthly_revenue.values

