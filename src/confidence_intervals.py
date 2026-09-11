import pandas as pd
from statsmodels.stats.proportion import proportion_confint

df = pd.read_csv("data/ab_test_data.csv")

for group in ["A", "B"]:

    data = df[df["group"] == group]

    conversions = data["converted"].sum()
    total = len(data)

    lower, upper = proportion_confint(
        count=conversions,
        nobs=total,
        alpha=0.05,
        method="normal"
    )

    print(f"\nGroup {group}")
    print(f"Conversion Rate: {conversions/total:.4%}")
    print(f"95% CI: [{lower:.4%}, {upper:.4%}]")