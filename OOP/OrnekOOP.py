class MarverHero():
    def __init__(self,guc,saglik,vurus,savunma,isim):
        self.guc = guc
        self.saglik = saglik
        self.vurus = vurus
        self.savunma = savunma
        self.isim = isim

    def vurusYap(self,eleman):
        self.guc -= self.vurus
        eleman.darbe(self.vurus)
        print(self.isim,"-",eleman.isim,"e vurdu")
        self.Ozet()
        

    def savunmaYap(self,darbe):
        self.saglik -= (darbe - self.savunma)
        print(self.isim,"Savunma Yaptı")
        self.Ozet()

    def calistir(self,func):
        return func()

    def Ozet(self):
        print("-"*20)
        print(self.isim)
        print("güç = ",self.guc)
        print("saglik = ",self.saglik)
        print("vurus = ",self.vurus)
        print("savunma = ",self.savunma)
        print("-"*20)

    def darbe(self,vurus):
        self.saglik -= vurus
        print(self.isim,"darbe aldı")
        self.Ozet()

class DeadPool(MarverHero):
    def __init__(self):
        super(DeadPool,self).__init__(200,1000,100,50,"DeadPool")
    
    def yetenek(self):
        self.saglik = 1000

class Hulk(MarverHero):
    def __init__(self):
        super(Hulk,self).__init__(300,800,300,100,"Hulk")

    def yetenek(self):
        self.guc = 500


class IronMan(MarverHero):
    def __init__(self):
        super(IronMan,self).__init__(200,500,200,150,"IronMan")

    def yetenek(self):
        self.guc = 500    
