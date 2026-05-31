#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# ### Row Wise

# In[ ]:


data = pd.DataFrame({
    'name' : ["Sumit","Shivam","Saket"],
    'age' : [21,13,16],
    'city' : ["Bangaluru" , "Pune" , "Hydrabad"]
})

for index , row in data.iterrows():
    print("Row: ",index)
    print(row['name'] , row['age'] , row['city'] ,'\n')
    print(row,'\n\n')


# In[ ]:


for row in data.itertuples():
    print(row)
    print("Index:",row.Index)
    print(row.name)
    print(row.age)
    print(row.city)
    print()


# ### Column Wise

# In[ ]:


for col in data.columns:
    print("Columns:",col)


# In[ ]:


for col in data.columns:
    print(data[col],'\n')


# In[ ]:


for col in data.columns:
    print(data[col].values,'\n')

