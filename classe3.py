'''
Aggiungi alla classe Atleta un metodo chaimato effettua_visita che ponga l'attributo vistaMedica uguale a True
'''

class Atleta(): #definisco la classe 
    def __init__(self, name, age, weight, visitaMedica): #inizializzazione attributi  self identifica la calsse stessa e consente al metodo di utilizzare gli attributi
        self.name = name
        self.age = age
        self.weight = weight
        self.visitaMedica = visitaMedica
    
    def info(self): 
        if self.visitaMedica == True :
            print(self.name, "ha ricevuto la visita medica")
        if self.visitaMedica == False: 
            print(self.name,"non ha ricevuto la visita medica")

    def team(self, name_team): 
        self.name_team = name_team
        print(self.name, self.age, self.weight, self.name_team)

    def effettua_visita(self, visitaMedica):
        self.visitaMedica = True

a1 = Atleta("Alice", 19, "49 kg", True)
a1.team("Inter")
a1.effettua_visita(False)
a1.info()
a2 = Atleta("Michele", 34, "78 kg", False)
a2.team("Reggiana")
a2.effettua_visita(True)
a2.info()
