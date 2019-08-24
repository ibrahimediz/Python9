def dosyaAc(adres="defter.csv"):
    import os 
    if os.path.exists(adres):
        dosya = open(adres,"r+")
    else:
        dosya = open(adres,"w+")
    return dosya


def dosyaKayit(ifade):
    dosya = dosyaAc("defter2.csv")
    dosya.read()
    dosya.write(ifade)
    dosya.close()

def dosyaOkuma():
    dosya = dosyaAc("defter2.csv")
    liste= dosya.readlines()
    for i in range(0,len(liste)):
        liste[i] = liste[i].strip("\n")
    return liste

def bakiyeKontrol(musteriNum):
    liste = dosyaOkuma()
    ayiklaListe = []
    for item in liste:
        if item.split(";")[0] == musteriNum:
            ayiklaListe.append(item)
    YazdirBakiye(ayiklaListe)


def dosyaYazListe(dosya,liste):
    dosya.seek(0)
    dosya.truncate()
    for i in range(0,len(liste)):
        liste[i] = liste[i]+"\n"
    dosya.writelines(liste)
    dosya.close()

def HesapNoKontrol(HesapNo,hesapTuru):
    liste = dosyaOkuma()
    sonuc = ""
    for item in liste:
        if item.split(";")[1] == HesapNo and hesapTuru == item.split(";")[2]:
            sonuc = item
    return sonuc

def tutarKontrol(musteriNo,HesapID,tutar):
    liste = dosyaOkuma()
    hesapListesi = []
    for item in liste:
        if item.split(";")[0] == musteriNo:
            hesapListesi.append(item)
    if int(hesapListesi[HesapID-1].split(";")[3]) >= int(tutar):
        return True
    else:
        return False


def temizle(metin):
    sonuc = ""
    for item in metin:
        sonuc += str(item) + ";"
    return sonuc.strip(";")

def YazdirBakiye(liste):
    for i in range(0,len(liste)):
        musno,hesapNo,Tur,Bakiye = liste[i].split(";")
        print("{}-{} Numaralı {} Hesabı => {}".format((i+1),hesapNo,Tur,Bakiye))

def havaleIslemiYap(hesapNo,hedefHesapNo,tutar):
    liste = dosyaOkuma()
    for i in range(0,len(liste)):
        temp =  liste[i].split(";")
        if temp[1] == hesapNo:
            temp[3] = int(temp[3]) -  int(tutar)
        if temp[1] == hedefHesapNo:
            temp[3] = int(temp[3]) +  int(tutar)
        liste.pop(i)
        liste.insert(i,temizle(temp))
    dosyaYazListe(dosyaAc("defter2.csv"),liste)
    print(*liste,sep="\n")
        
def hesapNoGetirVs(musteriNum,hesapSecim,param=1):
    liste = dosyaOkuma()
    hesapListesi = []
    for item in liste:
        if item.split(";")[0] == musteriNum:
            hesapListesi.append(item)
    return hesapListesi[hesapSecim-1].split(";")[param]



def AnaMenu():
    islem = """
    1-Bakiye
    2-Havale
    3-Çıkış
    """
    while True:
        print(islem)
        secim = input("Yapmak İstediğiniz İşlemi Seçiniz")
        if secim == "1":
            musteriNum = input("Müşteri Numaranızı Giriniz")
            bakiyeKontrol(musteriNum)
        elif secim == "2":
            musteriNum = input("Müşteri Numaranızı Giriniz")
            bakiyeKontrol(musteriNum)
            HesapSecim = int(input("Havale için hesap seçiniz"))
            hedefHesapNo = input("Havale için hedef hesap seçiniz")
            hesapTuru = hesapNoGetirVs(musteriNum,HesapSecim,2)
            hedefHesapBilgisi = HesapNoKontrol(hedefHesapNo,hesapTuru)
            if hedefHesapBilgisi:
                tutar = input("Havale Yapmak istediğiniz tutarı giriniz")
                if tutarKontrol(musteriNum,HesapSecim,tutar):
                    havaleIslemiYap(hesapNoGetirVs(musteriNum,HesapSecim),hedefHesapNo,tutar)
                else:
                    print("İşlem için hesabınız müsait değildir")
            else:
                print("Seçtiğiniz hesap bulunmamaktadır")
        elif secim=="3":
            break
AnaMenu()
