'''
ES 14 pag 189.
Organizza in una struttura dati i valori degli occupati negli ultimi dieci anni. Utilizza un dizionario, assegnando 
il ruolo di chiave all'anno. Inserisci i dati da tastiera e memorizzari nel continentore. Calcola poi il valore medio dei dieci anni e 
visualizzane il risultato 
'''
d = {}
for v in range(1, 3) :
    print("Anno", v) 
    dato = int(input("Numero degli occupati :"))
    d["anno",v] = dato
print(d)
media = sum(d.values())/len(d)
print("Ecco la media", float(media))


