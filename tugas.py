
import pandas as pd


data = {
    'Nama': ['dewi', 'imas', 'mudin', 'koko', 'erika', 'asep', 'vina', 'dadi', 'endah', 'Joko'],
    'Nilai_Matematika': [78, 85, 92, 66, 88, 73, 94, 58, 81, 76],
    'Nilai_Bahasa': [82, 79, 91, 60, 87, 75, 95, 62, 80, 70],
    'Umur': [21, 22, 20, 23, 22, 21, 20, 23, 22, 21]
}
df = pd.DataFrame(data)


print("5 Data Teratas:")
print(df.head(5))


print("\n5 Data Terbawah:")
print(df.tail(5))
