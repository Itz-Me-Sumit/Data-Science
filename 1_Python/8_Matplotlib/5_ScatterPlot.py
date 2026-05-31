#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt 
import pandas as pd
from data import Data
import random

obj=Data()
clean_data=obj.get_clean_data()


# In[ ]:


clean_data


# In[ ]:


sample_df = clean_data.sample(1000 , random_state=1)


# In[ ]:


plt.figure(figsize=(8,6))
plt.scatter(sample_df["Quantity"] , sample_df["Revenue"] , alpha=0.5 , color="red")

plt.title("Quantity Vs Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue")

plt.style.use("ggplot")

plt.grid(True)
plt.show()


# In[ ]:


# Monthly Revenue Vs Monthly Qunatity

monthly_revenue = clean_data.groupby("Month")["Revenue"].sum()
monthly_quantity = clean_data.groupby("Month")["Quantity"].sum()

plt.figure(figsize=(7,5))
plt.scatter(monthly_revenue.values , monthly_quantity.values , alpha=0.6 , color="red")

plt.title("Monthly Revenue Vs Quantity")
plt.xlabel("Monthly Revenue")
plt.ylabel("Monthly Revenue")

plt.grid(True)
plt.style.use("ggplot")


# ### Subplots : Multiple Charts in one figure

# In[ ]:


fig , axs = plt.subplots(nrows=1 , ncols=2 , figsize=(20,10) , sharex=True)

axs[0].plot(monthly_revenue.index , monthly_revenue.values , marker='o' , color='blue' , label="revenue")
axs[0].set_title("Monthly Revenue")

axs[1].plot(monthly_quantity.index , monthly_quantity.values , marker='o' , color='red' , label='quantity')
axs[1].set_title("Monthly Quantity")

for ax in axs:
    ax.tick_params(axis='x', rotation=45)


# In[ ]:


plt.figure(figsize=(12,8))

plt.plot(monthly_revenue.index , monthly_revenue.values , marker='o' , color='blue' , label="revenue")

plt.plot(monthly_quantity.index , monthly_quantity.values , marker='o' , color='red' , label='quantity')

plt.xticks(rotation=45)
plt.title("Monthly Revenue vs Quantity")
plt.xlabel("Month")
plt.ylabel("Values")

plt.legend()
plt.grid(True)
plt.show()

