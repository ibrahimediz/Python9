import os
# import datetime as dt
# print(os.name)
# print(os.getcwd())
# print(os.sep)
# print(os.listdir())
# # os.mkdir("c:"+os.sep+input("klasör ismi giriniz"))
# tarih = dt.datetime.now()
# liste = [tarih.year,tarih.month,tarih.day,tarih.hour]
# sonuc = ""
# for item in liste:
#     sonuc +=str(item) + os.sep
# else:
#     os.makedirs(sonuc)
#     os.chdir(sonuc)
#     dosya = open(r"Log_1.txt","w")

# liste = os.walk(r"C:\Users\vektorel\.anaconda\navigator")
# for item in liste:
#     print(item)


# def listeleme(dizin,arananUzantı = ".py"):
#     baslangic = os.getcwd()
#     os.chdir(dizin)
#     liste = os.listdir()
#     dosyaListesi = []
#     for item in liste:
#         if not os.path.isdir(item):
#             if item.endswith(arananUzantı):
#                 dosyaListesi.append(item)
#         else:
#             dosyaListesi.extend(listeleme(item))
#     os.chdir(baslangic)
#     return dosyaListesi

# print(*listeleme(r"D:\İbrahim EDİZ"),sep="\n")

print(os.path.abspath("teldefter.csv"))
