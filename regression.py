import pandas as pd
import os 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

os.chdir('C:/Users/bencr/Downloads/Dataset_2')
df = pd.read_csv('cleaned_dublin_air_quality.csv')

# Prepare the data
X = df.drop(columns=['gps_timestamp', 'PM25_ugm3'])
Y = df['PM25_ugm3']

# Split the data
X_training, X_temporary, Y_training, Y_temporary = train_test_split(X, Y, test_size=0.2, random_state=42)
X_validation, X_testing, Y_validation, Y_testing = train_test_split(X_temporary, Y_temporary, test_size=0.5, random_state=42)

print(f"Training set size: {X_training.shape[0]} samples")
print(f"Validation set size: {X_validation.shape[0]} samples")
print(f"Testing set size: {X_testing.shape[0]} samples")

# Train the model
model = LinearRegression()
model.fit(X_training, Y_training)

# Evaluate the model
Y_val_pred = model.predict(X_validation)
mse = mean_squared_error(Y_validation, Y_val_pred)
print(f"Validation MSE: {mse}")

# Test the model
Y_test_pred = model.predict(X_testing)
test_mse = mean_squared_error(Y_testing, Y_test_pred)
print(f"Test MSE: {test_mse}")

plt.figure(figsize=(14, 8))
plt.scatter(Y_testing, Y_test_pred, color='blue', edgecolor='k', alpha=0.7)
plt.plot([Y_testing.min(), Y_testing.max()], [Y_testing.min(), Y_testing.max()], 'k--', lw=2)
plt.xlabel('Actual PM2.5 Concentration (ug/m3)')
plt.ylabel('Predicted PM2.5 Concentration (ug/m3)')
plt.title('Actual vs Predicted PM2.5 Concentration')
plt.show()
