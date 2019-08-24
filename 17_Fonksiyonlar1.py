# def Fonk():
#     pass

def KareAl(a):
    print(a**2)

# def KareAl2(a):
#     return a**2

# sonuc = KareAl2(2)
# print(sonuc)

# def cevirASCII(karakter):
#     sonuc = str(ord(karakter))
#     while len(sonuc)%3>0:
#         sonuc = "0" +sonuc
#     return sonuc

# def ASCIICevir(deger):
#     sonuc = chr(int(deger))
#     return sonuc

# def girisAl(isim):
#     deger = ""
#     for i in isim:   #A l i
#         deger+=cevirASCII(i) #deger = 065108105
#     return deger

# isim = input("isim giriniz")
# print(girisAl(isim))

def fonksiyon(a=0,b=0):
    sonuc = 0
    if a:
        sonuc =  a**b
    return sonuc


print(fonksiyon(b=5,a=4))