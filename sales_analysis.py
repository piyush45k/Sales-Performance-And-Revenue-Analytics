import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/sales_data.csv")

# Convert Order Date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Revenue Analysis
total_revenue = df['Sales'].sum()
print("Total Revenue:", total_revenue)

# Revenue by Region
region_sales = df.groupby('Region')['Sales'].sum()

# Plot
region_sales.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# Top Products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("Top 5 Products:\n", top_products)

# Monthly Revenue Trend
df['Month'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum()

monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
