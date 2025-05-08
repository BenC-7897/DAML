import pandas as pd
import os 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('C:/Users/bencr/Downloads/Dataset_2')
df = pd.read_csv('cleaned_dublin_air_quality.csv')

# Define air quality categories based on PM2.5 concentration (example thresholds)
def air_quality(pm25):
    if pm25 <= 12.5:
        return 'Good'
    elif 12.5 <= pm25 <= 25:
        return 'Fair'
    elif 25 <= pm25 <= 50:
        return 'Poor'
    elif 50 <= pm25 <= 150:
        return 'Very Poor'
    else:
        return 'Extremely Poor'

# Apply the categorization function to create a new column
df['Air_Quality'] = df['PM25_ugm3'].apply(air_quality)

# Prepare the data
X = df.drop(columns=['gps_timestamp', 'PM25_ugm3', 'Air_Quality'])
Y = df['Air_Quality']

# Split the data into training, validation, and testing sets
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.2, random_state=42)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5, random_state=42)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Validation set size: {X_val.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Train the model using Logistic Regression
model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, Y_train)

# Evaluate the model on the validation set
Y_val_pred = model.predict(X_val)
print("Validation Set Classification Report:")
print(classification_report(Y_val, Y_val_pred))

# Evaluate the model on the test set
Y_test_pred = model.predict(X_test)
print("Test Set Classification Report:")
print(classification_report(Y_test, Y_test_pred))

# Convert the gps_timestamp column to datetime
df['gps_timestamp'] = pd.to_datetime(df['gps_timestamp'])

# Convert datetime to a numerical format (e.g., timestamp)
df['timestamp_numeric'] = df['gps_timestamp'].apply(lambda x: x.timestamp())

# Set the style of seaborn
sns.set(style="whitegrid")

# Create a regplot for PM2.5 against time
plt.figure(figsize=(14, 8))
sns.regplot(x='timestamp_numeric', y='PM25_ugm3', data=df, scatter_kws={'s':10}, line_kws={'color':'red'})
plt.title('Regression Plot of PM2.5 vs Time')
plt.xlabel('Time')
plt.ylabel('PM2.5 (µg/m³)')

# Customize the x-axis to show datetime labels
plt.xticks(ticks=df['timestamp_numeric'][::len(df)//10], labels=df['gps_timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')[::len(df)//10], rotation=45)

# Show the plot
plt.show()