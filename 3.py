import pandas as pd

# Load the dataset
file_path = 'data.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display the first few rows before handling missing values
print("First few rows of the dataset before handling missing values:")
print(data.head())

# Calculate the mean of the 'salary' and 'age' columns
mean_salary = data['salary'].mean()
mean_age = data['age'].mean()

# Replace missing values in 'salary' and 'age' columns with their respective means
data['salary'].fillna(mean_salary, inplace=True)
data['age'].fillna(mean_age, inplace=True)

# Display the first few rows after handling missing values
print("\nFirst few rows of the dataset after handling missing values:")
print(data.head())

# Save the updated dataset to a new CSV file
output_file_path = 'data_cleaned.csv'
data.to_csv(output_file_path, index=False)

print(f"\nUpdated dataset has been saved to '{output_file_path}'.")

