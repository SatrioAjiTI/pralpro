#Satrio Aji Utomo 71200538
#Universitas Kristen Duta Wacana

"""
Samir adalah pemmilik toko kain. dia ingin memiliki program untuk menghitung harga total
yang perlu dibayarkan oleh pembeli. Berikut adalah jenis kain yang dijual samir.
kain denim, kain drill, kain katun, dan kain polyester. dan harga dari kain per meter adalah 34.500, 48.000, 31.000, dan 25.000
dan program yang di harapkan samir dapat mencatat nama dari pembeli.

input :
    - Nama pembeli
    - Jenis kain yang akan dibeli
    - Jumlah kain yang dibutuhkan dalam meter

proses :
    - Mengimput nama pembeli
    - Menampilkan jenis dan harga per meter
    - Mengimput jenis kain
    - Mengimput jumlah kain dalam meter
    - Menghitung harga dengan mengalikan harga jenis kain dengan jumlah kain per meter
    - Menampilkan nama pembeli dan harga yang harus dibayar

output :
    - Menampilkan jenis kain dan harga per meter
    - Menampilkan nama pembeli
    - Menampilkan jumlah uang yang harus dibayar pembeli

"""
#Judul
print ("== Toko Kain Samir ==")

#Proses
nama = str(input("Masukan nama anda : "))
print ("Hallo ", nama)
print ("===============================")
print ("Denim --------------- Rp 34.500")
print ("Drill --------------- Rp 48.000")
print ("Katun --------------- Rp 31.000")
print ("Polyester ----------- Rp 25.000")
print ("===============================")

jenis = str(input("Masukan jenis kain yang akan anda beli : "))
jenis = jenis.lower()

panjang = float(input("Masukan panjang kain dalam meter : "))

#Perhitungan
if jenis == "denim" :
    harga = panjang * 34500
    print ("Hi ",nama,", harga yang perlu anda bayar adalah Rp ",harga)

if jenis == "drill" :
    harga = panjang * 48000
    print ("Hi ",nama,", harga yang perlu anda bayar adalah Rp ",harga)

if jenis == "katun" :
    harga = panjang * 31000
    print ("Hi ",nama,", harga yang perlu anda bayar adalah Rp ",harga)

if jenis == "polyester" :
    harga = panjang * 25000
    print ("Hi ",nama,", harga yang perlu anda bayar adalah Rp ",harga)

else :
    print ("Terimakasih",nama," telah berkunjung.")