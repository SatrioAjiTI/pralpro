#Satrio Aji Utomo (71200538)

"""
Samir ingin menghitung rumus kombinasi dengan menggunakan fungsi rekursif
bantulah samir menghitung dua bilangan

Input :
    - masukkan bilangan pertama atau n
    - masukkan bilangan kedua atau r

Proses :
    - mengurangi n dengan r
    - menghitung faktorial n
    - menghitung faktorial r
    - menghitung faktorial n-r
Output:
    - hasil kombinasi n,r
"""

def kombinasiPertama(a):
    if a == 0 or a == 1:
        return 1
    else :
        return kombinasiPertama(a-1) * a

def kombinasiKedua(b):
    if b == 0 or b == 1:
        return 1
    else :
        return kombinasiKedua(b-1) * b

def kombinasiKetiga(c):
    if c == 0 or c == 1:
        return 1
    else :
        return kombinasiKetiga(c-1) * c

a = int(input("Masukkan bilangan pertama yang akan di kombinasi: "))
b = int(input("Masukkan bilangan kedua yang akan di kombinasi: "))

c = a - b

x = kombinasiPertama(a)/ (kombinasiKedua(b)*kombinasiKetiga(c))

print (x)

    