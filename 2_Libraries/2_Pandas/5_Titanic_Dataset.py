#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


titanic_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pd.read_csv(titanic_dataset)
df


# In[ ]:


# first 5 rows
df.head()


# In[ ]:


# last five rows
df.tail()


# In[ ]:


df.Name


# In[ ]:


df[["Name" , "Age"]]


# In[ ]:


df.loc[0]


# In[ ]:


df.loc[0 , "Name"]


# In[ ]:


df.iloc[0]


# In[ ]:


df.iloc[0 , 3] # row 0 and column 3(column 3 contains Name)


# ### Conditional Selection

# In[ ]:


# get all the rows where person age > 70

df[df["Age"]>70]


# In[ ]:


# Get all the females who survived
df[ (df["Sex"]=="female")  & (df["Survived"] == 1) ]


# In[ ]:


# Get only name and age of all the females who survived 

survived_female = df[ (df["Sex"]=="female") & (df["Survived"]==1) ]
name_age = survived_female[["Name" , "Age"]]
name_age


# In[ ]:


name_age.head(10)


# In[ ]:


# Total Number Of survivors

survived = len(df[df["Survived"]==1])
not_survived = len(df[df["Survived"]==0])

# Percentage Survived
print(f"{round( ( survived/(survived+not_survived) )*100 , 2 )} % Survived")

#percentage Not Survived
print(f"{round( ( not_survived/(survived+not_survived) )*100 , 2 )} % Not Survived")


# In[ ]:


# use of loc in DataFrame
# df.loc(DataFrame , index)
df.loc[(df["Sex"]=="female") & (df["Survived"]==1) , ["Name" , "Age"]]


# In[ ]:


df.loc[ : 9 , ["Name" , "Cabin"]]

