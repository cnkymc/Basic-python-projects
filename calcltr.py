
def toplama(x,y):
    return x+y
def cikarma(x,y):
    return x-y
def carpma(x,y):
    return x*y
def bolme(x,y):
    return x/y

print("Yapılacak İşlemi Seçin.")
print("=======================")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")


while True:

    secim = int(input("Seçiminiz (1/2/3/4):"))
    sayi1=float(input("1. sayı:"))
    sayi2=float(input("2. sayı:"))


    if secim==1:
        print(toplama(sayi1,sayi2))
    elif secim==2:
        print(cikarma(sayi1,sayi2))
    elif secim==3:
        print(carpma(sayi1,sayi2))
    elif secim==4:
        print(bolme(sayi1,sayi2))
    else:
         print("Geçersiz işlem")

