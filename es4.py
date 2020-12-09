# SCRIVI UN PROGRAMMA CHE A SCELTA DELL'UTENTE CALCOLI L'AREA DI UN QUADRATO 
#RETTANGOLO TRIANGOLO E CERCHIO 

import math #utilizzo pigreco per il calcolo dell'area del cerchio
lista = ["QUADRATO", "RETTANGOLO", "TRIANGOLO", "CERCHIO"]

while True : 
    print("scrivi 1 per terminare")
    print("scegli uno tra questi di cui vuoi calcolare l'area", lista)
    risposta = input() 
    
    if risposta == "1" :
        break 
                                                                                                                                                                                 
    elif risposta == "quadrato" or risposta == "QUADRATO"  :  #(vanno bene anche upper() o lower())
        lato = int(input("inserisci il valore del lato del quadrato"))
        print(lato)
        print("l'area del quadrato è", lato **2)
        
    elif risposta == "rettangolo" or risposta ==  "RETTANGOLO" :  
        b1 = int(input("inserisci il valore della base del rettangolo"))
        h1 = int(input("inserisci il valore dell'altezza del rettangolo"))
        print("l'area del rettangolo è", b * h)
        
    elif risposta == "triangolo" or risposta ==  "TRIANGOLO" :
        b2 = int(input("inserisci il valore della base del triangolo"))
        h2 = int(input("inserisci il valore dell'altezza del triangolo"))
        print("l'area del triangolo è", b2 * h2/2 )
        
    else :
        raggio = int(input("inserisci il valore del raggio della circonferenza"))
        area = int(raggio **2 * math.pi)
        print(area) #senza numeri decimali 












