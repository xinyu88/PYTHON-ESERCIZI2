'''
esercizio 34 pag 191 
Le prenotazioni per la partecipazione a un convegno sono memorizzati secondo l'ordine di arrivo 
(suggerimento utilizza una struttura di coda per memorizzare i dati dei partecipanti). 
Scrivi un programma che comprenda due funzionalità: 
- operazione per registrare i dati dei partecipanti.
- L'operazione per visualizzare i nomi dei partecipanti a cui si deve inviare una lettera di conferma: si tratta dei nomi dell'elenco,
eliminando quelli ai quali la lettera è già stata inviata e che sono registrati in un apposito elenco. La funzione che produce l'elenco deve anche aggiornare 
l'elenco dei partecipanti ai quali è già stata inviata la lettera.
'''
partecipanti = []
ricevuti = []
non_ricevuti = []
dizionario = []

#chiedo i nomi dei partecipanti
print("scrivi 1 per terminare")
while True : 
    nome = input("inserisci il nome del partecipante :  ").capitalize()
    if nome == "1" : 
        break 
    else : 
        partecipanti.append(nome)
        
#chiedo i dati dei partecipanti 
for n in partecipanti: 
    print(n, "inserisci i tuoi dati : ")
    eta = int(input("eta = "))
    d = {
        'nome': n,
        'eta': eta}
    dizionario.append(d)
print("ecco i dati dei partecpanti", dizionario) #visualizzo i dati dei songoli partecipanti 

#chiedo se hanno ricevuto o no la lettera 
for n in partecipanti : 
    print(n, "hai ricevuto la lettera ? ")
    r = input("si o no ? ").lower()
    if r == "si":
        ricevuti.append(n)
    else : 
        non_ricevuti.append(n)
print("si deve ancora inviare la lettera alle seguenti persone ", non_ricevuti)

