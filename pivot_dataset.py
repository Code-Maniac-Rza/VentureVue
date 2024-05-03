import pandas as pd

# Assuming your dataset is stored in a DataFrame named 'df'
df = pd.read_csv("labelled_sentiment_data.csv")

# Pivot the DataFrame
pivot_df = df.pivot_table(index=df.index, columns='category', values='sentiment_score')

# Reset index to make the categories as columns
pivot_df.reset_index(drop=True, inplace=True)

# Optional: Fill NaN values with 0 if needed
pivot_df.fillna(0, inplace=True)

# Print the pivoted DataFrame
pivot_df.to_csv("pivoted_sentiment_data.csv", index=False)