import pandas as pd # Import pandas
import os # Operation system

# Change directory and upload the filled dataset to the newly created summary data frame
os.chdir('C:/Users/bencr/Downloads/Dataset_1') 
summary_df = pd.read_csv('gas_dataset2_filled.csv') 

# Perform the description function on the summary data frame, convert the summary data frame back to csv for gas and print the gas dataset summary statistics
summary = summary_df.describe() 
summary.to_csv('gas_summary_statistics.csv') 
print(summary) 
