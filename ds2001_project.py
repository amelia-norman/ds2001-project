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
cleaned = df[["Gender", "Age.at.Initial.Pathologic.Diagnosis", "AJCC.Stage"]]
cleaned = cleaned.rename(columns={"Age.at.Initial.Pathologic.Diagnosis": "initial_age", "AJCC.Stage": "AJCC_stage"})

print(cleaned)
#%%
plt.scatter(cleaned.initial_age, cleaned.AJCC_stage)
plt.title('Age vs Cancer Stage')
plt.xlabel('Age') 
plt.ylabel('AJCC Breast Cancer Stage') 
plt.grid()

#%%

field = "AJCC_stage"
order = ["Stage I", "Stage IA", "Stage IB", "Stage II", "Stage IIA", "Stage IIB", "Stage III", "Stage IIIA", "StageIIIB", "Stage IIIC", "Stage IV"]

cleaned['AJCC_stage'] = [order.index(x) for x in cleaned['AJCC_stage']]

plt.xticks(range(len(order)), order)
plt.scatter(cleaned['initial_age'], cleaned['AJCC_stage'])