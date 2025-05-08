import pandas as pd # Import pandas
import os # Operation system

# Change directory and upload the filled dataset to the newly created summary data frame
os.chdir('C:/Users/bencr/Downloads/Dataset_1') 
summary_df = pd.read_csv('electricity_dataset2_filled.csv') 

# Convert the date to datetime and update the date columns 
summary_df['Date'] = pd.to_datetime(summary_df['Date']) 
summary_df.set_index('Date', inplace=True)

# Obtain the monthly summary statistics for electricity and convert back to csv 
aggregate_functions = ['mean', 'std', 'min', 'max']
summary_month_df = summary_df.resample('M').agg(aggregate_functions) 
summary_month_df.to_csv('monthly_electricity_summary_stats1.csv')
print(summary_month_df)
