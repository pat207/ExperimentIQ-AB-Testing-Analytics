import pandas as pd
import numpy as np

np.random.seed(42)

n_users = 10000

group = np.random.choice(
    ['A', 'B'],
    size=n_users
)

conversion = []

for g in group:
    if g == 'A':
        conversion.append(
            np.random.binomial(1, 0.05)
        )
    else:
        conversion.append(
            np.random.binomial(1, 0.065)
        )

df = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'group': group,
    'converted': conversion
})

df.to_csv(
    'data/ab_test_data.csv',
    index=False
)

print(df.head())
print("\nDataset Shape:", df.shape)