'''
ES 13 pag 189.
Acquisisci da tastiera un elenco di parole, memorizzandole in una lista, finchè l'utente segnala 
la fine dell'inserimento con un asterisco *. Visualizza alla fine il numero delle parole memorizzate.
Ordina alfabeticamente la lista delle parole e visualizzala, ordinata in modo crescente e decrescente.
'''
lista = []
print("Per terminare inserire : *")
while True :
    parola = input("inserisci la parola : ").lower()
    if parola == "*":
        break 
    else : 
        lista.append(parola)

print("le parole inserite sono", len(lista))

#ordino alfabeticamente le parole in modo crescente
lista.sort()
print("Ecco la lista ordinata in modo crescente delle parole", lista)
lista.reverse()
print("Ecco la lista ordinata in modo decrescente delle parole", lista)