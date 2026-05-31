#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
titanic_dataset = "https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv"

df = pd.read_csv(titanic_dataset)
df


# ### Indexing

# In[ ]:


df.loc[4]


# In[ ]:


df.loc[4:9 , ["Name" , "Age"]]


# ### Slicing Rows

# In[ ]:


df.loc[0:4]


# ### Slicing Columns

# In[ ]:


df.loc[ : , ["Name" , "Age"]]


# In[ ]:


df.iloc[:,[2,4]] # it'll return column at 2th and 4th index


# In[ ]:


df.iloc[ : , 2:5 ] # will give column from 2nd to 4th index , final index is exclusive


# In[ ]:


subset=df[df["Sex"]=="male"].copy().reset_index(drop=True)
subset


# ### set_index

# In[ ]:


df_with_NameIndex = df.set_index("Name")
df_with_NameIndex


# ### Reseting Index -> For Rows

# In[ ]:


jan_sales = pd.DataFrame(
    {"sales" : [200,300,400]},
    index = ["Store_A" , "Store_B" , "Store_C"],
)
jan_sales


# In[ ]:


feb_sales = pd.DataFrame(
    {"sales" : [240 , 303]},
    index = ["Store_A" , "Store_C"]
)
feb_sales


# In[ ]:


common_index = jan_sales.index
common_index


# In[ ]:


feb_sales_aligned = feb_sales.reindex(common_index)


# In[ ]:


feb_sales_aligned


# In[ ]:


feb_sales_aligned = feb_sales.reindex(common_index , fill_value=0)


# In[ ]:


feb_sales_aligned


# In[ ]:


jan_sales["sales"] - feb_sales_aligned["sales"]


# ### Reindexing For Columns

# In[ ]:


source_a = pd.DataFrame({
    "Products" : ["Laptop", "Tablet" , "Phone"],
    "Price" : [50000 , 40000 , 30000],
    "Stock" : [20 , 14 , 30]
})
source_a


# In[ ]:


source_b = pd.DataFrame({
    "Products" : ["Laptop" , "Tablet" , "Phone"],
    "Battery" : [5 , 8 , 25]
})
source_b


# In[ ]:


source_a_column = source_a.columns
source_a_column


# In[ ]:


source_b_aligned = source_b.reindex(columns = source_a_column , fill_value = 0)
source_b_aligned


# In[ ]:


all_columns = source_a.columns.union(source_b.columns)

source_b_a_columns = source_b.reindex(columns = all_columns , fill_value = 0)
source_b_a_columns

