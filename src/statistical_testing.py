import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

df = pd.read_csv("data/ab_test_data.csv")

group_A = df[df["group"] == "A"]
group_B = df[df["group"] == "B"]

successes = [
    group_A["converted"].sum(),
    group_B["converted"].sum()
]

totals = [
    len(group_A),
    len(group_B)
]

z_stat, p_value = proportions_ztest(
    successes,
    totals
)

print("Group A Conversions:", successes[0])
print("Group B Conversions:", successes[1])

print("\nZ-Statistic:", round(z_stat, 4))
print("P-Value:", p_value)

if p_value < 0.05:
    print("\n Statistically Significant")
    print("Version B performs better than Version A")
else:
    print("\n Not Statistically Significant")