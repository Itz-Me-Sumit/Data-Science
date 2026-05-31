#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import Data

obj = Data()
df = obj.get_clean_data()


# In[ ]:


sample_df = df.sample(1000,random_state=1)
sample_df.head()


# In[ ]:


corr_matrix = sample_df[["Quantity" , "UnitPrice" ,"Revenue"]].corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix , annot=True , cmap='coolwarm' , fmt='.2f' , linewidths=0.5)
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

