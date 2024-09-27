import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from seaborn
iris = sns.load_dataset('iris')

# Count the frequency of each species
species_counts = iris['species'].value_counts()

# Create a pie plot
plt.figure(figsize=(8, 6))
plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99'])
plt.title('Frequency of Iris Species')
plt.show()

