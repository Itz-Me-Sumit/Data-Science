#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from data import Data

obj = Data()
df = obj.get_data()
clean_data = obj.get_clean_data()


# In[ ]:


clean_data


# In[ ]:


monthly_revenue = obj.monthly_revenue()


# In[ ]:


filtered = clean_data[clean_data['Revenue']>500]
country_revenue = filtered.groupby("Country")["Revenue"].sum()
filtered


# In[ ]:


plt.style.use("ggplot")
plt.figure(figsize=(12,6))
plt.bar(country_revenue.index , country_revenue.values ,  color="pink")

plt.xlabel("Revenue")
plt.ylabel("Country")
plt.title("Revenue per year")

plt.grid(True)

