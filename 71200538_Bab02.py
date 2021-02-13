#Satrio Aji Utomo 71200538
#Universitas Kristen Duta Wacana


"""
Samir ingin menghitug pendapatan dan pengeluarannya. Dalam satu bulan gaji Samir dihitung dari 
jumlah hari ia masuk. Dari gaji yang dia dapat 11% akan dia tabung, Setelah menabung 13.5% gaji Samir 
digunakan untuk membayar asuransi anggota keluarga nya.

gajiHari = gaji per hari masuk
hariMasuk = hari masuk per minggu * 4 
gajiKotor = gajiHari * hariMasuk
gajiTabung = gajiKotor - gajiKotor * 0.11
jumlahAsuransi = gajiTabung * 0.135
totalPengeluaran = gajiKotor * 0.11 + jumlahAsuransi
gajiBersi = gajiKotor - totalPengeluaran

input :
 + Gaji per hari masuk
 + Hari masuk dalam 1 minggu

proses :
 + Memasukan input gaji dan input hari
 + Menghitung gaji kotor
 + Menghitung gaji setelah menabung
 + Menghitung jumlah uang yang digunakan untuk membayar asuransi
 + Menghitung total pengeluaran
 + Menghitung gaji bersih
 + Menampilkan hasil hitung
 
output :
 + Gaji kotor
 + Gaji setelah menabung
 + Jumlah uang yang digunakan untuk membayar asuransi
 + Total pengeluaran
 + Gaji bersih
"""
print ("===== Penghitung pengeluaran =====")

#input
gajiHari = int(input("Masukan gaji per hari masuk : "))
hariMasuk = int(input("Masukan hari masuk dalam satu minggu : ")) * 4

#proses
gajiKotor = (gajiHari * hariMasuk)
gajiTabung = (gajiKotor - gajiKotor * 0.11)
jumlahAsuransi = (gajiTabung * 0.135)
totalPengeluaran = (gajiKotor * 0.11 + jumlahAsuransi)
gajiBersih = (gajiKotor - totalPengeluaran)

#output
print ("Gaji kotor anda adalah : ", gajiKotor)
print ("Gaji anda setelah menabung adalah : ", gajiTabung)
print ("jumlah uang anda yang digunakan untuk membayar asuransi adalah : ", round(jumlahAsuransi,3))
print ("Total pengeluaran anda adalah : ", totalPengeluaran)
print ("Gaji bersih anda adalah : ", gajiBersih)
 