import pandas as pd

# Load the dataset from the CSV file
file_path = 'height_weight.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display the shape of the dataset
print(f"Shape of the dataset: {data.shape}")

# Print the first 10 rows
print("\nFirst 10 rows of the dataset:")
print(data.head(10))

# Print the last 10 rows
print("\nLast 10 rows of the dataset:")
print(data.tail(10))

# Print 20 random rows
print("\n20 Random rows from the dataset:")
print(data.sample(n=20))

