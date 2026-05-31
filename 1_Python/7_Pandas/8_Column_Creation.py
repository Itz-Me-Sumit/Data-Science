#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# ### Custom Based Column Creation based on login

# In[ ]:


data = pd.DataFrame({
    'name' : ["Sumit","Shivam","Saket"],
    'age' : [21,13,16],
    'city' : ["Bangaluru" , "Pune" , "Hydrabad"]
})
data


# In[ ]:


"""
experience = []
for index , row in data.iterrows():
    if row["age"]>18:
        experience.append("young")
    else:
        experience.append("senior")
"""

values=['young' if row["age"]<18 else "senior" for index,row in data.iterrows()]
data['experience'] = values


# In[ ]:


data


# In[ ]:


# Vectorized way
data['experience'] = data['age'].apply(lambda age : 'young' if age<18 else 'senior')


# In[ ]:


data


# In[ ]:


data = pd.DataFrame({
    'name' : ["Sumit","Shivam","Saket"],
    'age' : [21,13,16],
    'city' : ["Bangaluru" , "Pune" , "Hydrabad"]
})
data


# In[ ]:


# kuch to khud se kiya

def filter(age):
    if age<18:
        return "young"
    else:
        return "senior"
data['experience'] = data['age'].apply(filter)
data

