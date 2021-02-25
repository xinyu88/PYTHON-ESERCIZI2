'''
ES 8 
Crea una classe Quadrato con l'attributo lato e i metodi per il calcolo del perimetro e dell'area.
'''
class Quadrato :
    def __init__(self, lato): 
        self.lato = lato
        
    def calc_perimeter(self): 
        perimeter = self.lato * 4
        print("il perimetro è di", perimeter)

    def calc_area(self): 
        area = self.lato **2
        print("l'area è di", area)
        
f = Quadrato(8)
f.calc_perimeter()
f.calc_area()
