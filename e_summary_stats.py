import pandas as pd # Import pandas
import os # Operation system

# Change directory and upload the filled dataset to the newly created summary data frame 
os.chdir('C:/Users/bencr/Downloads/Dataset_1')
summary_df = pd.read_csv('electricity_dataset2_filled.csv') 

# Perform the description function on the summary data frame, convert the summary data frame back to csv for electricity and print the electricity dataset summary statistics 
summary = summary_df.describe() 
summary.to_csv('electricity_summary_statistics.csv') 
print(summary) 
