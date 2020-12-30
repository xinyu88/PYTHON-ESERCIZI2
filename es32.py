#Implementa l'argoritmo per il calcolo della soluzione di un'equazione di primo grado a x + b = 0.
#Il processo risolitivo dipende dai valori assunti dai coefficienti a e b secondo la che segue.

import fractions # scrivere in frazione 

a = int(input("inserisci il valore di a : "))
b = int(input("inserisci il valore di b : "))

if a == 0 and b == 0 : 
    print("l'equazione", a, "x +", b, " = 0 è Indeterminata")
elif a == 0 and b != 0 : 
    print("l'equazione", a, "x +", b, " = 0 è Impossibile")
elif a != 0 and b == 0 : 
    print("l'equazione", a, "x +", b, " = 0 è x = 0")
else : 
    x = fractions.Fraction(- b, a) 
    print("l'equazione", a, "x +", b, " = 0", "risulta", x)
