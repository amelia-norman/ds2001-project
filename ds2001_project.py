#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:24:26 2021

@author: amelianorman
"""

import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv(r'/Users/amelianorman/Desktop/ds2001-project/clinical_breast_cleaned.csv')
print(df.head())

#%%

# rename columns and remove rows with male participants 

cleaned = df[["Gender", "Age.at.Initial.Pathologic.Diagnosis", "AJCC.Stage"]]
cleaned = cleaned.rename(columns={"Age.at.Initial.Pathologic.Diagnosis": "initial_age", "AJCC.Stage": "AJCC_stage"})

cleaned = cleaned.drop(cleaned[cleaned.Gender == "MALE"].index)
        
print(cleaned.Gender.unique())

#%%
#plt.scatter(cleaned.initial_age, cleaned.AJCC_stage)
#plt.title('Age vs Cancer Stage')
#plt.xlabel('Age') 
#plt.ylabel('AJCC Breast Cancer Stage') 
#plt.grid()

#%%
# fixing indexing on graph; y-axis is showing values in the incorrect order

order = ["Stage I", "Stage IA", "Stage IB", "Stage II", "Stage IIA", "Stage IIB", "Stage III", "Stage IIIA", "Stage IIIB", "Stage IIIC", "Stage IV"]
order2 = ["I", "IA", "IB", "II", "IIA", "IIB", "III", "IIIA", "IIIB", "IIIC", "IV"]

cleaned['AJCC_stage'] = [order.index(x) for x in cleaned['AJCC_stage']]

df_sorted = cleaned.sort_values(["AJCC_stage", "initial_age", "Gender"], ascending=True)

df_sorted['AJCC_stage'] = [order2[x] for x in df_sorted['AJCC_stage']]

#%%
plt.scatter(df_sorted['initial_age'], df_sorted['AJCC_stage'])
plt.title('Age vs Cancer Stage')
plt.xlabel('Age') 
plt.ylabel('AJCC Breast Cancer Stage') 
plt.grid()

#%%
plt.scatter(df_sorted['AJCC_stage'], df_sorted['initial_age'])
plt.title('Age vs Cancer Stage')
plt.xlabel('AJCC Breast Cancer Stage') 
plt.ylabel('Age') 
plt.grid()

#%%
# groupby age; show age distribution

import numpy as np

#print(df_sorted['initial_age'].min()) # it's 30
#print(df_sorted['initial_age'].max()) # it's 88

#age_groups = ["30-39", "40-49", "50-59", "60-69", "70-79", "80-89"]

out = pd.cut(df_sorted['initial_age'], bins=[30, 40, 50, 60, 70, 80, np.inf])
out_norm = out.value_counts(sort=False, normalize=True).mul(100)
ax = out_norm.plot.bar(rot=0, color="pink", figsize=(6,4))
# ax.set_xticklabels([c[1:-1].replace(","," to") for c in out.cat.categories])
plt.title('Breast Cancer Patient Age Distribution')
plt.xlabel('Age') 
plt.ylabel('pct')
plt.show()

#%%
# bar graph for cancer stage grouped by age
print(df_sorted.head())
print(out.head())
        
    
