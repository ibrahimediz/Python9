anahtar = 1
liste=[]
while anahtar == 1:
    ad =  input("Adınızı Giriniz")
    if ad != 'çik':
        liste.append(ad)
    else:
        anahtar = 0
    print(liste)