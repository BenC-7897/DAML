import os
import pandas as pd

# Change directory to where the dataset is located
os.chdir('C:/Users/bencr/Downloads/Dataset_2')

# Load the dataset
df = pd.read_csv('airview_dublincity_roaddata_ugm3.csv')

# Columns to be cleaned
columns_clear = ['NO2_ugm3', 'NO_ugm3', 'CO2_mgm3', 'CO_mgm3', 'O3_ugm3', 'PM25_ugm3', 'NO2drives', 'NOdrives', 'CO2drives', 'COdrives', 'O3drives', 'PM25drives']

# Drop NaN values and negative values for the specified columns
for column in columns_clear:
    df = df[df[column].notna()]  
    df = df[df[column] >= 0]  

# Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_roadside_dublin_air_quality.csv', index=False)
