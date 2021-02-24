'''
ES 5 
Elenca proprietà e metodi della classe Prodotto.
ES 6 
Definisci il metodo assegna prezzo della classe Prodotto.
'''
class Prodotto(): 
    def __init__(self, name, price): 
        self.name = name
        self.price = price
    def info(self): 
        print("Nome del prodotto è", self.name)

    def assegna_prezzo(self): 
        print("il prezzo di è", self.price, "€")
        
p = Prodotto("prodotto", 2)
p.info()
p.assegna_prezzo()


