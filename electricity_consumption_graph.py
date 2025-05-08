import pandas as pd # Import pandas
import os # Operation system
import matplotlib.pyplot as plt # Graph creation 
import seaborn as sns # Graph visualisation 

# Change directory and upload the filled dataset to the newly created summary data frame 
os.chdir('C:/Users/bencr/Downloads/Dataset_1') 
e_summary_df = pd.read_csv('electricity_dataset2_filled.csv')

# Convert the date to datetime, set the date column and drop the NaN values
e_summary_df['Date'] = pd.to_datetime(e_summary_df['Date'])
e_summary_df.set_index('Date', inplace=True)
last_value = e_summary_df.dropna(how='all').index[-1]

# Add up the electricity usage values until the last recorded value 
e_summary_df = e_summary_df.loc[:last_value]
e_summary_df['Electricity_Consumption'] = e_summary_df.sum(axis=1)

# Create the line plot with the dates on the x-axis and the daily electricity usage on the y-axis 
plt.figure(figsize=(14, 6))
sns.lineplot(data=e_summary_df, x=e_summary_df.index, y='Electricity_Consumption', color='blue', label='Daily Consumption')
plt.title('Daily Electricity Consumption 2023 and 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Electricity Usage (Units)', fontsize=12)
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()
