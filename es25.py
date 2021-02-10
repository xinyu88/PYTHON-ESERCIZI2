''' 
I voti assegnati a 30 studenti di una classe in una prova di italiano sono memorizzati in un dizionatio 
che ha per chiave la matricola, mentre il valore associato è il voto.
Elenca i risultati in ordine crescente di voto e successivamente visualizza quali voti diversi tra loro 
sono stati assegnati, riducendo a uno i voti uguali.
'''
s = 0 # conto i studenti
#chiedo i voti ai studenti 
lista = {} 
for e in range(30) : 
    print("studente", s)
    voto = int(input("quanto hai preso?"))
    lista[s] = voto #studente come chiave e voto come valore
    s += 1 
print("ecco la lista con i loro voti", lista)

#elencare i risultati in ordine crescente di voto
ordine_crescente = sorted(lista.values())
print("Ecco in ordine crescente di voti", ordine_crescente)

for e in ordine_crescente :
    c = ordine_crescente.count(e)
    if c >= 2 :
        ordine_crescente.remove(e) #rimuovo a uno i voti uguali
        print("ecco la nuova lista", ordine_crescente) #in caso i voti siano uguali, rimuovere a uno.
