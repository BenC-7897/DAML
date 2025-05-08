import pandas as pd 
import os 
from sklearn.model_selection import train_test_split
os.chdir('C:/Users/bencr/Downloads/Dataset_2') 
testing_df = pd.read_csv('cleaned_dublin_air_quality.csv')
X = testing_df.drop(columns=['gps_timestamp'])
Y = testing_df['gps_timestamp']
X_training, X_temporary, Y_training, Y_temporary = train_test_split(X, Y, test_size=0.2, random_state=42)
X_validation, X_testing, Y_validation, Y_testing = train_test_split(X_temporary, Y_temporary, test_size=0.5, random_state=42)
print(f"Training set size: {X_training.shape[0]} samples")
print(f"Validation set size: {X_validation.shape[0]} samples")
print(f"Testing set size: {X_testing.shape[0]} samples")

