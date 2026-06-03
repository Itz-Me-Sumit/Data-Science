#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.DataFrame({
    "event":["concert" , "conference" , "wedding"],
    "date":['2025-01-01' , '2025-03-15' , '2025-07-20']
})


# In[ ]:


df["pandas_date"] =pd.to_datetime(df["date"])


# In[ ]:


df.head()


# In[ ]:


print(df.dtypes[["event","date","pandas_date"]])


# In[ ]:


df["pandas_date"].dt.year


# In[ ]:


df["pandas_date"].dt.month


# In[ ]:


df["pandas_date"].dt.day


# In[ ]:


df["pandas_date"].dt.weekday


# In[ ]:


pd.date_range(start='2024-01-01' , end='2024-01-01' , freq='D')


# In[ ]:


pd.date_range(start='2024-01-01' , end='2024-01-01' , freq='ME') # ME => Month Start


# In[ ]:


pd.date_range(start='2024-01-01' , end='2024-01-01' , freq='MS') # ME => Month End

