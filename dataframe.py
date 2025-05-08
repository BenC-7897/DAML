import pandas as pd
import os
os.chdir('C:/Users/bencr/Downloads/Dataset_1')
csv_files = [f for f in os.listdir("C:/Users/bencr/Downloads/Dataset_1") if f.endswith('.csv')]
print(csv_files)
dfs = [] 
for csv in csv_files: 
    df = pd.read_csv(os.path.join("C:/Users/bencr/Downloads/Dataset_1", csv))
    dfs.append(df)
final_df = pd.concat(dfs, ignore_index=True)
final_df.to_csv('combined_dataset.csv', index=False)
