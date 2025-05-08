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
pollutants_pmch = ['PMch1_perL', 'PMch2_perL', 'PMch3_perL', 'PMch4_perL', 'PMch5_perL', 'PMch6_perL']

# Calculate summary statistics for each pollutant
summary_stats_pmch = ml_df[pollutants_pmch].describe()
print(summary_stats_pmch)

# Save the summary statistics to CSV files
summary_stats_pmch.to_csv('pollutants_summary_statistics_pmch.csv')

# Plot time series for PMch pollutants
plt.figure(figsize=(15, 10))
for i, pollutant in enumerate(pollutants_pmch, 1):
    plt.subplot(3, 2, i)
    sns.lineplot(x='gps_timestamp', y=pollutant, data=ml_df)
    plt.title(f'{pollutant}')
    plt.xlabel('Time')
    plt.ylabel(pollutant)

plt.tight_layout()
plt.show()

