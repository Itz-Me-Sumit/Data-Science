#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

s1 = pd.Series([10,20,30,40,50])
print(s1)


# In[ ]:


s2 = pd.Series([10,20,30,40,50] , index=['a','b','c','d','e'] , name = "Scores")
print(s2)


# In[ ]:


import numpy as np
np_array = np.array([10,20,30,40,50])
s3 = pd.Series(np_array)
print(s3)

