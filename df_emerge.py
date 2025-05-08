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
# Concatenate the datasets in the data frame and convert the data frame to a csv file
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('energy_dataset1.csv', index=False)  

# Drop the “Values” column, convert the updated data frame to a csv file and print out the merged electricity dataset 
final_df.drop(labels=['Values'], axis=1, inplace=True) 
final_df.to_csv('electricity_dataset1.csv', index=False) 
print(final_df) 

