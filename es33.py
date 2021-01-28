#Es 33 In un laboratorio di analisi i pazienti sono sottoposti ad un esame specialistico
#(utilizza la struttura di coda per memorizzare i nomi dei pazienti) : scrivi il programma che 
#consenta di registrare i nomi dei pazienti che man mano arrivano. Visualizza poi il nome del paziente 
#che deve essere sottoposto all'esame perchè il primo della coda in attesa.

pazienti = []
print("inserisci -1 per terminare")
while True : 
    nome_paziente = input("inserisci nome paziente ")
    if nome_paziente == "-1" : 
        break 
    else : 
        pazienti.append(nome_paziente)
print("i pazienti sono : ", pazienti) 

print("il primo paziente è", pazienti.pop(0)) #il primo paziente della coda
#oppure fare con indice, pazienti[0]
for p in pazienti : 
    print("il prossimo paziente è", p)
