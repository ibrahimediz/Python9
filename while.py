islemmenu="""
1-Toplama
2-Çıkarma
3-Çarpma
4-Bölme
5-Çıkış
"""


anahtar = 1
while anahtar == 1:

    print(islemmenu)
    islem = int(input("İşlem Seçimi:"))
    if islem == 1:
        a = int(input("1. Sayı Seçimi:"))
        b = int(input("2. Sayı Seçimi:"))
        print(a + b)
    elif islem == 5:
        print("Çıkış")
        anahtar = 0

    