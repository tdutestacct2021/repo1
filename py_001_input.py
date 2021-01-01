# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas
df =pandas.read_csv('C:/thuan/python_training/panda_spyder/data/workday_chglog_new_add.csv')

print(df.head())
print(type(df))   
print(df.shape)   # number row and col
print(df.dtypes)
lastname_df=df[['Last Name', 'First Name']]

#print(lastname_df.head())
print(df.groupby(['RDT Number', 'Last Name']) ['day'].mean()) 
#grpby=df.groupby(['RDT Number', 'Last Name']) [['day'].mean() as avg]


#grpby.to_csv('C:/thuan/python_training/panda_spyder/data/grpby.csv', index=False) # wirte to output

