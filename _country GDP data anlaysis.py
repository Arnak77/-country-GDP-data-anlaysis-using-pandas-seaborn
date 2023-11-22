#!/usr/bin/env python
# coding: utf-8

# ## Dataframe in python and how to import the dataset
# ### pandas are very good package for dataframes & its perfect for dataset & very powerfull packages

# In[ ]:


import pandas as pd#USE FOR DATAFRAMES


# In[2]:


# How to read the dataet
start=pd.read_csv(r'D:\NIT\20NOV\17th,18th\DataFrame_ Pandas\data1.csv')


# In[3]:


start


# In[4]:


len(start)


# In[5]:


start.columns


# In[6]:


len(start.columns)


# In[7]:


start.head()


# In[8]:


start.head(2)


# In[9]:


start.tail()


# In[10]:


start.tail(4)


# In[11]:


start.info()


# In[12]:


start.dtypes


# In[13]:


start.describe()


# In[14]:


start.describe().transpose()


# In[15]:


start.head()


# In[16]:


start.columns


# In[17]:


start.columns=['a','b','c','d','e']


# In[18]:


start.columns


# In[19]:


start.head()


# In[20]:


start.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers','IncomeGroup']


# In[21]:


start


# In[22]:


start.columns


# In[23]:


start[21:26]


# In[24]:


start[:]


# In[25]:


start[:10]


# In[26]:


start.head(10)


# In[27]:


start[ : : -1]


# In[28]:


start


# In[29]:


start[: : 20]


# In[30]:


start.columns


# In[31]:


start.head()


# In[32]:


start['CountryName'].head()


# In[33]:


start['CountryName'].head(2)


# In[34]:


['CountryName','BirthRate']


# In[35]:


start[['CountryName','BirthRate']]


# In[36]:


start['CountryName']


# In[37]:


start[['CountryName','BirthRate']].tail()


# In[38]:


start.head()


# In[39]:


start.columns


# In[40]:


start['BirthRate']


# In[41]:


start[4:8][['BirthRate','CountryCode']]


# In[42]:


start[6:8][['BirthRate','CountryCode']]


# In[43]:


start[9:8][['BirthRate','CountryCode']]


# In[44]:


start[4:10][['BirthRate','CountryName']]


# In[45]:


start[['BirthRate','CountryName']][4:10]


# In[46]:


df1=start[['BirthRate','CountryName']]


# In[47]:


df1


# In[48]:


df2=start[4:10]


# In[49]:


df2


# In[50]:


start.head()


# In[51]:


start[['CountryCode','BirthRate','InternetUsers']][4:8]


# In[52]:


start.head()


# In[53]:


#Mathmetical operation =
start.BirthRate*start.InternetUsers


# In[54]:


start.BirthRate+start.InternetUsers


# In[55]:


start['Addition ']=start.BirthRate+start.InternetUsers


# In[56]:


start


# In[57]:


start['multiplication ']=start.BirthRate*start.InternetUsers


# In[58]:


start


# In[59]:


start.columns


# In[60]:


start


# In[61]:


start.columns[2]


# In[62]:


start.columns


# In[63]:


start.InternetUsers<2


# In[64]:


filter=start.InternetUsers<2


# In[65]:


filter


# In[66]:


start[filter]


# In[67]:


start.BirthRate>40


# In[68]:


filter2=start.BirthRate>40


# In[69]:


start[filter2]


# In[70]:


len(filter2)


# In[71]:


len(start[filter])


# In[72]:


len(start[filter2])


# In[73]:


filter & filter2


# In[74]:


start[filter & filter2]


# In[75]:


start.head(
)


# In[76]:


filter3=start[start.IncomeGroup == 'Low income']


# In[77]:


filter3


# In[78]:


start[start.IncomeGroup == 'High income']


# In[79]:


start.IncomeGroup.unique()


# In[80]:


start.IncomeGroup.nunique()


# In[81]:


# Introduction to seaborn # seaborn is very powerfull visualizatio(STATISTIC VISULAIZATION) pkg in python


# In[82]:


import matplotlib as plt
import seaborn as sns


# In[83]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=8,5


# In[84]:


start.head(3)


# In[85]:


start = start.drop('Addition ',axis = 1) 


# In[88]:


start=start.drop('multiplication ',axis=1)


# In[89]:


start


# In[98]:


v1= sns.distplot(start['InternetUsers'],bins=15)


# In[99]:


v2=sns.distplot(start['BirthRate'])


# In[114]:


v3=sns.boxplot(data = start, x='IncomeGroup', y='BirthRate')


# In[123]:


v3=sns.boxplot(data = start, x='IncomeGroup', y='BirthRate')


# In[125]:


v4=sns.lmplot(data=start,x='InternetUsers',y='BirthRate')


# In[127]:


v4=sns.lmplot(data=start,x='InternetUsers',y='BirthRate',fit_reg=False)


# In[129]:


v4=sns.lmplot(data=start,x='InternetUsers',y='BirthRate',fit_reg=False,hue='IncomeGroup')

