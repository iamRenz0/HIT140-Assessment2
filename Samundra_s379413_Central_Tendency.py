import pandas as pd
import numpy as np

# A simple function to calculate the mean, median, and mode for each numerical column in the dataset
def calculate_central_tendency(dataset):
    # List to store results for each column
    results = []

     # Loop through each numerical column in the dataset
    for column in dataset.select_dtypes(include=[np.number]).columns:
        # Calculate mean, median, and mode
        mean_value = dataset[column].mean()
        median_value = dataset[column].median()
        mode_value = dataset[column].mode()[0]  # Mode can have multiple values, we take the first one

           # Store the results in a dictionary for this column
        results.append({
            'Column': column,
            'Mean': mean_value,
            'Median': median_value,
            'Mode': mode_value
        })

    # Return the results as a DataFrame (like a table) for easy viewing
    return pd.DataFrame(results)

# Load datasets from CSV files
dataset1 = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

# Calculate central tendencies for each dataset
central_tendency_1 = calculate_central_tendency(dataset1)
central_tendency_2 = calculate_central_tendency(dataset2)
central_tendency_3 = calculate_central_tendency(dataset3)

# Print the results in a friendly format
print("Central Tendency for Dataset 1:\n", central_tendency_1)
print("\nCentral Tendency for Dataset 2:\n", central_tendency_2)
print("\nCentral Tendency for Dataset 3:\n", central_tendency_3)

