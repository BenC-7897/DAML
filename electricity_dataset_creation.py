import pandas as pd # Import pandas
import os # Operation system

# Change directory, obtain the electricity csv files and print the csv files
os.chdir('C:/Users/bencr/Downloads/Dataset_1') 
csv_files = ['electricity_usage_2023.csv', 'electricity_usage_2024.csv'] 
print(csv_files) 

# Create an empty data frame
dfs = [] 
for csv in csv_files: 
     # Read in the csv files and link the csv files together
    df = pd.read_csv(os.path.join("C:/Users/bencr/Downloads/Dataset_1", csv))
    dfs.append(df) 

# Concatenate the datasets in the data frame, convert the data frame to a csv file, drop the “Values” column, convert the date to datetime and convert the updated data frame to a csv file for electricity 
final_df = pd.concat(dfs, ignore_index=True) 
final_df.to_csv('energy_dataset2.csv', index=False) 
final_df.drop(labels=['Values'], axis=1, inplace=True)  
final_df['Date'] = pd.to_datetime(final_df['Date'], format="%d/%m/%Y") 
final_df.to_csv('electricity_dataset2.csv', index=False) 

# Definition function to fill in the NaN values with column mean, get the last recorded value in the dataset, obtain the column mean, fill the NaN with column mean values until the last recorded value and return the updated data frame
def gaps(df): 
    for column in df.columns[1:]:  
        last_value = df[column].last_valid_index()  
        mean = df.loc[:last_value, column].mean()  
        df.loc[:last_value, column] = df.loc[:last_value, column].fillna(mean) 
    return df 

# Fill in the gaps of the final_df, convert the updated data frame to csv and print the filled electricity dataset
final_df = gaps(final_df) 
final_df.to_csv('electricity_dataset2_filled.csv', index=False) 
print(final_df) 
