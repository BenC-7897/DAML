import pandas as pd # Import pandas
import os # Operation system
import matplotlib.pyplot as plt # Graph creation
import seaborn as sns # Graph visualisation

# Change directory and upload the filled dataset to the newly created summary data frame 
os.chdir('C:/Users/bencr/Downloads/Dataset_1')
g_summary_df = pd.read_csv('gas_dataset2_filled.csv')

# Convert the date to datetime, set the date column and drop the NaN values
g_summary_df['Date'] = pd.to_datetime(g_summary_df['Date'])
g_summary_df.set_index('Date', inplace=True)
last_value = g_summary_df.dropna(how='all').index[-1]

# Add up the gas usage values until the last recorded value 
g_summary_df = g_summary_df.loc[:last_value]
g_summary_df['Gas_Consumption'] = g_summary_df.sum(axis=1)

# Create the line plot with the dates on the x-axis and the daily gas usage on the y-axis 
plt.figure(figsize=(14, 6))
sns.lineplot(data=g_summary_df, x=g_summary_df.index, y='Gas_Consumption', color='blue', label='Daily Consumption')
plt.title('Daily Gas Consumption 2023 and 2024', fontsize=16)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Gas Usage (units)', fontsize=12)
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.show()

