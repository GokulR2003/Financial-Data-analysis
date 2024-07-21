import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = '/mnt/data/Financial Analytics data.csv'
data = pd.read_csv(file_path)

print("First few rows of the dataset:")
print(data.head())

print("\nBasic information about the dataset:")
print(data.info())

print("\nSummary statistics of the dataset:")
print(data.describe())

data = data.drop(columns=['Unnamed: 4'])
data['Mar Cap - Crore'].fillna(data['Mar Cap - Crore'].mean(), inplace=True)
data['Sales Qtr - Crore'].fillna(data['Sales Qtr - Crore'].mean(), inplace=True)
print("\nDataset after handling missing values:")
print(data.info())
print("\nSummary statistics after handling missing values:")
print(data.describe())

plt.figure(figsize=(10, 6))
sns.histplot(data['Mar Cap - Crore'], bins=30, kde=True)
plt.title('Distribution of Market Capitalization (Crore)')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data['Sales Qtr - Crore'], bins=30, kde=True)
plt.title('Distribution of Quarterly Sales (Crore)')
plt.xlabel('Quarterly Sales (Crore)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Mar Cap - Crore', y='Sales Qtr - Crore', data=data)
plt.title('Market Capitalization vs. Quarterly Sales')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Quarterly Sales (Crore)')
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

top_10_market_cap = data.nlargest(10, 'Mar Cap - Crore')[['Name', 'Mar Cap - Crore']]
print("\nTop 10 companies by Market Capitalization:")
print(top_10_market_cap)
top_10_sales = data.nlargest(10, 'Sales Qtr - Crore')[['Name', 'Sales Qtr - Crore']]
print("\nTop 10 companies by Quarterly Sales:")
print(top_10_sales)
market_cap_sales_corr = data['Mar Cap - Crore'].corr(data['Sales Qtr - Crore'])
print(f"\nCorrelation between Market Capitalization and Quarterly Sales: {market_cap_sales_corr:.2f}")

print("Data analysis completed.")
