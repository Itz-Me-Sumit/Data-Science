#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from data import Data
obj = Data()
df = obj.get_data()
clean_data = obj.get_clean_data()
monthly_revenue = obj.monthly_revenue()


# In[ ]:


clean_data.head()


# In[ ]:


plt.figure(figsize=(12,6)) # Decide Size of Canvas

plt.plot(monthly_revenue.index , monthly_revenue.values , marker="o") # plot x-axis and y-axis

plt.grid(True)

plt.title("Monthly Revenue Over Time")
plt.xlabel("Year-Months")
plt.ylabel("Revenue")

plt.style.use("classic")
plt.xticks(rotation=45)

plt.savefig("Monthly_Revenue_Plot.png" , dpi=300)


plt.show() # to see data


# In[ ]:


plt.figure(figsize=(12,6)) # Decide Size of Canvas

plt.plot(monthly_revenue.index , monthly_revenue.values , marker="o") # plot x-axis and y-axis

plt.grid(True)

plt.title("Monthly Revenue Over Time")
plt.xlabel("Year-Months")
plt.ylabel("Revenue")

plt.style.use("ggplot")
plt.xticks(rotation=45)


plt.show() # to see data


# In[ ]:


plt.figure(figsize=(12,6))
plt.plot(monthly_revenue.index , monthly_revenue.values , marker='o')

plt.xlabel("Revenue")
plt.ylabel("Year-Month")
plt.title("Revenue Vs Months")
plt.grid(True)
plt.style.use("ggplot")
plt.xticks(rotation=45)

for i , value in enumerate(monthly_revenue):
    plt.text(monthly_revenue.index[i] , value , f"{int(value):,}" , ha="left" ,)

plt.show()

