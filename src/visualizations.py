import os
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportion_confint

# ==================================
# Setup
# ==================================

os.makedirs("figures", exist_ok=True)

plt.style.use("ggplot")

plt.rcParams.update({
    "font.size": 12,
    "axes.titlesize": 18,
    "axes.labelsize": 13,
    "figure.facecolor": "white",
    "axes.facecolor": "white"
})

df = pd.read_csv("data/ab_test_data.csv")

# ==================================
# Metrics
# ==================================

group_a = df[df["group"] == "A"]
group_b = df[df["group"] == "B"]

n_a = len(group_a)
n_b = len(group_b)

conv_a = group_a["converted"].sum()
conv_b = group_b["converted"].sum()

rate_a = conv_a / n_a
rate_b = conv_b / n_b

rate_a_pct = rate_a * 100
rate_b_pct = rate_b * 100

relative_improvement = (
    (rate_b - rate_a) / rate_a
) * 100

# ==================================
# Confidence Intervals
# ==================================

lower_a, upper_a = proportion_confint(
    conv_a,
    n_a,
    alpha=0.05
)

lower_b, upper_b = proportion_confint(
    conv_b,
    n_b,
    alpha=0.05
)

monthly_gain = 146944
annual_gain = 1763330

# ==================================
# 1. Conversion Rate Comparison
# ==================================

plt.figure(figsize=(8, 5))

bars = plt.bar(
    ["Variant A", "Variant B"],
    [rate_a_pct, rate_b_pct],
    color=["#4C78A8", "#54A24B"],
    width=0.55
)

plt.title(
    "Conversion Rate Comparison",
    fontweight="bold",
    pad=20
)

plt.ylabel("Conversion Rate (%)")

plt.ylim(4.0, 7.0)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

for bar, value in zip(
    bars,
    [rate_a_pct, rate_b_pct]
):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.05,
        f"{value:.2f}%",
        ha="center",
        fontweight="bold",
        fontsize=12
    )

plt.figtext(
    0.5,
    0.02,
    f"Variant B improved conversion by {relative_improvement:.1f}%",
    ha="center",
    fontsize=11
)

plt.tight_layout()

plt.savefig(
    "figures/conversion_rates.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==================================
# 2. Confidence Intervals
# ==================================

plt.figure(figsize=(8, 5))

plt.errorbar(
    ["Variant A", "Variant B"],
    [rate_a_pct, rate_b_pct],
    yerr=[
        [
            (rate_a - lower_a) * 100,
            (rate_b - lower_b) * 100
        ],
        [
            (upper_a - rate_a) * 100,
            (upper_b - rate_b) * 100
        ]
    ],
    fmt="o",
    markersize=12,
    capsize=8,
    linewidth=3
)

plt.title(
    "95% Confidence Intervals",
    fontweight="bold",
    pad=20
)

plt.ylabel("Conversion Rate (%)")

plt.ylim(4.0, 7.2)

plt.grid(
    axis="y",
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    "figures/confidence_intervals.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# ==================================
# 3. Revenue Impact
# ==================================

plt.figure(figsize=(9, 5))

bars = plt.barh(
    ["Monthly Gain", "Annual Gain"],
    [monthly_gain, annual_gain],
    color=["#4C78A8", "#54A24B"]
)

plt.title(
    "Projected Revenue Impact",
    fontweight="bold",
    pad=20
)

plt.xlabel("Revenue ($)")

for bar in bars:

    value = bar.get_width()

    plt.text(
        value + annual_gain * 0.01,
        bar.get_y() + bar.get_height()/2,
        f"${value:,.0f}",
        va="center",
        fontweight="bold"
    )

plt.tight_layout()

plt.savefig(
    "figures/revenue_impact.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Professional charts generated successfully!")