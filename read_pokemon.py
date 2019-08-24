import pandas as pd

print("start!")

df = pd.read_csv('data/pokemon.csv')

print(df[0:2])

first_rows = df.iloc[:10, 1:5]

print(first_rows)

print(first_rows.describe())