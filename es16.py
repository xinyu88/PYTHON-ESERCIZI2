#ES 16 Risolvi il problema precedente(es15) partendo da due liste che generano un dizionario con 
#la nazione come chiave e la capitale come valore. Successivamente interroga il dizionario per 
#visualizzare la capitale di una nazione 

nazioni = ["Italia", "Inghilterra", "Francia", "Cina", "Russia", "Germania", "Giappone"]
capitali = ["Roma", "Londra", "Parigi", "Pechino", "Mosca", "Berlino", "Tokyo", "" ]
d = { } 

for n in range(len(nazioni)) : 
    d[nazioni[n]] = capitali[n]  

print("Di quale nazione vuoi saperne la capitale ? ", nazioni)
risposta = input("nazione = ").capitalize()

if risposta in nazioni :       
    print("la capitale è", d[risposta]) #d[chiave] trovo il valore della chiave(capitale)
else :  
    print("la nazione inserita non compare nell'elenco")