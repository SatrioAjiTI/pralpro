#Satrio Aji Utomo (71200538)

"""
Samir ingin menampilkan angka paling banyak muncul dalam suatu
kelompok namun samir tidak tahu berapa banyak angka yang harus dia masukkan

Input :
    - masukkan angka kedalam kelompok
    - masukkan angka 0 untuk berhenti

Proses :
    - perulangan while
    - penentuan bilangan terbesar
Output:
    - bilangan terbesar
"""

start = 1
kelangka = []

while start != 0:
    start = int(input("Masukkan angka kedalam kelompok (0 untuk berhenti) :"))
    if start == 0:
        break
    kelangka.extend([start])

    
maxnum = 0
kel = dict()
for i in kelangka:
    if i not in kel:
        kel[i] = 1
    else:
        kel[i] = kel[i] + 1
for j in kel:
    if kel.get(j) > maxnum:
        maxnum = kel.get(j)

for k in kel:
    if kel.get(k) == maxnum:
        print (k, "Muncul sebanyak", kel[k])