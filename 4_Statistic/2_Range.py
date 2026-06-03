#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy import stats


# In[ ]:


data = [1,2,3,4,5,6,7,8,9,10]


# In[ ]:


q1_lower = np.percentile(data , 25 , method="lower")
q3_lower = np.percentile(data , 75 , method="lower")


# In[ ]:


print(q1_lower,q3_lower)


# In[ ]:


IQR_lower = q3_lower-q1_lower
print(IQR_lower)


# In[ ]:


q1_linear = np.percentile(data , 25 , method="linear")
q3_linear = np.percentile(data , 75 , method="linear")


# In[ ]:


IQR_linear = q3_linear-q1_linear
print(IQR_linear)

