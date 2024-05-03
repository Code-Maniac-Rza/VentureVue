import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
data = pd.read_csv('average_values.csv', header=None, names=['Category', 'Value'])

plt.figure(figsize=(10, 6))
plt.plot(data['Category'], data['Value'], color='skyblue')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Data from CSV file')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig('average_values.png')
plt.show()