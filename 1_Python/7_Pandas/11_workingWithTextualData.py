#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from data import Data
obj = Data()
df=obj.data()


# In[ ]:


df[["Name" , "Sex" , "Cabin"]].head(10)


# In[ ]:


df["Name"].str.upper()


# In[ ]:


df["Name"] = df["Name"].str.capitalize()
df


# In[ ]:


df["Name"] = df["Name"].str.replace("mr" , "sir")
df.head()


# In[ ]:


df["Name"] = df["Name"].replace({
    r"\bMrs\b": "ma'am",
    r"\bMr\b": "sir"
}, regex=True)
df

