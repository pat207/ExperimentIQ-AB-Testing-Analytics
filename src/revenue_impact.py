import pandas as pd

df = pd.read_csv("data/ab_test_data.csv")

# Conversion rates
group_rates = df.groupby("group")["converted"].mean()

rate_A = group_rates["A"]
rate_B = group_rates["B"]

# Business assumptions
monthly_visitors = 100000
average_order_value = 100  # dollars

# Expected conversions
conversions_A = monthly_visitors * rate_A
conversions_B = monthly_visitors * rate_B

extra_conversions = conversions_B - conversions_A

monthly_revenue_gain = (
    extra_conversions * average_order_value
)

annual_revenue_gain = (
    monthly_revenue_gain * 12
)

print("REVENUE IMPACT ANALYSIS:\n")

print(f"Conversion Rate A: {rate_A:.4%}")
print(f"Conversion Rate B: {rate_B:.4%}")

print(f"\nExtra Conversions per Month: {extra_conversions:.0f}")

print(
    f"Monthly Revenue Gain: ${monthly_revenue_gain:,.2f}"
)

print(
    f"Annual Revenue Gain: ${annual_revenue_gain:,.2f}"
)