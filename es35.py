#ES35 organizza con un dizionario i dati sui conti correnti bancari con un numero del conto e saldo.
#Fornito poi il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso 
#in cui il conto fornito non sia presente nella mappa 

d = {
    "001" : 32568,
    "002" : 12546,
    "003" : 46562189,
    "004" : 123898,
    "005" : 1478,
    "006" : 99542,
    "007" : 4578,
    "008" : 78991
 }
print("i conti sono ", d.keys())
conto = input("inserisci il numero del conto di cui vuoi saperne il saldo")

if conto in d :  
    print("il saldo è", d[conto]) 
else : 
    print("Ci dispiace, il conto non è presente")
