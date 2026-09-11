import pandas as pd

df = pd.read_csv("data/ab_test_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nGroup Counts:")
print(df["group"].value_counts())

print("\nConversion Counts:")
print(df["converted"].value_counts())

conversion_rates = (
    df.groupby("group")["converted"]
      .mean()
      .reset_index()
)

conversion_rates["converted"] = (
    conversion_rates["converted"] * 100
)

print("\nConversion Rates (%):")
print(conversion_rates)