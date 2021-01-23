#ES 15 Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista 
#(nazioni e la relativa capitale si trovano nella medesima posizione delle rispettive liste), 
#visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,segnando con un 
#messaggio di errore il caso in cui la nazione richiesta non sia compresa nell'elenco

nazioni = ["Italia", "Inghilterra", "Francia", "Cina", "Russia", "Germania", "Giappone", "Spagna"]
capitali = ["Roma", "Londra", "Parigi", "Pechino", "Mosca", "Berlino", "Tokyo", "" ]
print("Di quale nazione vuoi saperne la capitale ? ", nazioni)

risposta = input("nazione = ").capitalize()
if risposta in nazioni :           # IN = verificare se un valore è presente in una sequenza (elenco, intervallo, stringa)
    cap_nazione = (nazioni.index(risposta))
    c = capitali[cap_nazione]
    print(c)
else :  
    print("la nazione inserita non compare nel'elenco")
    