# #1 Mengimpor pustaka untuk membaca data, membuat grafik, dan mencari lokasi file.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# #2 Mengatur tampilan grafik Seaborn agar memakai latar putih dengan garis kisi.
sns.set_theme(style="whitegrid")

# #3 Menentukan folder tempat script berada, lalu membaca Car_sales.csv ke DataFrame.
project_dir = Path(__file__).resolve().parent
df = pd.read_csv(project_dir / 'Car_sales.csv')

# #4 Menampilkan ringkasan struktur dataset, seperti jumlah baris, kolom, dan tipe data.
print("=== INFO DATASET ===")
df.info()

# #5 Menghitung statistik deskriptif untuk kolom numerik, misalnya rata-rata dan nilai minimum/maksimum.
print("\n=== STATISTIK UTAMA ===")
print(df.describe())

# #6 Menjumlahkan penjualan tiap pabrikan, mengurutkannya dari terbesar, lalu mengambil lima teratas.
top_sales = df.groupby('Manufacturer')['Sales_in_thousands'].sum().sort_values(ascending=False).head(5)
print("\n=== TOP 5 PABRIKAN PENJUALAN TERTINGGI (in thousands) ===")
print(top_sales)

# #7 Memilih kolom pabrikan, model, dan harga; mengurutkan dari harga tertinggi dan mengambil lima mobil.
top_expensive = df[['Manufacturer', 'Model', 'Price_in_thousands']].sort_values(by='Price_in_thousands', ascending=False).head(5)
print("\n=== TOP 5 MOBIL TERMAHAL ===")
print(top_expensive)


# #8 Membuat kanvas grafik pertama dan menghitung sepuluh pabrikan dengan total penjualan terbesar.
plt.figure(figsize=(10, 6))
top_10_sales = df.groupby('Manufacturer')['Sales_in_thousands'].sum().sort_values(ascending=False).head(10)

# #9 Membuat diagram batang: nilai penjualan pada sumbu X dan nama pabrikan pada sumbu Y.
sns.barplot(
    x=top_10_sales.values,
    y=top_10_sales.index,
    hue=top_10_sales.index,
    hue_order=top_10_sales.index,
    palette="Blues_r",
    legend=False,
)

# #10 Memberi judul dan label sumbu, merapikan tata letak, menyimpan grafik, lalu menampilkannya.
plt.title('Top 10 Manufacturers by Total Sales (in Thousands)', fontsize=14, fontweight='bold')
plt.xlabel('Total Sales (in Thousands)', fontsize=12)
plt.ylabel('Manufacturer', fontsize=12)
plt.tight_layout()
plt.savefig(project_dir / 'top_manufacturers_sales.png', dpi=300)
plt.show()

# #11 Membuat kanvas grafik kedua untuk membandingkan harga mobil dengan tenaga kuda.
plt.figure(figsize=(10, 6))

# #12 Membuat scatter plot; setiap titik adalah mobil dan warnanya menunjukkan jenis kendaraan.
sns.scatterplot(data=df, x='Horsepower', y='Price_in_thousands', hue='Vehicle_type', palette='Set1', s=80, alpha=0.8)

# #13 Memberi judul dan label sumbu, menampilkan legenda, merapikan, menyimpan, lalu menampilkan grafik.
plt.title('Price vs Horsepower by Vehicle Type', fontsize=14, fontweight='bold')
plt.xlabel('Horsepower', fontsize=12)
plt.ylabel('Price (in Thousands USD)', fontsize=12)
plt.legend(title='Vehicle Type')
plt.tight_layout()
plt.savefig(project_dir / 'price_vs_horsepower.png', dpi=300)
plt.show()