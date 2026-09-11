from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Baseline conversion rate
baseline_rate = 0.05

# Expected improved conversion rate
new_rate = 0.065

effect_size = proportion_effectsize(
    baseline_rate,
    new_rate
)

analysis = NormalIndPower()

required_sample_size = analysis.solve_power(
    effect_size=effect_size,
    power=0.80,
    alpha=0.05,
    ratio=1
)

print(" SAMPLE SIZE CALCULATOR:\n")

print(f"Baseline Conversion Rate: {baseline_rate:.2%}")
print(f"Expected Conversion Rate: {new_rate:.2%}")

print(f"\nRequired Users per Group: {required_sample_size:.0f}")
print(
    f"Total Users Needed: {required_sample_size*2:.0f}"
)