#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from data import Data
obj = Data()
df = obj.data()


# In[ ]:


# Convert a column into category
df["Sex_C"] = df["Sex"].astype("category")
df[["Sex" , "Sex_C"]].head(10)


# In[ ]:


print(df["Sex"].dtype)
print(df["Sex_C"].dtype)


# In[ ]:


df["Sex_C_Category_Code"] = df["Sex_C"].cat.codes


# In[ ]:


df[["Sex" , "Sex_C" , "Sex_C_Category_Code"]].head(10)


# In[ ]:


df["Sex"].apply(lambda x: 1 if x=="female" else 0)
df.insert(5 , "Sex_encode" , df["Sex"].apply(lambda x : 1 if x=="female" else 0))


# In[ ]:


df

