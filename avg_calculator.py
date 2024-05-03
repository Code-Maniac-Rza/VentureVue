import pandas as pd

# Assuming your DataFrame is named 'df'
df = pd.read_csv("pivoted_sentiment_data.csv")

# Calculate the average values for each column
average_values = df.mean()

# Create a new DataFrame with the average values
average_df = pd.DataFrame(average_values).T  # Transpose to convert the Series to a DataFrame with one row

# Save the new DataFrame to a CSV file
average_df.to_csv('average_values.csv', index=False)
