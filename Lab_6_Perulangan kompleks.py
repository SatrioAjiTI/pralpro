#Satrio Aji Utomo 71200538

"""
Samir ingin membuat diagram batang yang menampilkan progres yang telah dia lakukan
dengan menggunakan perulangan for dan while buatlah suatu progress bar untuk samir

Input :
    - Batas akhir progress bar
    - nilai progress awala
    - pilihan untuk menambah mengurang atau mengakiri progress

Proses :
    - melakukan input data
    - melakukan perulangan while
    - menampilkan perulangan for dalam bentuk progress bar
    - pemilihan input dari user

Output :
    - progress bar
    - pilihan input

"""
start = 0
full = int(input("Masukkan batas akhir progress bar :"))
nilai = int(input("Masukkan nilai progress anda :"))

while start != 3 :
    print ("Ini adalah progress bar anda")
    for i in range(1,full + 1):
        print ("|", i , "|", end="")
    print ()

    for x in range (nilai):
        print ("| # |", end="")
    print()

    print("1. Tambah progress")
    print("2. Mengurangi progress")
    print("3. Keluar dari progress")
    start = int(input("Masukkan Input :"))

    if start == 1 :
        tambah = int(input("Masukkan nilai tambah progress :"))
        nilai = nilai + tambah

    if start == 2 :
        kurang = int(input("Masukkan nilai yang akan dikurangi dari progress :"))
        nilai = nilai - kurang

    if start == 3 :
        print("Terimakasih telah menggunakan progress bar kami")
        break

    if nilai == full :
        print ("Ini adalah progress bar anda")
        for i in range(1,full + 1):
            print ("|", i , "|", end="")
        print ()

        for x in range (nilai):
            print ("| # |", end="")
        print()

        print("Selamat progress anda telah selesai")
        break
    
    
    
    

    