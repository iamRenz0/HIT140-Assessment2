import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Load the datasets
df = pd.read_csv('dataset1 (1).csv')
df = pd.read_csv('dataset2 (1).csv')

# Reading the CSV files
dataset1 = pd.read_csv('dataset1 (1).csv')
dataset2 = pd.read_csv('dataset2 (1).csv')


# Merge the datasets on 'ID' column
merged_dataset = pd.merge(dataset1, dataset2, on='ID', how='inner')

# Calculate the central tendencies (median)
median_values = merged_dataset.median()

# Visualizing screen time for different categories
plt.figure(figsize=(12, 8))

# Specify the columns related to screen time
columns = ['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']

# Plotting the boxplot to understand the distribution and outliers
sns.boxplot(data=merged_dataset[columns])

# Adding titles and labels
plt.title('Distribution of Screen Time Usage (Weekdays vs Weekends)', fontsize=16)
plt.xlabel('Activity Type', fontsize=12)
plt.ylabel('Hours per Day', fontsize=12)

# Show the plot
plt.show()

# Output the median values
print(median_values)
