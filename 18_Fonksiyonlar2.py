def Fonksiyon(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc
print("a")

Fonksiyon(b=2,1,2,3,4,5)

def Fonksiyon2(**kwargs):
    liste = []
    for key,value in kwargs.items():
        if key == "TOPLA":
            sonuc = 0
            for i in value:
                sonuc += i
        if key == "CARP":
            sonuc = 1
            for i in value:
                sonuc *= i
        liste.append(sonuc)
    return liste


print(Fonksiyon2(TOPLA=[1,2,3,4],CARP=[1,2,3,4]))

# sayi = str(371)
# toplam = 0
# for i in sayi:
#     toplam += int(i)**len(sayi)
# print(sayi,toplam)





# giris = input("Sayı Giriniz")
# print(armstrongNumber(giris))

# sayi = str(371)
# toplam = 0
# for i in sayi:
#     toplam += int(i)**len(sayi)
# print(sayi,toplam)

def armstrongNumber(sayi):
    sayi = str(sayi)
    toplam = 0
    for i in sayi:
        toplam += int(i)**len(sayi)
    return int(sayi) == toplam

def findArmstrong():
    for i in range(10,10000):
        if armstrongNumber(i):
            print(i)
        else:
            continue
findArmstrong()



def faktoriyel(sayi):
    sayi = int(sayi)
    sonuc = 1
    for i in range(1,sayi+1):
        sonuc *= i
    return sonuc

def asalSayi(sayi):
    sayi = int(sayi)
    for i in range(2,sayi):
        if sayi%i == 0:
            return False
    else:
        return True 




