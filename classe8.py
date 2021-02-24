'''
ES 8 
Crea una classe Quadrato con l'attributo lato e i metodi per il calcolo del perimetro e dell'area.
'''
class Quadrato :
    def __init__(self, lato): 
        self.lato = lato
        
    def perimeter(self): 
        perimeter = self.lato * 4
        print("il perimetro è di", perimeter)

    def area(self): 
        area = self.lato **2
        print("l'area è di", area)
        
f = Quadrato(8)
f.perimeter()
f.area()
