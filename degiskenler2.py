defter = open("defter.csv","a+")
adi = input("Adınızı Giriniz ")
soyadi = input("Soyadı Giriniz ")
telefon = input("Telefon Giriniz ")

print(adi,soyadi,telefon,sep=";",end="\n",file=defter)