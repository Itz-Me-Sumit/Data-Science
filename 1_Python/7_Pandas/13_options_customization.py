#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from data import Data
obj = Data()
df = obj.data()


# In[ ]:


pd.set_option("display.max_rows" , 4)
df


# In[ ]:


pd.set_option("display.max_columns" , None)
df


# In[ ]:


pd.set_option("display.max_columns",4)
df

