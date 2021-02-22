'''
Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra
'''
class Atleta():
    def __init__(self, name, age, weight, visitaMedica): 
        self.name = name
        self.age = age
        self.weight = weight
        self.visitaMedica = visitaMedica
    
    def info(self): 
        print(self.name, self.age, self.weight)
        if self.visitaMedica == True :
            print(self.name, "ha ricevuto la visita medica")
        else:
            print(self.name,"non ha ricevuto la visita medica")
    def team(self, name_team): 
        self.name_team = name_team
        print(self.name, self.age, self.weight, self.name_team)

a1 = Atleta("Alice", 19, "49 kg", True)
a1.team("Inter")
a2 = Atleta("Michele", 34, "78 kg", False)
a2.team("Reggiana")
