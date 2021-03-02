
def modulus (x1,x2):
    mod = x1%x2
    return mod

def floordiv (x1,x2):
    floordiv = x1//x2
    return floordiv

def square (x1,x2):
    square = x1**x2
    return square

print ("Selamat datang di Kalkulator sederhana")
print("ketik 1 untuk mencari modulus")
print("ketik 2 untuk mencari floor division")
print("ketik 3 untuk mencari pemangkatan")
program = int(input("Masukan plihan Anda: "))
if program == 1:
    x1 = int(input("Masukan bilangan pertama: "))
    x2 = int(input("Masukan bilangan kedua: "))
    print ("Hasil" ,x1,"Modulus" , x2 , "adalah",modulus(x1,x2))
elif program == 2:
    x1 = int(input("Masukan bilangan pertama: "))
    x2 = int(input("Masukan bilangan kedua: "))
    print ("Hasil" ,x1,"Floor division" , x2 , "adalah",floordiv(x1,x2))
elif program == 3:
    x1 = int(input("Masukan bilangan pertama: "))
    x2 = int(input("Masukan bilangan kedua: "))
    print ("Hasil" ,x1,"Pangkat" , x2 , "adalah",square(x1,x2))
else :
    print ("Terima Kasih Satrio")