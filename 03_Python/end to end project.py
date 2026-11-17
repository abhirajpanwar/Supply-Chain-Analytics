import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Point this path at your local DataCo dataset before running.
df = pd.read_excel(
    "DataCoSupplyChainDataset.PROJECT.xlsx",
    sheet_name="DataCoSupplyChainDataset.PROJEC"
)
print(df.shape)
print(df.isnull().sum())
print(df.head())
print(df.describe())
print(df.info())
print(df.tail())
print("duplicate rows:", df.duplicated().sum())
print(df.dtypes)
print(df.nunique())

df = df.drop(columns=[
    'Product Description', 'Order Zipcode', 'Customer Email',
    'Customer Password', 'Product Image', 'Customer Street'
])
print("Shape after dropping columns:", df.shape)
print(df.columns)
df["Customer Lname"] = df["Customer Lname"].fillna("Unknown")
print(df["Customer Lname"].isnull().sum())

for col in ['order date (DateOrders)', 'shipping date (DateOrders)']:
    df[col] = pd.to_datetime(df[col], format='mixed', errors='coerce')
print(df[['order date (DateOrders)', 'shipping date (DateOrders)']].dtypes)
df.to_excel("DataCoSupplyChain_Clean.xlsx", index=False)
print("successfully Data CLEANED")

df["Delivery Status"].value_counts().plot(kind="bar", color="skyblue", figsize=(8, 5))
plt.title("Delivery_Status_Distribution")
plt.xlabel("Delivery_Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Delivery_Status.png", dpi=300, bbox_inches="tight")
plt.show()

df["Late_delivery_risk"].value_counts().plot(kind="bar", color=["green", "red"], figsize=(6, 4))
plt.title("Late Delivery Risk")
plt.xlabel("risk")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Late_Delivery_risk.png", dpi=300, bbox_inches="tight")
plt.show()

df['Shipping Mode'].value_counts().plot(kind='bar', color='orange', figsize=(8, 5))
plt.title("Orders by Shipping Mode")
plt.xlabel("Shipping Mode")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Shipping_Mode.png", dpi=300, bbox_inches="tight")
plt.show()

sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("Sales_Distribution.png", dpi=300, bbox_inches="tight")
plt.show()
