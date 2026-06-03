#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


titanic_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pd.read_csv(titanic_dataset)
df


# ### sort by values

# In[ ]:


sorted_by_Age = df.sort_values(by="Age" , ascending=False)
sorted_by_Age.head(10)


# In[ ]:


sortedBy_Pclass_Fare = df.sort_values(by=["Pclass" , "Fare"] , ascending = [True , False]).copy()
sortedBy_Pclass_Fare.head()


# ### sort by index

# In[ ]:


passengerIndexedData = df.set_index("PassengerId")
passengerIndexedData.sort_index(ascending=True , inplace=True)
passengerIndexedData


# ### Sorting Columns Alphabatically

# In[ ]:


sortedDataByColumn = df.sort_index(axis=1)
sortedDataByColumn

