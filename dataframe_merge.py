# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 13:03:41 2024
@author: bencr
"""
import pandas as pd
import os
os.chdir('C:/Users/bencr/Downloads/Dataset_1')
csv_files = [f for f in os.listdir("C:/Users/bencr/Downloads/Dataset_1") if f.endswith('.csv')]
print(csv_files)
dfs = [] 
for csv in csv_files: 
    df = pd.read_csv(os.path.join("C:/Users/bencr/Downloads/Dataset_1", csv))
    dfs.append(df)
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('energy_dataset.csv', index=False)
final_df.drop(labels=['Values'], axis=1, inplace=True)
final_df.to_csv('e_dataset1.csv', index=False)
print(final_df) 
