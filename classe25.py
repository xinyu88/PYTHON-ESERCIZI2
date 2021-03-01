'''
ES 25 Crea la classe Triangolo, la classe derivata Triangoloisoscele e, da quest'ultima, la classe derivata Triangoloequilatero
'''
class Triangolo: 
    def __init__(self, base, lato1, lato2):
        self.base = base
        self.lato1 = lato1 
        self.lato2 = lato2 
    def info(self): 
        print("la base :",  self.base)
        print("i lati :", self.lato1, self.lato2)

class Triangoloisoscele(Triangolo): 
    def __init__(self, base, lato1, lato2) :
        super().__init__(base, lato1, lato2)
        self.base = base
        self.lato1 = lato1
        self.lato2 = lato2 

    def info_isoscele(self): 
        print("il tringolo è isoscele")
        print("Base =", self.base, )
        print("lati =", self.lato1, self.lato2 )

class Triangoloequilatero(Triangoloisoscele): 
    def __init__ (self, base, lato1, lato2) : 
        super().__init__(base, lato1, lato2)

    def info_equilatero(self):
        print("Il triangolo è equilatero")
        print("Lati del triangolo =", self.base)

t_iso= Triangoloisoscele(1,2, 2)
t_iso.info_isoscele()
t_e = Triangoloequilatero(2, 2, 2)
t_e.info_equilatero()