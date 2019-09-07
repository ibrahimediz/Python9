import os
class DosyaUtility():
    __uygulama = []
    dosyaUzanti = ".csv"
    def __init__(self,adres = "defter",**kwargs):
        self.adres = os.getcwd()+os.sep+adres+self.dosyaUzanti
        self._isim = adres
        self.dosya = None
        self.dosyaAc()
        self.uygulamaYaz()
        self.parametreler = kwargs
    
    @property
    def isim(self):
        return self._isim

    @isim.setter
    def isim(self,yeni_deger):
        indis = self.__uygulama.index(self._isim)
        self.__uygulama[indis] = yeni_deger
        self._isim = yeni_deger
        adres = os.getcwd()+os.sep+self._isim+self.dosyaUzanti
        self.dosya.close()
        os.rename(self.adres,adres)
        self.adres = adres

    


    def uygulamaYaz(self):
        self.__uygulama.append(self._isim)


    @staticmethod
    def PiSayisi():
        return 22/7

    @property
    def dosyaismi(self):
        return self.__dosyaIsmi

    @dosyaismi.setter
    def dosyaismi(self,yeni_deger):
        if yeni_deger == 5:
            self.__dosyaIsmi = yeni_deger
        return self.__dosyaIsmi
    

    @dosyaismi.deleter
    def dosyaismi(self):
        del self.__dosyaIsmi

    @classmethod
    def uygulamaListele(cls):
        print("Dosya Listesi")
        for item in cls.__uygulama:
            print(item)

    def dosyaAc(self):
        if os.path.exists(self.adres):
            dosya = open(self.adres,"r+")
        else:
            dosya = open(self.adres,"w+")
        self.dosya = dosya

    def arama(self):
        self.dosyaAc()
        giris = input("Aramak istediğiniz kelime ya da sayıyı giriniz")
        self.dosya.seek(0)
        liste = self.dosya.readlines()
        aramasonuc = []
        for item in liste:
            for i in item.split(";"):
                if giris.upper() in i.upper():
                    aramasonuc.append(item)
                    break
        self.yazdir(aramasonuc)



    # def arama2(self):
    #     self.dosyaAc()
    #     giris = input("Aramak istediğiniz kelime ya da sayıyı giriniz")
    #     self.dosya.seek(0)
    #     liste = self.dosya.readlines()
    #     aramasonuc = []
    #     for item in liste:
    #         for i in item.split(";"):
    #             if giris.upper() in i.upper():
    #                 aramasonuc.append(item)
    #                 break
    #     self.yazdir(aramasonuc)

    
        
             
    def yazdir(self,liste):
        for i in range(0,len(liste)):
            metin = "{}-".format((i+1))
            for item in liste[i].split(";"):
                metin+= item + "-"
            print(metin)


    def Listele(self):
        print("-"*20)
        print(self.adres)
        self.dosyaAc()
        self.dosya.seek(0)
        liste = self.dosya.readlines()
        for i in range(0,len(liste)):
            metin = "{}-".format((i+1))
            for item in liste[i].split(";"):
                metin+= item + "-"
            print(metin)
        self.dosya.close()

    def girisAl(self):
        sonuc = ""
        for key,value in self.parametreler.items():
            if key=="ALANLAR":
                for item in value:
                    sonuc+= input(item + " giriniz ") + ";"
        sonuc = sonuc.rstrip(";") + "\n"
        return sonuc 

    def idu(self,param=0):
        self.Listele()
        kayit = ""
        self.dosyaAc()
        liste = self.dosya.readlines()
        # ekleme
        if param == 1:
            kayit = self.girisAl()
            liste.insert(0,kayit)
        #düzeltme
        elif param == 2:
            kayitID = int(input("Düzenlenecek Kaydı Seç"))
            kayit = self.girisAl()
            liste[kayitID-1] = kayit
        #silme
        elif param==3:
            kayitID = int(input("Silinecek Kaydı Seç"))
            liste.pop(kayitID-1)
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writelines(liste)
        self.dosya.close()
if __name__ == "__main__":
    dosyaislem =  DosyaUtility("kendisinden",ALANLAR=["Adı","Soyadı","Telefon"])
    menu = """
    1-Ekleme
    2-Düzeltme
    3-Silme
    4-Listeleme
    5-Arama
    6-Çıkış
    """
    anahtar = 1
    while anahtar == 1:
        print("*"*30)
        print(menu)
        print("*"*30)
        islem = int(input("İşlem Seçimi"))
        if islem in (1,2,3):
            dosyaislem.idu(islem)
        elif islem == 4:
            dosyaislem.Listele()
        elif islem == 5:
            dosyaislem.arama()
        elif islem == 6:
            anahtar = 0
        else:
            print("Menü Dışında Seçenek Girdin ")
    else:
        print("İyi Günler Dileriz")
    