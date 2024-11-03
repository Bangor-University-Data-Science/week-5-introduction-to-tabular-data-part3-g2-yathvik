import pandas as pd
def import_data(filename):
    if filename.endswith(".csv"):
        df = pd.read_csv(filename)
        return df
    elif filename.endswith(".xlsx"):
        df = pd.read_excel(filename)
        return df
filename = "Customer_Behavior.xlsx"
df = import_data(filename)


def filter_data(df):
    df = df[~(df["CustomerID"].isna())]
    df = df[(df["Quantity"] >= 0) & (df["UnitPrice"] >= 0)]
    return df

filtered_df = filter_data(df)
print(filtered_df.head())


def loyalty_customers(df, min_purchases):
    purchase_counts = df.groupby("CustomerID").count()
    loyal_customers = purchase_counts[purchase_counts["InvoiceNo"] >= min_purchases]
    return loyal_customers

min_purchases = 10 
loyal_df = loyalty_customers(df, min_purchases)
print(loyal_df.head())

def quarterly_revenue(df):
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
    df["Quarter"] = df["InvoiceDate"].dt.to_period("Q")
    df["Revenue"] = df["Quantity"] * df["UnitPrice"]
    total_revenue = df.groupby("Quarter")["Revenue"].sum().reset_index()
    total_revenue.columns = ["Quarter", "Total Revenue"]
    return total_revenue

revenue_df = quarterly_revenue(df)
print(revenue_df.head())
  

def high_demand_products(df, top_n):
    total_quantity = df.groupby("StockCode")["Quantity"].sum().reset_index()
    sorted_products = total_quantity.sort_values(by="Quantity", ascending=False)
    top_products = sorted_products.head(top_n)
    return top_products

top_n = 10 
top_products_df = high_demand_products(df, top_n)
print(top_products_df)


def purchase_patterns(df):
    summary = df.groupby("Description")[["Quantity", "UnitPrice"]].mean().reset_index()
    summary.columns = ["Description", "avg_quantity", "avg_unit_price"]
    summary.rename(columns={"Description": "product"}, inplace=True)
    return summary

print(purchase_patterns(df))


