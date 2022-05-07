#hitungBangun.py (pemanggilan fungsi)
import bangunruang
#menghitung volume tabung dan volume kerucut
r=15
tinggi_tabung=20
tinggi_kerucut=25
#menghitung volume balok dan volume prisma
panjang=10
lebar=5
tinggi_balok=15
tinggi_prisma=20

print("Menghitung Volume Tabung")
print(bangunruang.volumeTabung(r,tinggi_tabung))
print("Menghitung Volume Kerucut")
print(bangunruang.volumeKerucut(r,tinggi_kerucut))
print("Menghitung Volume Balok")
print(bangunruang.volumeBalok(panjang,lebar,tinggi_balok))
print("Menghitung Volume Prisma")
print(bangunruang.volumePrisma(panjang,lebar,tinggi_prisma))
