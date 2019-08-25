import sys


# print(sys.version_info)
# print(sys.winver)
# print(sys.setrecursionlimit())
# if not sys.version_info.minor == 5:
#     print("Çalışmaz")
# print(*sys.path,sep="\n")
# sys.path.append(r"D:\İbrahim EDİZ\SYSICINDENEME")
# from  SINIFDos import SINIF
# print(*sys.path,sep="\n")
# print(sys.argv)

import random as rnd
print(rnd.random())
print(rnd.uniform(0.5,1.0))
print(rnd.randint(45,500))
liste = ["ali","veli","ebru","çisem","güneş","tuğçe","semih","duygu"]
print(rnd.choice(liste))
liste = list(range(20))
print(liste)
rnd.shuffle(liste)
print(liste)
liste = list(range(1,50))
print(rnd.sample(liste,6))


