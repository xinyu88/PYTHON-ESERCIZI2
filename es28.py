''' 
I nomi della città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseritida tastiera 
e memorizzati in un dizionario, dove la CAP è la chiave. Fornito poi da tastiera il nome di una città, 
costruisci un programma che visualizzi il suo CAP oppure un messaggio nel caso la città non sia compresa 
nell'elenco. Analogamente, fornendo il CAP restituisce il nome della città oppure un messaggio di errore
'''
dcitta = {}
dcap = {}

print("inserisci 1 per terminare")
while True : 
    cap = int(input("inserisci il CAP : "))
    citta = input("inserisci il nome della citta : ")
    if cap == 1 or citta == "1" : 
        break 
    else : 
        dcap[cap] = citta #CAP è la chiave
        dcitta[citta] = cap #citta è la chiave
print("Dato il nome della città o il CAP, vuoi sapere la città o il CAP ? ")
print("inserire 1. se vuoi sapere il nome della città corrispondente al CAP ")
print("inserire 2. se vuoi sapere il cap")
r = int(input("risposta = "))
if r == 1 : 
    r_cap = int(input("inserisci il CAP : "))
    if r_cap in dcap : 
        print("la città avene come CAP", r_cap, "è", dcap[r_cap])
    else : 
        print("Nessuna città avente CAP", r_cap)
else : 
    nome_citta = input("inserisci il nome della città di cui vuoi conoscere il CAP : ")
    if nome_citta in dcitta : 
        print("Il CAP di", nome_citta, "è", dcitta[nome_citta])
    else : 
        print("Nessuna CAP della città", nome_citta)
