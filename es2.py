#SCRIVI UN PROGRAMMA CHE DATA IN INGRESSO UNA LISTA A CONTENENTE n PAROLE RESTISTUISCA 
# IN OUTPUT UNA LISTA B CHE RAPPRESENTANO LE LUNGHEZZE DELLE PAROLE CONTENUTE IN A 
indice = 0
ListaA = [] 
ListaB = []
print("inserisci 1 se hai terminato")

while True : 
    risposta = input("inserisci delle parole per la listaA")
    
    if risposta == "1" : 
        break 
    else : 
        ListaA.append(risposta)

print("ecco la lista", ListaA)

for parole in ListaA : 
    l = len(ListaA[indice])
    ListaB.append(l)
    indice +=1

print("ecco le lunchezze delle parole",ListaB)



