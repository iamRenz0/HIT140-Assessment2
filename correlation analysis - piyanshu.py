import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Read the data
dataset1 = pd.read_csv('dataset1 (3).csv')
dataset2 = pd.read_csv('dataset2.csv')
dataset3 = pd.read_csv('dataset3.csv')

#Merged datasets to include screen time, demographic information and well being indicators
merged_data = pd.merge(dataset2, dataset3, on='ID')

#Covert the data into panda DataFrame
df = pd.DataFrame(merged_data)

#Here calculate the correlation matrix
correlation_matrix = df.corr()

# Now display the correlation matrix
print(correlation_matrix)

# Here visualize the correlation matrix using a heatmap
plt.figure(figsize = (10, 8))
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm', fmt = ".2f")
plt.title("Correlation Matrix")
plt.show()

