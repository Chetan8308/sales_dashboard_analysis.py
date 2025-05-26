import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load sales data
    df = pd.read_csv('sales_data.csv', parse_dates=['Order Date'])

    # Check data structure
    print("Data preview:")
    print(df.head())
    print("\nData info:")
    print(df.info())

    # Extract month for trend analysis
    df['Month'] = df['Order Date'].dt.to_period('M')

    # Monthly Sales Trend
    monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

    plt.figure(figsize=(10,5))
    sns.lineplot(data=monthly_sales, x='Month', y='Sales', marker='o')
    plt.title('Monthly Sales Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('monthly_sales_trend.png')  # Save plot image
    plt.show()

    # Sales by Region
    region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)

    plt.figure(figsize=(8,5))
    region_sales.plot(kind='bar', color='skyblue')
    plt.title('Sales by Region')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('sales_by_region.png')
    plt.show()

    # Top 10 Products by Sales
    top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,5))
    top_products.plot(kind='barh', color='orange')
    plt.title('Top 10 Products by Sales')
    plt.xlabel('Sales')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig('top_products.png')
    plt.show()

    # Profit Margin by Category
    category_profit = df.groupby('Category')[['Sales', 'Profit']].sum()
    category_profit['Profit Margin (%)'] = (category_profit['Profit'] / category_profit['Sales']) * 100

    print("\nProfit Margin by Category:")
    print(category_profit.sort_values(by='Profit Margin (%)', ascending=False))

if __name__ == "__main__":
    main()