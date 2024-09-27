import pandas as pd

# Load the winequality-red dataset
file_path = 'winequality-red.csv'  # Replace this with the path to your CSV file
wine_data = pd.read_csv(file_path)

# View the first few rows of the dataset
print("First few rows of the dataset:")
print(wine_data.head())

# Get basic statistical details of the dataset
print("\nBasic statistical details:")
print(wine_data.describe(include='all'))

# Additional details
print("\nData Types of Each Column:")
print(wine_data.dtypes)

print("\nMissing Values in Each Column:")
print(wine_data.isnull().sum())

print("\nCorrelation Matrix:")
print(wine_data.corr())

