import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'data1.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Sort data by 'name' to ensure a proper line plot
data_sorted = data.sort_values(by='name')

# Generate the line plot
plt.figure(figsize=(10, 6))
plt.plot(data_sorted['name'], data_sorted['salary'], marker='o', linestyle='-', color='b')
plt.xlabel('Name')
plt.ylabel('Salary')
plt.title('Line Plot of Name vs Salary')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()

