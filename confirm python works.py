import pandas as pd

df = pd.DataFrame({
    'weight': [1, 2, 3, 4, 5, 6],
    'score': [10, 15, 10, 20, 15, 25],
    'group': ['A', 'A', 'B', 'B', 'A', 'B']
})

weighted_avg = df.groupby('group').apply(
    lambda x: (x['score'] * x['weight']).sum() / x['weight'].sum()
)

print(weighted_avg)
