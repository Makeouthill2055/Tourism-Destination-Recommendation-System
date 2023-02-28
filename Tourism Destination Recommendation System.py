#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
from scipy import sparse
import matplotlib
print(pd.__version__)


# In[16]:


user = pd.read_csv('user.csv')
location = pd.read_csv('locations.csv')
tourism = pd.merge(location,user).drop(['Category','timestamp'], axis=1)
tourism.head()


# In[17]:


tourism.info()


# In[18]:


tourism_group = tourism.groupby('Place_Ratings')['Place_Name'].count().sort_values(ascending=False).head(100)
tourism_group.plot.bar()


# In[19]:


tourism_group = tourism.groupby('Place_Id')['Place_Name'].count().sort_values(ascending=False).head(10)
tourism_group.plot.bar()


# In[20]:


tourism.groupby('Place_Ratings')['Place_Name'].count().plot.pie(autopct="%1f%%")


# In[21]:


tourism_group = tourism.groupby('User_Id')['Place_Name'].count().sort_values(ascending=False).head(10)
tourism_group.plot.bar()


# In[22]:


tourism_ratings = tourism.pivot_table(index=['User_Id'], columns=['Place_Name'],values='Place_Ratings')
tourism_ratings.head()


# In[23]:


##
print("Before: ",tourism_ratings.shape)
tourism_ratings = tourism_ratings.dropna(thresh=10,axis=1).fillna(0)
print("After: ",tourism_ratings.shape)


# In[24]:


corrMatrix = tourism_ratings.corr(method='pearson')
corrMatrix.head(5)
item_similarity_df = tourism_ratings.corr(method='pearson')
item_similarity_df.head(20)


# In[25]:


def get_similar(Place_Name,Place_Ratings):
    similar_ratings = corrMatrix[Place_Name]*(Place_Ratings-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings


# In[26]:


mountain_lover = [("Bukit Panguk Kediwung",5),("Bukit Gantole Cililin",2),("Blue Lagoon Jogja",1),("Air Terjun Kedung Pedut",2)]
similar_location = pd.DataFrame()
for users,locations in mountain_lover:
    similar_location = similar_location.append(get_similar(users,locations),ignore_index = True)

similar_location.head(5)


# In[27]:


similar_location.sum().sort_values(ascending=False).head(20)


# In[28]:


beach_lover = [("Bandros City Tour",5),("Bangsal Pagelaran",4),("Bukit Gantole Cililin",2),("Atlantis Land Surabaya",4)]
similar_location = pd.DataFrame()
for users,locations in beach_lover:
    similar_location = similar_location.append(get_similar(users,locations),ignore_index = True)

similar_location.head(10)
similar_location.sum().sort_values(ascending=False).head(10)


# In[ ]:




