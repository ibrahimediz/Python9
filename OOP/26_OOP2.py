# class evcilHayvan():
#     #sınıf özelliği
#     tur = "evcilHayvan"
 
#     tuyuzunlugu = ""
#     gozrengi = ""
#     isim = " "
#     cins = ""

#     def besle(self):
#         print(self.isim,"beslendi")


# class Kedi(evcilHayvan):
#     def tuyTara(self):
#         print(self.isim," tüyü tarandı")


# class Kopek(evcilHayvan):
#     def odulMamasi(self):
#         print(self.isim,"ödül maması verdim")



class Kedi():
   # sınıf özelliği (class attribute)
    tur = "evcilHayvan"
    
    def __init__(self,adi="",tuyuzunlugu="",cins=""):
        # örnek özellik (instance attribute)
        self.tuyuzunlugu = tuyuzunlugu
        self.ismi = adi
        self.cins = cins
        self.besle()

    # örnek metod (instance method)
    def besle(self):
        print(self.ismi,"beslendi")

    def tuyTara(self):
        print(self.ismi," tüyü tarandı")

duman = Kedi()