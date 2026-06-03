#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy import stats


# In[ ]:


data = [20,14,43,2,135,56,3,4,83,5]


# In[ ]:


print(stats.tmean(data))


# In[ ]:


print(stats.mode(data))


# In[ ]:


print(stats.tmedian(data))

