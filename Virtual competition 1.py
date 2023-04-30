#!/usr/bin/env python
# coding: utf-8

# Consider the following Python dictionary `data` and Python list `labels`:
# 
# ``` python
# data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
#         'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
#         'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#         'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
# 
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# ```
# 
# **1.** Create a DataFrame `df` from this dictionary `data` which has the index `labels`.

# In[1]:


import numpy as np
import pandas as pd
data ={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(data,index=labels)
df




# **2.** Display a summary of the basic information about this DataFrame and its data (*hint: there is a single method that can be called on the DataFrame*).

# In[2]:


df.info()


# **3.** Return the first 3 rows of the DataFrame `df`.

# In[3]:


df.head(3)


# **4.** Display the 'animal' and 'age' columns from the DataFrame `df`

# In[4]:


df.iloc[:,[0,1]]


# **5.** Display the data in rows `[3, 4, 8]` *and* in columns `['animal', 'age']'

# In[5]:


df.iloc[[3,4,8],[0,1]]


# **6.** Select only the rows where the number of visits is greater than 3.

# In[6]:


print('Rows where the number of visits is greater than 3')
print(df[df['visits']>3])


# **7.** Select the rows where the age is missing, i.e. it is `NaN`.

# In[7]:


print('Rows where the age is missing:')
print(df[df['age'].isna()])


# **8.** Select the rows where the animal is a cat *and* the age is less than 3.

# In[8]:


print('Rows where the animal is cat and the age is less than 3:')
print(df[(df['animal']== 'cat') & (df['age']< 3)])


# **9.** Select the rows where the age is between 2 and 4 (inclusive)

# In[9]:


print('Rows where the age is between 2 and 4(inclusive):')
print(df[df['age'].between(2,4)])


# **10.** Change the age in row 'f' to 1.5.

# In[10]:


print('Change the age in row f to 1.5:')
df.loc['f','age']=1.5
print(df)


# **11.** Calculate the sum of all visits in `df` (i.e. the total number of visits).

# In[11]:


print('Sum of all visits in df:')
df.sum().visits


# **12.** Calculate the mean age for each different animal in `df`.

# In[12]:


print('The mean age for each different animal in df:')
df.groupby(by='animal')['age'].mean()



# **13.** Append a new row 'k' to `df` with your choice of values for each column. Then delete that row to return the original DataFrame.

# In[13]:


print('Append a new row k to df:')
df.loc['k']=['cat',4.3,2,'yes']
print(df)
print('Return the Original DataFrame:')
df=df.drop('k')
print(df)



# **14.** Count the number of each type of animal in `df`.

# In[22]:


print('Count the number of each type of animal in df:')
import numpy as np
import pandas as pd
data ={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(data,index=labels)
df.groupby(by='animal').count()


# **15.** Sort `df` first by the values in the 'age' in *decending* order, then by the value in the 'visits' column in *ascending* order (so row `i` should be first, and row `d` should be last).

# In[15]:


print('Sort df first by the values in the age in decending order,then by the value in the visits column in ascending order:')
df.sort_values(by=['age','visits'],ascending=[False,True])


# **16.** The 'priority' column contains the values 'yes' and 'no'. Replace this column with a column of boolean values: 'yes' should be `True` and 'no' should be `False`.

# In[16]:


data ={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(data,index=labels)
df['priority']=df['priority'].map({'yes':True,'no':False})
df



# **17.** In the 'animal' column, change the 'snake' entries to 'python'.

# In[17]:


data ={'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df= pd.DataFrame(data,index=labels)
df['animal']=df['animal'].replace('snake','python')
df



# **18.** Load the ny-flights dataset to Python

# In[18]:


print('Read the ny-flights dataset to Python:')
ny_flights=pd.read_csv(r"C:\Users\Radhika K J\Downloads\ny-flights.csv")
ny_flights


# **19.** Which airline ID is present maximum times in the dataset

# In[35]:


max_airline_id=ny_flights['airline_id'].value_counts().idxmax()
max_airline_id


# **20.** Draw a plot between dep_delay and arr_delay

# In[33]:


import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(11.7,8.27))
plt.scatter(ny_flights['dep_delay'],ny_flights['arr_delay'],color ='red')
plt.xlabel('dep_delay')
plt.ylabel('arr_delay')
plt.show()




# In[ ]:





# In[ ]:




