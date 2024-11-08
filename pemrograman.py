import pandas as pd
data = {
    'A': [6, 2, 10],
    'B': [5, 4, 3]
}
df = pd.DataFrame(data)


df['Penjumlahan'] = df['A'] + df['B']
df['Pengurangan'] = df['A'] - df['B']
df['Perkalian'] = df['A'] * df['B']
df['Pembagian'] = df['A'] / df['B']

print("Hasil aritmatika pada DataFrame:\n", df)
