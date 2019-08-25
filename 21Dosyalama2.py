def dosyaAc(adres="defter.csv"):
    import os 
    if os.path.exists(adres):
        dosya = open(adres,"r+")
    else:
        dosya = open(adres,"w+")
    return dosya


dosya = dosyaAc("teldefter.csv")


def KayitAl(*args):
    sonuc =""
    for item in args:
        sonuc += input( item + " Giriniz") + ";"
    sonuc =  sonuc.rstrip(";") + "\n"
    return sonuc









def Listeleme():
    dosya = dosyaAc("teldefter.csv")
    liste = dosya.readlines()
    for i in range(0,len(liste)):
        metin = "{}-{}-{}-{}"
        temp =  liste[i].split(";")
        metin = metin.format((i+1),temp[0],temp[1],temp[2])
        print(metin)
    dosya.close()

# def Ekleme():
#     Listeleme()
#     dosya = dosyaAc("teldefter.csv")
#     liste =  dosya.readlines()
#     kayit =  KayitAl("Adı","Soyadı","Telefon")
#     liste.insert(0,kayit)
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


# def Guncelleme():
#     Listeleme()
#     dosya = dosyaAc("teldefter.csv")
#     liste = dosya.readlines()
#     kayitID = int(input("Düzenlemek istediğiz kayıt numarası"))
#     kayit = KayitAl("Adı","Soyadı","Telefon")
#     liste[kayitID-1] = kayit
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


# def Silme():
#     Listeleme()
#     dosya = dosyaAc("teldefter.csv")
#     liste = dosya.readlines()
#     kayitID = int(input("Silmek istediğiz kayıt numarası"))
#     liste.pop(kayitID-1)
#     dosya.seek(0)
#     dosya.truncate()
#     dosya.writelines(liste)
#     dosya.close()


def SilDuzEk(param=0):
    try:

        Listeleme()
        dosya = dosyaAc("teldefter.csv")
        liste = dosya.readlines()
        if param==1:
            kayit =  KayitAl("Adı","Soyadı","Telefon")
            liste.insert(0,kayit)
        elif param==2:
            kayitID = int(input("Düzenlemek istediğiz kayıt numarası"))
            kayit = KayitAl("Adı","Soyadı","Telefon")
            liste[kayitID-1] = kayit
        elif param==3:
            kayitID = int(input("Silmek istediğiz kayıt numarası"))
            liste.pop(kayitID-1)
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(liste)
    except:
        pass
    finally:
        dosya.close()