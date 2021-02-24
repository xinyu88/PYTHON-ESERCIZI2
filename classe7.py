'''
ES 7 
Elenca proprietà e metodi della classe Motociclo
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
def main(): 
    name = input("Nome del motociclo: ")
    color = input("Colore del motociclo: ")
    speed = int(input("Velocità del motociclo: "))
    m = Motociclo(name, color, speed)
    m.info()
main()