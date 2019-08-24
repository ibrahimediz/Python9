sayi1 = int(input("Sayı Giriniz"))
Asal = True
for i in range(2,sayi1):
    if sayi1%i == 0:
        Asal = False
        print("Asal Değildir")
if Asal:
    print("Asaldır")
    


