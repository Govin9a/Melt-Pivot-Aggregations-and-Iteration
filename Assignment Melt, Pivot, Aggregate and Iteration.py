#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
diabetic_data = pd.read_csv('diabetic_data.csv') 


# In[11]:


Q_1 = pd.melt(diabetic_data, id_vars=['patient_nbr'], value_vars=['gender']) 
#using melt function to create a specific format of the DataFrame object where one or more columns work as identifiers
print(Q_1)


# In[25]:


Q_2 = diabetic_data.pivot(index='encounter_id', columns='admission_type_id', values='discharge_disposition_id')
#using pivot function to summarize multiple numeric variable
print(Q_2)


# In[16]:


Q_3 = diabetic_data.agg({'num_lab_procedures' : ['sum', 'min'], 'num_medications' : ['min', 'max']}) 
#.agg function for different aggregations per column.
print(Q_3)


# In[22]:


#Q_4 Iteration
for row_index,row in diabetic_data.iterrows():
#iterrows() returning the iterator yielding each index value along with a series containing the data in each row.
 print(row_index,row)


# In[24]:


Q_5 = diabetic_data.groupby(by=["number_outpatient"]).sum()
#grouping the data according to the categories and applying a function to the categories
print(Q_5)


# In[ ]:




