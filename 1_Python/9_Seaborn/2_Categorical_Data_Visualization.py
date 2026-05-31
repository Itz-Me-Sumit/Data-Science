#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from data import Data

obj = Data()
df = obj.get_data()
clean_data = obj.get_clean_data()


# In[ ]:


clean_data.head()


# In[ ]:


clean_data.info()


# In[ ]:


top_country = clean_data.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)


# In[ ]:


top_country.index


# In[ ]:


plt.figure(figsize=(12,8))
sns.barplot(x=top_country.values , y=top_country.index, hue=top_country.index ,palette='viridis')
plt.title("Top 10 Compnies By Revenue")
plt.xlabel("Total Revenue")
plt.ylabel("Countries")
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.barplot(x=top_country.index , y=top_country.values, hue=top_country.index ,palette='viridis')
plt.title("Top 10 Compnies By Revenue")
plt.xlabel("Countries")
plt.ylabel("Total Revenue")
plt.show()


# In[ ]:


df_sample = clean_data.sample(1000 , random_state=1)


# In[ ]:


df_sample['Country'].value_counts().index


# In[ ]:


plt.figure(figsize=(12,8))
sns.countplot(data = df_sample , x='Country' , order=df_sample['Country'].value_counts().index)
plt.xticks(rotation=45)


# In[ ]:


top_country = clean_data["Country"].value_counts().head(5).index.tolist()
top_country


# In[ ]:


df_top = clean_data[clean_data["Country"].isin(top_country)].copy()
grouped = df_top.groupby(["Country","Month"])["Revenue"].sum().reset_index()
grouped.head()


# In[ ]:





# In[ ]:


grouped["Month"] = pd.to_datetime(grouped["Month"])
grouped = grouped.sort_values('Month')
grouped['Month'] = grouped["Month"].dt.strftime('%Y-%m')


# In[ ]:


# Grouped BarPlot Using Seaborn

plt.figure(figsize=(12,6))
sns.barplot(data=grouped , x='Month' , y="Revenue" , hue="Country")
plt.title('Monthly Revenue By Country (Grouped)')
plt.xlabel('Month')
plt.ylabel("Revenue")
plt.tight_layout()
plt.legend(title="Country")
plt.show()

