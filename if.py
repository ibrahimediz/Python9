sayi = int(input("Sayıyı Giriniz"))
if sayi%2 == 0:
    print("Sayı Çifttir")
else:
    print("Sayı Tektir")


sayi = int(input("Parametre Giriniz"))
if sayi == 1 and sayi>0 or sayi !=2:
    print("parametre 1")
elif sayi == 2:
    print("parametre 2")
else:
    print("yanlış parametre")


liste = [1,2]
liste2 = liste
if liste is liste2:
    print("Doğru")
metin = "BEŞİKTAŞ"
if 3 in liste:






"""
kullanıcıdan alınan sifre verisinin girilip 
girilmediğini tespit eden algoritmayı yazınız

"""
# liste = ["123","456","qwe","aaa"]
# sifre = input("Sayıyı Giriniz")
# if sifre:
#     if sifre not in liste:
#         print("Şifre Yanlış")
#     else:
#         if sifre.isalnum():
#             print("Giriş Başarılı")
#         else:
#             if sifre.isnumeri():
#                 print("Giriş Eksik")
#             elif sifre.islower():
#                     print("giriş hep küçük")
# else:
#     print("Giriş Başarısız")
   


"""
a == b --a eşittir b
a != b --a eşit değildir b
a >= b --a büyük eşittir b
a <= b --a küçük eşittir b
a > b  --a büyüktür b 
a < b  --a küçüktür b
a and b -- a ve b
a or b -- a veya b
a not b -- a değil b
a in b -- a b'nin içinde mi
a is b -- a b mi

"""

"""
FF 0-35
DD 35-50
CC 50-65
BB 65-80
AA 80-100
"""
notunuz = int(input("Notunuzu Giriniz"))
if notunuz>0 and notunuz <= 35:
    print("FF")
elif notunuz >35 and notunuz <= 50:
    print("DD")
elif notunuz >50 and notunuz <= 65:
    print("CC")
elif notunuz >65 and notunuz <= 80:
    print("BB")
elif notunuz >80 and notunuz <= 100:
    print("AA")
else:
    print("Hesaplanamadı")
print("İyi Günler")

