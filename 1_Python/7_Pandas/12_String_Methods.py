#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from data import Data
obj = Data()
df = obj.data()
df.head()


# In[ ]:


df["Name"].str.find("Mr").head()


# In[ ]:


count = df["Name"].str.contains("Mrs").sum()
print(count)


# In[ ]:


data = {
    "Name":["Sumit" , "Shivam k" , "Shivang" , "Shiva"],
    "Email":["s@gmail.com" , "t@gmail.com" , "m@gmail.com" , "p@gmail.com"]
}

df = pd.DataFrame(data)
df


# In[ ]:


df["Name"].str.replace("k" ,  "Kumar" , regex=False)


# In[ ]:


df["Name"].str.pad(width=10 , side="left" , fillchar="-")

