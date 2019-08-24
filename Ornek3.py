dosya = open(r"D:\İbrahim EDİZ\Ornekler\sayisalloto.csv")
liste = dosya.readlines()
liste.reverse()
temizListe = []
for item in liste:
    temizListe.append(item.split(";")[1:])
for item in temizListe:
    item[5] = item[5].strip("\n")

liste2 = [i for i in range(1,50)]
sozluk = dict.fromkeys(liste2,0)

for cekilis in temizListe:
    for  item in cekilis:
        sozluk[int(item)] = sozluk[int(item)] + 1

import pandas as pd
deneme =  pd.DataFrame(temizListe)
print(deneme.describe())