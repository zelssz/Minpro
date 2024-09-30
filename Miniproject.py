print("_______________________________")
print("Menghitung total harga barang  ")
print("Nama: Zelsya Rizqita Rahmadhini")
print("Kelas: A'Sistem Informasi      ")

#Meminta input harga barang dan jumlah pembelian dari pengguna
harga_barang = int(input("Masukkan harga barang: Rp. "))
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

#Fungsi untuk menghitung total harga
total_harga = jumlah_barang * harga_barang
batas_diskon = 250000
diskon = 0.25

if total_harga > batas_diskon:
    total_harga_setelah_diskon = total_harga * (1 - diskon)
    print(f"Total harga setelah diskon 25%: Rp. {total_harga_setelah_diskon:}")
    print("Selamat anda berhasil mendapatkan diskon sebesar 25%")

else:
    print(f"Total harga: Rp. {total_harga:}")
    print("Maaf anda tidak mendapatkan diskon sebesar 25%")
    