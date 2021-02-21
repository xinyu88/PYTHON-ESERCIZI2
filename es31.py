'''
Es 31 pag 191
Un'azienda vende prodotti in tutta italia e la rete di vendita è suddivisa in quattro zone: Nord, Centro, Sud, Isole). Dopo aver acquisito in 
un array il fatturato nelle quattro zone, calcola : 
-Totale del fatturato
-Valori in percentuale delle vendite nelle quattro zone rispetto al totale.
'''
zone = ["Nord", "Centro", "Sud", "Isole"]

d = {}
for e in range(len(zone)) : 
    print("Zona", zone[e])
    fatturato = int(input("inserisci il fatturato : "))
    d[zone[e]]= fatturato
print(d)

totale = sum(d.values())
print("Il totale del fatturato è", totale)
print("ecco i valori in percentuale delle vendite nelle quattro zone rispetto al totale")
for val in d.values():
    calcolo = round(val * 100 / totale)
    print( calcolo, end="% " )

