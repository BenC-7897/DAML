import os
import pandas as pd

# Change directory
os.chdir('C:/Users/bencr/Downloads/Dataset_2')

# Upload the dataset 
df = pd.read_csv('sorted_dublin_air_quality.csv')

# Columns to be cleaned
columns_clear = ['CO_mgm3', 'CO2_mgm3', 'NO_ugm3', 'NO2_ugm3', 'O3_ugm3', 'PMch1_perL', 'PMch2_perL', 'PMch3_perL', 'PMch4_perL', 'PMch5_perL', 'PMch6_perL']

# Drop NaN values and negative values for the columns
for column in columns_clear:
    df = df[df[column].notna()]  
    df = df[df[column] >= 0]  

# Save the sorted dataset to a csv file
df.to_csv('cleaned_dublin_air_quality.csv', index=False)
