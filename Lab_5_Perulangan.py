#satrio aji utomo 71200538

"""
Samir ingin menghitung uang yang dia miliki dan ingin 
mengetahui barang apa saja yang dapat samir beli
menggunakan uang nya saat ini

input :
    - Saldo awal dari pengguna
    - Nama dari barang yang akan dibeli oleh pengguna
    - Harga dari barang yang akan dibeli oelh pengguna

proses :
    - Memasukan saldo awal pengguna
    - Memasukan nama barang yang akan di beli
    - Memasukan jumlah barang yang akan di beli
    - Memasukan harga dari barang yang akan di beli
    - Melakukan proses penghitungan
    - Melakukan proses percabangan
    - Menampilkan barang yang tidak dapat dibeli
    - Menampilkan sisa saldo dari pengguna

output :
    - Barang yang tidak dapat dibeli oleh pengguna
    - Sisa saldo dari pengguna

"""
print ("Ini adalah aplikasi penghitung sisa saldo")

uang = int(input("Masukkan saldo awal yang anda miliki :"))

while uang >= 0 :
    barang = str(input("Masukkan nama barang yang akan anda beli :"))
    harga = int(input("Masukkan harga barang yang akan anda beli :"))
    jumlah = int(input("Masukkan jumlah barang yang akan anda beli :"))

    hargaTotal = harga * jumlah
    uang = uang - hargaTotal

    if uang < 0 :
        saldo = uang + hargaTotal
        print ("Anda tidak dapat membeli", barang,"dengan jumlah", jumlah,"karena saldo anda kurang")
        print ("Sisa saldo anda hanya", saldo)
        break
    else :
        print ("Saldo anda masih ", uang)
        continue