#SCRIVI UN PROGRAMMA A CUI VIENE PASSATA UNA PAROLA E RICONOSCERE SE SI 
#TRATTA DI UN PALINDROMO(CHE SI LEGGONO UGUALI ANCHE AL CONTRATIO) OPPURE MENO.

print(" riconoscere se la parola si tratta di un palindromo")
print("per terminare scrivi 1")

while True : 
    print("scrivi la parola")
    risposta = input()
    parola = risposta[::-1] #utilizzo [::-1] per invertire la stringa 
    if risposta == "1" : 
        break 
    
    elif parola == risposta :
        print( parola + ": la parola passata è un palindromo!")
    else:
        print(parola + ": mi dispiace, la parola inserita NON è un palindromo...")













