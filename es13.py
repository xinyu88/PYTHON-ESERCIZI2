#Verifica se un numero è pari o dispari (un numero è pari quando il resto della divisione intera per 2 è uguale a 0)

numero = int(input("inserisci un numero a piacere, per verificare se è pari o dispari = "))

if numero % 2 == 0 :
    print("il numero inserito", numero, "è pari")
else : 
    print("il numero inserito", numero, "è dispari")
