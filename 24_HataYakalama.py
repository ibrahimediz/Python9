# try:
#     a = int(input("1. Sayı"))
#     b = int(input("2. Sayı"))
#     print(a/b)
# except ZeroDivisionError:
#     print("Sıfıra Bölünür mü bi sayı ? ")
# except ValueError:
#     print("Rakam Girmek çok mu zor ")
import os
import datetime as dt
def adresGetir(): 
    tarih = dt.datetime.now()
    liste = [tarih.year,tarih.month,tarih.day,tarih.hour]
    sonuc = ""
    for item in liste:
        sonuc +=str(item) + os.sep
    return sonuc

def LogKlasor():
    try:
        sonuc = adresGetir()
        os.makedirs(sonuc)
        os.chdir(sonuc)
        dosya = open(r"Log.txt","w")
    except Exception as hata:
        print(hata)

def LogTut(mesaj,tip):
    if os.path.exists(adresGetir()+os.sep+"Log.txt"):
        dosya=open(adresGetir()+os.sep+"Log.txt","r+")
        dosya.write("\n"+mesaj+":"+str(tip)+":"+str(dt.datetime.now()))
        dosya.close()
    else:
        LogKlasor()

try:
    adim = "1BolA"
    a = input("1. Sayı")
    if a != "Soner":
        a = int(input("1. Sayı"))
    else:
        raise Exception
    adim = "1BolB"
    b = int(input("2. Sayı"))
    adim = "1BolC"
    print(a/b)
except (ZeroDivisionError,ValueError):
    LogTut(adim,2)
    print("Hata :",adim,hata)
except Exception:
    print("Ama Lütfen Yaaa")

