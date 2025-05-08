import os
import pandas as pd

# Change directory
os.chdir('C:/Users/bencr/Downloads/Dataset_2')

# Upload the dataset 
df = pd.read_csv('AirView_DublinCity_Measurements_ugm3.csv')

# Convert the dates in timestamp to datetime 
df['gps_timestamp'] = pd.to_datetime(df['gps_timestamp'])

# Sort the dataset with the timestamp 
df = df.sort_values(by='gps_timestamp')

# Save the sorted dataset to a csv file 
df.to_csv('sorted_dublin_air_quality.csv', index=False)

