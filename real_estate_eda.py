import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("real_estate_data.csv")

print("Dataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Size_sqft"] = df["Size_sqft"].fillna(df["Size_sqft"].median())
df["Price"] = df["Price"].fillna(df["Price"].median())

# Remove outliers using IQR
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df = df[(df["Price"] >= lower) & (df["Price"] <= upper)]

# Save cleaned dataset
df.to_csv("cleaned_real_estate_data.csv", index=False)

# Price Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Price"], bins=10, kde=True)
plt.title("Price Distribution")
plt.savefig("price_distribution.png")
plt.show()

# Neighborhood Price Comparison
plt.figure(figsize=(8,5))
sns.boxplot(x="Neighborhood", y="Price", data=df)
plt.title("Price Distribution by Neighborhood")
plt.savefig("neighborhood_prices.png")
plt.show()

# Size vs Price
plt.figure(figsize=(8,5))
sns.scatterplot(x="Size_sqft", y="Price", hue="Neighborhood", data=df)
plt.title("Size vs Price")
plt.savefig("size_vs_price.png")
plt.show()

print("\nEDA Completed Successfully!")