#Crea un programma che scriva la differenza di due numeri a e b se il loro prodotto è maggiore di 10,
#oppure la loro somma se il prodotto è minore o uguale a 10.
#Esegui poi il programma con diverse coppie di valori per a e b: (-5, 2),(5, -5), (10, 2), (-4, -5), (5, 4), (-3, -2).

a = int(input("inserisci un numero a : "))
b = int(input("inserisci un numero b : "))
prodotto = a * b 

if prodotto > 10 : 
    print("il prodotto di", a, "e", b, "ovvero", a * b, "è maggiore di 10, allora la differenza di", a, "-", b, "è", a-b)
elif prodotto == 10 : 
    print("il prodotto di", a, "e", b, "ovvero",  a * b, "è uguale a 10, allora la somma di", a, " + ", b, "è", a+b)
else : 
    print("il prodotto di", a, "e", b, "ovvero", a * b, "è minore di 10, allora la somma di", a, " + ", b, "è", a+b)
    