class EvcilHayvan():
    tur = "EvcilHayvan"
    def __init__(self,adi="",tuyuzunlugu="",cins=""):
        #örnek özellik (instance attribute)
        self.tuyuzunlugu = tuyuzunlugu
        self.ismi = adi
        self.cins = cins
        self.besle()
    # örnek metod (instance method)
    def besle(self):
        print(self.ismi,"beslendi")
    


class Kedi(EvcilHayvan):
    #sınıf özelliği (class attribute)
    tur = "Kedi"

    def __init__(self,adi="",tuyuzunlugu="",cins=""):
        super().__init__(adi,tuyuzunlugu,cins)
    def besle(self):
        return True

    def tuyTara(self):
        print(self.ismi," tüyü tarandı")

class Kopek(EvcilHayvan):
    #sınıf özelliği (class attribute)
    tur = "Kopek"
    def __init_(self,adi="",tuyuzunlugu="",cins=""):
        super().__init__(adi,tuyuzunlugu,cins)
    
    def odulMamasi(self):
        print(self.ismi," Ödül Maması Aldı")