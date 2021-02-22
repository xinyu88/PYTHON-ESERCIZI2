'''
Crea una classe Atleta per rappresentare le informazioni su un giocatore. 
La classe deve contenere un attributo booleano chiamato visitaMedica.
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
        else: #False  
            print(self.name,"non ha ricevuto la visita medica")
            
a1 = Atleta("Alice", 19, "49 kg", True)
a1.info()
a2 = Atleta("Michele", 34, "78 kg", False)
a2.info()
