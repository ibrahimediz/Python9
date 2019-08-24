dosya = open("defter2.csv","r+")
liste= dosya.readlines()
for i in range(0,len(liste)):
    liste[i] = liste[i].strip("\n")
print(liste)

