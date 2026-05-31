#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

titanic_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pd.read_csv(titanic_dataset)
df.head()


# In[ ]:


new_order = ["Name","Sex","Age","Pclass","Fare","Survived"]


# In[ ]:


df_reordered = df[new_order]
df_reordered.head(10)

