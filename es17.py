#Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo il ruolo 
#di chiave e valore.Usa il nuovo diizonario per trovare il nome della nazione, noto il nome della 
#capitale
nazioni = ["Italia", "Inghilterra", "Francia", "Cina", "Russia", "Germania", "Giappone"]
capitali = ["Roma", "Londra", "Parigi", "Pechino", "Mosca", "Berlino", "Tokyo" ]
d = { } 

for c in range(len(capitali)) : 
    d[capitali[c]] = nazioni[c]  #assegno alla 

print("Di quale capitale vuoi saperne la nazione ? ", capitali)
risposta = input("capitale = ").capitalize()

if risposta in capitali : #
    print("la nazione è", d[risposta])
else : 
    print("la capitale non appare nell'elenco")