"""
Rakamla girilen sayıyı
yazı olarak ekrana 
yazan programı yazınız

5,859,265,321

Dokuz Milyon İki Yüz Altmış Beş Bin Üç Yüz Yirmi Bir
"""
basamak = {0:"",1:"Bin",2:"Milyon",3:"Milyar",4:"Trilyon",5:"Katrilyon"}
birler = {"0":"",
"1":"bir",
"2":"iki",
"3":"üç",
"4":"dört",
"5":"beş",
"6":"altı",
"7":"yedi",
"8":"sekiz",
"9":"dokuz",}
onlar = {"0":"",
"1":"on",
"2":"yirmi",
"3":"otuz",
"4":"kırk",
"5":"elli",
"6":"altmış",
"7":"yetmiş",
"8":"seksen",
"9":"doksan"}

# 5,859,265,321
miktar = input("Tutarı Yazınız")
# miktar = "5,859,265,321"
miktar =  miktar.replace(",","").replace(".","").strip()
print(miktar)
while len(miktar)%3 > 0:
    miktar = "0" + miktar
print(miktar)
print(len(miktar))
liste = []
for i in range(0,int(len(miktar)/3)):
    liste.append(miktar[i*3:(i*3)+3])

sonuc = ""
for i in range(0,len(liste)):
    if  liste[i][0] != "0":
        sonuc =  sonuc + birler[liste[i][0]] + " yüz "  
    sonuc = sonuc + onlar[liste[i][1]] + " "
    sonuc = sonuc + birler[liste[i][2]]  + " "
    sonuc = sonuc + basamak[(len(liste)-1)-i] + " "

print(sonuc)
   
    