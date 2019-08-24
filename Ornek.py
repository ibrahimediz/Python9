import random
kolonSay = int(input("Kolon Sayısı Giriniz"))
buyukListe = []
while len(buyukListe) < kolonSay:
    liste = []
    for i in range(0,6):
        sayi  = random.randint(1,50)
        while sayi in liste:
            sayi  = random.randint(1,50)
        liste.append(sayi)
        liste.sort()
    if liste not in buyukListe:
        buyukListe.append(liste)
for item in buyukListe:
    print(item)

liste = [(1,2,3),(4,5,6)]
for a,b,c in liste:
    print(a,b,c)
# print(*buyukListe,sep="\n")
