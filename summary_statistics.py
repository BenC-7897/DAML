# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:19:25 2024
@author: bencr
"""
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Change directory to the location of the dataset
os.chdir('C:/Users/bencr/Downloads/Dataset_2')

# Load the dataset
ml_df = pd.read_csv('cleaned_dublin_air_quality.csv')

# Convert the 'gps_timestamp' column to datetime format
ml_df['gps_timestamp'] = pd.to_datetime(ml_df['gps_timestamp'])

# Extract the month and year from the 'gps_timestamp' column
ml_df['month_year'] = ml_df['gps_timestamp'].dt.to_period('M')

# List of pollutants to analyze 
pollutants = ['NO_ugm3', 'NO2_ugm3', 'O3_ugm3', 'CO_mgm3', 'CO2_mgm3', 'PM25_ugm3']

# Calculate summary statistics for each pollutant
summary_stats = ml_df[pollutants].describe()
print(summary_stats)

# Save the summary statistics to CSV files
summary_stats.to_csv('pollutants_summary_statistics.csv')

# Plot time series for other pollutants
plt.figure(figsize=(15, 10))
for i, pollutant in enumerate(pollutants, 1):
    plt.subplot(3, 2, i)
    sns.lineplot(x='gps_timestamp', y=pollutant, data=ml_df)
    plt.title(f'{pollutant}')
    plt.xlabel('Time')
    plt.ylabel(pollutant)

plt.tight_layout()
plt.show()