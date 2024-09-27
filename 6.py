import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
file_path = 'iris.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print("First few rows of the dataset:")
print(data.head())

# Set up the matplotlib figure
plt.figure(figsize=(16, 10))

# Create a box plot for Sepal Length
plt.subplot(2, 2, 1)  # (rows, columns, panel number)
sns.boxplot(x='species', y='sepal_length', data=data)
plt.title('Sepal Length Distribution by Species')

# Create a box plot for Sepal Width
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='sepal_width', data=data)
plt.title('Sepal Width Distribution by Species')

# Create a box plot for Petal Length
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='petal_length', data=data)
plt.title('Petal Length Distribution by Species')

# Create a box plot for Petal Width
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='petal_width', data=data)
plt.title('Petal Width Distribution by Species')

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()

