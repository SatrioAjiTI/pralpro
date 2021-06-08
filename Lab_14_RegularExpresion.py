#Satrio aji utomo (71200538)
"""
Samir ingin anda membuat program yang dapat menghilangkan alphabet atau angka
dari kata yang di masukkan pengguna.

Input :
 - Kalimat
 - Pilihan apa yang akan di hilang kan

Proses :
 - Fungsi if untuk pemilihan
 - RegEx untuk penghapusan kata

Output :
 - Hasli olahan kata dengan pilihan
"""
import re

x = str(input("Masukkan kalimat sembarang: "))
print ("Pilihan proses")
print ("1. penghapusan alphabet")
print ("2. penghapusan angka")
pilihan = int(input("Masukan pilihan proses: "))

if pilihan == 1:
    hasil = re.findall("\d+",x)
    print (hasil)

if pilihan == 2:
    hasil = re.findall("\D+",x)
    print (hasil)

if pilihan != 1 and pilihan != 2:
    print ("Maaf inputan anda salah")