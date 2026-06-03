#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seaborn as sns

import matplotlib.pyplot as plt
from data import Data

obj = Data()
df = obj.get_data()
clean_data = obj.get_clean_data()


# In[ ]:


df_quantity = clean_data[ (clean_data["Quantity"]>0) & (clean_data["Quantity"]<100) ]


# In[ ]:


plt.figure(figsize=(15,6))
sns.histplot(df_quantity['Quantity'] , bins=10 , stat="frequency" , kde=True , color='skyblue')
plt.title("Quantity")
plt.xlabel("Quantity")
plt.show()

