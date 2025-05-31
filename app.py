import pandas as pd

# Load the local CSV file
recipes = pd.read_csv('epi_r.csv')  # make sure the filename matches exactly

# Display first few rows
print(recipes.head())

# Display info about data
print(recipes.info())

# Check for missing values
print(recipes.isnull().sum())
