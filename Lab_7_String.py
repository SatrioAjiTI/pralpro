#Satrio Aji Utomo 71200538

"""
Samir ingin membuat program yang dapat memisahkan kalimat menjadi kata
tanpa menggunakan spasi

Input:
    - Masukkan kalimat yang akan diproses

Proses:
    - Memisahkan kalimat menjadi kata
    - Menampilkan kalimat tanpa spasi
Output:
    - Kalimat awal ditampilkan lagi tanpa menggunakan spasi

"""

kalimat = str(input("Masukkan kalimat yang akan diproses penghilangan spasi: "))

kalimat = kalimat.lower()

kalimat = kalimat.split(" ")

for tanpaSpasi in kalimat:
    print(tanpaSpasi,end="")

