#encapsulation
#abstraction
#inheritance
#polymorphism

class evcilHayvan():
    tuyuzunlugu = ""
    gozrengi = ""
    isim = " "
    cins = ""

    def besle(self):
        print(self.isim,"beslendi")


class Kedi(evcilHayvan):
    def tuyTara(self):
        print(self.isim," tüyü tarandı")


class Kopek(evcilHayvan):
    def odulMamasi(self):
        print(self.isim,"ödül maması verdim")


duman = Kedi()
duman.tuyuzunlugu = "kısa"
duman.isim = "duman"

misket = Kedi()
misket.tuyuzunlugu = "uzun"
misket.isim = "misket"




hayko = Kopek()
hayko.isim = "hayko"
hayko.odulMamasi()
misket.besle()


