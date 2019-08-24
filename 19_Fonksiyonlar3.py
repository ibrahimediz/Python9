
# fonk2 = lambda a,b : fonk(a)*fonk(b)
# fonk3 = lambda x : x[0]

# print(fonk3("BEŞİKTAŞ"))
# print(fonk(2))
# print(fonk2(2,3))

# liste = ["çiğdem","sinem","elif","ışıl","ışınsu","aleyna","özge","zeynep"]

# alfabe = "abcçdefghıijklmnoöprsştuüvyz"
# cevrim = { alfabe[alfabe.index(i)]:alfabe.index(i) for i in alfabe }
# print(sorted(liste,key=lambda a: cevrim.get(a[0])))


# a = 5
# def fonk():
#     a = 2
#     print(a)
#     a = 3
# fonk()
# print(a)

# a = 4
# def fonk():
#     global a 
#     a = 6
# print(a)
# fonk()
# print(a)

# def outerFunc(a):
#     a = 2
#     def innerFunc(a):
#         a = a * 2
#         return a
#     a =  innerFunc(a)
#     return a
# print(outerFunc(2))


# def saydir(metin):
#     print(metin)
#     if not len(metin) == 1:
#         saydir(metin[1:])  
   


