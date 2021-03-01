'''
Descrivi la classe Quadrato del Problema 8 una nuova classe Rettangolo
aggiungendo un secondo lato per l'altezza e scrivendo i metodi per il calcolo 
del perimetro e dell'area.
'''

class Quadrato :
    def __init__(self, lato): 
        self.lato = lato
        
    def calc_perimetro(self): 
        perimetero = self.lato * 4
        print("il perimetro è di", perimetero)

    def calc_area(self): 
        area = self.lato **2
        print("l'area è di", area)

class Rettangolo(Quadrato):
    def __init__(self, lato, lato_h):
        super().__init__(lato)
        self.lato_h = lato_h
    
    def perimetro(self): 
        print("il perimetro del rettangolo è", 2 * (self.lato + self.lato_h))
        
    def area(self):
        print("l'area del rettangolo è", self.lato * self.lato_h  )

r = Rettangolo(2, 8)
r.perimetro()
r.area()
