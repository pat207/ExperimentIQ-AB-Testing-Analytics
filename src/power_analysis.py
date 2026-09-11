import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

df = pd.read_csv("data/ab_test_data.csv")

group_A = df[df["group"] == "A"]
group_B = df[df["group"] == "B"]

p1 = group_A["converted"].mean()
p2 = group_B["converted"].mean()

effect_size = proportion_effectsize(
    p1,
    p2
)

analysis = NormalIndPower()

power = analysis.power(
    effect_size=effect_size,
    nobs1=len(group_A),
    ratio=len(group_B) / len(group_A),
    alpha=0.05
)

print("POWER ANALYSIS:\n")

print(f"Group A Conversion Rate: {p1:.4%}")
print(f"Group B Conversion Rate: {p2:.4%}")

print(f"\nEffect Size: {effect_size:.4f}")
print(f"Statistical Power: {power:.4f}")

if power >= 0.8:
    print("\n Experiment is sufficiently powered")
else:
    print("\n Experiment may require more users")