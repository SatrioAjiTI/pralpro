#Satrio Aji Utomo 71200538
"""
Samir ingin mencatat siapa saja yang telah menerima gaji bulan ini
namun samir tidak tahu berapa jumlah pegawai yang harus di catat
dan sewaktu waktu dapat bertambah jumlahnya

Input :
    - Masukkan perintah yang akan di gunakan
    - Masukkan jumlah list yang akan di tambah kan
    - Masukan nama yang akan di hapus
    - Melihat nama yang ada di list
Process :
    - Perulangan while
    - Extend list
    - Delet item yang ada di list
Output :
    - Nama yang ada di list
    - Nama setelah di edit

"""
proses = 0
listPegawai = []

print ("Pencatatan Nama Penerima Gaji")

while proses != 4:
    print ("1. Menambahkan Nama")
    print ("2. Menghapus Nama")
    print ("3. Menampilkan Nama")
    print ("4. Exit")
    proses = int(input("Pilih proses yang akan di jalan kan: "))

    if proses == 1:
        print ("Program pemasukkan nama")
        ulang = input("Masukkan jumlah pegawai yang akan di input :")
        for i in range(int(ulang)):
            nama = input("Masukkan nama pegawai :")
            listPegawai.extend([nama])
    
    if proses == 2:
        print("Program penghapus nama")
        nama = input("Masukkan nama yang akan di hapus :")
        listPegawai.remove(nama)

    if proses == 3:
        print("Program penampilan list")
        print(listPegawai)

    if proses == 4:
        print("Terimakasih")
        break
