'''
Es 27 Organizza una rubrica con i nomi delle persone e i rispettivi numeri telefonici. Fornito poi il 
nome della persona, il programma visualizza il suo numero telefonico oppure un messaggio nel caso la
persona non sia presente nella rubrica
'''
rubrica = {
    'maria' : '241 854 4843',
    'ilaria' : '654 589 7714',
    'caterina': '154 656 7871',
    'marco' : '544 565 4878',
    'elena' : '264 679 4887',
}

print("Ecco la rubrica con i nomi", rubrica.keys())
print("Per terminare premere 1")
while True : 
    nome = input("inserisci il nome di cui vuoi conoscere il numero telefonico ").lower()
    if nome != "1":
        if nome in rubrica : 
            print("il numero telefonico di", nome, "è", rubrica[nome])
        else : 
            print("Spiacenti", nome, "non è presenta nella rubrica")
    else : 
        break 
