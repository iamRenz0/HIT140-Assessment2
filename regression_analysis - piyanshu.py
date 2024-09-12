import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('dataset1 (3).csv')
df2 = pd.read_csv('dataset2.csv')
df3 = pd.read_csv('dataset3.csv')

df = pd.merge(df1, df2, on='ID')
df = pd.merge(df, df3, on='ID')
df_clean = df.dropna()

df_clean['total_screen_time'] = df_clean[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

X = sm.add_constant(df_clean[['total_screen_time']])
y = df_clean['Optm']
model = sm.OLS(y, X).fit()

print(model.summary())

sns.scatterplot(data=df_clean, x='total_screen_time', y='Optm')
plt.title('Total Screen Time vs Optimism')
plt.show()
