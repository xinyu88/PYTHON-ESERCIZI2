'''
ES 21 Data la classe Motociclo creata nel Problema 7, deriva la classe Ciclomotore. Aggiungi le proprietà opportune e modifica il metodo 
che consente di visualizzare i valori dellle proprietà
'''

class Motociclo(): 
    def __init__(self, name, color, speed): 
        self.name = name
        self.color = color
        self.speed = speed 

    def info(self): 
        print("Nome :", self.name )
        print("Colore :", self.color)
        print("Velocità :", self.speed)

class Ciclomotore(Motociclo): 
    def __init__(self, name, color, speed, price):
        super().__init__(self, name, color, speed)
        self.price = price

    def info_c(self) : 
        super().info()
        print("Prezzo =", self.price)
        
def main(): 
    nome = input("Nome: ")
    colore = input("Colore: ")
    velocita = int(input("Velocità : "))
    prezzo = int(input("prezzo: "))
    c = Ciclomotore(nome, colore, velocita, prezzo)
    c.info_c()
main()
       
