#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import plotly.express as px


# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data import Data

obj = Data()
df = obj.get_clean_data()


# In[ ]:


sample_df = df.sample(1000 , random_state=1)


# In[ ]:


monthly_revenue = sample_df.groupby("Month")["Revenue"].sum().reset_index()


# In[ ]:


monthly_revenue.head()


# In[ ]:


fig  =  px.line(monthly_revenue,
                x="Month" , y="Revenue",
                title="Monthly Revenue Trend",
                markers=True)

fig.update_layout(xaxis_title="Month" , yaxis_title="Revenue" , xaxis_tickangle=45)

