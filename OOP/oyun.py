from OrnekOOP import DeadPool,Hulk,IronMan
import random
import time
liste = [DeadPool,Hulk,IronMan]
hareketListesi = ["vurusYap","savunmaYap","darbe"]
karakter1= random.choice(liste)()
karakter2 = random.choice(liste)()

def calistir(kar1,hareket,kar2):
    if hareket == 1:
        kar1.vurusYap(kar2)
    elif hareket == 2:
        kar1.savunmaYap(kar2.vurus)
    elif hareket == 3:
        kar1.darbe(kar2.vurus)

while True:
    time.sleep(3)
    karakter1Har =  random.randrange(1,4)
    karakter2Har =  random.randrange(1,4)
    calistir(karakter1,karakter1Har,karakter2)
    calistir(karakter2,karakter2Har,karakter1)
    if (not karakter1.saglik or not karakter1.guc) or (not karakter2.saglik or not karakter2.guc):
        print("Oyun Bitti")
        break
