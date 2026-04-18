import pandas as pd
df= pd.read_csv("train.csv")


# Normalize column names
df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace('-', '_')

# Convert dates
df['order_date']= pd.to_datetime(df['order_date'], dayfirst=True)
df['ship_date']= pd.to_datetime(df['ship_date'], dayfirst=True)

# Calculate shipping_days
df['shipping_days'] = (df['ship_date'] - df['order_date']).dt.days

# Convert sales to numeric
df['sales']=pd.to_numeric(df['sales'], errors='coerce')

# Add year and month
df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month

# Clean data
df=df.drop_duplicates()
df=df.dropna()

# Groupby operations (though not assigned, perhaps for inspection)
print(df.groupby('order_year')['sales'].sum())
print(df.groupby('region')['sales'].sum().sort_values(ascending=False))
print(df.groupby('category')['sales'].sum())
print(df.groupby('sub_category')['sales'].sum().sort_values(ascending=False))
print(df.groupby('customer_name')['sales'].sum().nlargest(10))
print(df.groupby('segment')['sales'].sum())
print(df.groupby('ship_mode')['shipping_days'].mean())
print(df.groupby('order_month')['sales'].sum())
print(df)

df.to_csv("cleaned_sales.csv", index=False)