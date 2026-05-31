#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


data = {
    "name" : ["Sumit" , "Shivam" , "Shivang" , "Shiva"],
    "age" : [21 , 13 , 12 , 15],
    "city" : ["Bengaluru" , "Mumbai" , "Pune" , "Hydrabad"]
}


# In[ ]:


df = pd.DataFrame(data)
df


# In[ ]:


data_2 = [
    {"name":"Sumit" , "age":21 , "city":"Bengaluru"},
    {"name":"Shivam" , "age":13 , "city":"Mumbai"},
    {"name":"Shivang" , "age":12 , "city":"Pune"},
    {"name":"Shiva" , "age":15 , "city":"Hydrabad"}
]

df_2 = pd.DataFrame(data_2)
df_2


# ### Accessing the value

# In[ ]:


print("Name Column")
print(df['name'] , "\n")

print("City Column")
print(df.age , "\n")

print("2nd index of City Column")
print(df.city[2] , "\n")


# In[ ]:


print(df.loc[0],"\n")
print(df.loc[0:1],"\n")

print(df.iloc[2],"\n")
print(df.iloc[2:4],"\n")

