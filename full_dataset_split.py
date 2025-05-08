# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:48:52 2024
@author: bencr
"""
import pandas as pd 
import os 
from sklearn.model_selection import train_test_split
os.chdir('C:/Users/bencr/Downloads/Dataset_2') 
testing_df = pd.read_csv('airview_dublincity_roaddata_ugm3.csv')
X = testing_df.drop(columns=['road_id'])
Y = testing_df['road_id']
X_training, X_temporary, Y_training, Y_temporary = train_test_split(X, Y, test_size=0.4, random_state=42)
X_validation, X_testing, Y_validation, Y_testing = train_test_split(X_temporary, Y_temporary, test_size=0.5, random_state=42)
print(f"Training set size: {X_training.shape[0]} samples")
print(f"Validation set size: {X_validation.shape[0]} samples")
print(f"Testing set size: {X_testing.shape[0]} samples")

