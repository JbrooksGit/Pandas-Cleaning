#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 14:19:01 2019

@author: jonathanbrooks
"""
#Submission for take home assignment for job application 

import pandas as pd
  

def write_to_csv(df):
    df.to_csv('question1a_append.csv', index=False)

df = pd.read_csv('question1_data.csv')

data = []

#delimits values into list indexes based on ;
for index, row in df.iterrows():
    data.append(row['VF_DATA'].split(';'))
    

#gets relevant fields from list of lists
age_list = []
sex_list = []
Tscore_list = []
for i in data:
    age_list.append(i[0])
    sex_list.append(i[1])
    Tscore_list.append(i[5])
    
age_value = []
sex_value = []
Tscore_value = []

age_header = str(age_list[0])
sex_header = str(sex_list[0])
Tscore_header = str(Tscore_list[0])

#gets header by pulling everything from before =
Header = [age_header[:(age_header.find("="))],sex_header[:(sex_header.find("="))],Tscore_header[:(Tscore_header.find("="))]] 
print(Header)

#gets values from lists by getting values after =
for x in age_list:
    age_value.append(x[(x.find('=')+1):])
    
for x in sex_list:
    sex_value.append(x[(x.find('=')+1):])
    
for x in Tscore_list:
    Tscore_value.append(x[(x.find('=')+1):])


#ended up not needing header algorithm by using Pandas instead lol
new_column = pd.DataFrame(
 {'AGE': age_value,
  'SEX': sex_value,
  'Tscore': Tscore_value})
 
df = df.merge(new_column, left_index = True, right_index = True)
df.to_csv('question1a_append.csv', index = False)

write_to_csv(df)



   


        

