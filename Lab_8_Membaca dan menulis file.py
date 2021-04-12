#Satrio Aji Utomo 71200538

"""
Samir ingin membuat program yang dapat mengetahui kalimat terpanjang dalam suatu file .txt
bantulah samir membuat program yang dapat menemukan kalimat terpanjang dalam suatu file

Input:
    - Memasukkan nama file dan lokasi file .txt
Proses:
   - input nama file dan lokasi file
   - Program akan mebaca file perkalimat
   - program akan menentukan kalimat terpanjang dalam file tersebut
   - Menampilkan kalimat terpanjang dalam file tersebut
Output:
    - kalimat terpanjang dalam file tersebut
"""

def kalimatTerpanjang(namaFile):
    handle = open(namaFile, 'r')
    kalimat = handle.read().split(",")
    terpanjang = len(max(kalimat,key=len))
    return [kalimat for kalimat in kalimat if len(kalimat) == terpanjang]

namaFile = input("Masukkan nama file yang akan di cek (d:/daftarbuku.txt) : ")
print (kalimatTerpanjang(namaFile))