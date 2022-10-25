#Generer un nombre mistere
#Demander un nombre a l'utilisateur compris entre 0 et 100
#Si l'utilisateur ne rentre pas un nombre le jeu n'a pas encore commencer
#Afficher le nombre d'essais restants
#Afficher si le nombre entrer est plus grand, plus petit ou egal au nombre mystere
#Afficher terminer si plsu de vie

import random
import sys

nombre_mystere = random.randint(0, 10)
essais = 5

while essais > 0:
    nombre_entre = input("Devinez le nombre mystere : ")
    if not nombre_entre.isdigit():
        print("Veuillez entrer un nombre valide.")
        print(f"Il vous reste {essais} essais")
        continue
    else:
        nombre_entre = int(nombre_entre)
        essais -= 1
        if nombre_entre < nombre_mystere:
            print(f"Le nombre mystere est plus grand {nombre_entre}.")
            print(f"Il vous reste {essais}.")
        elif nombre_entre > nombre_mystere:
            print(f"Le nombre mystere est plus petit que {nombre_entre}.")
            print(f"Il vous reste {essais}.")
        else:    
            print(f"Felicitations vous avez gagner au {5 - essais}e essais.")
            sys.exit()
print(f"Desole! Le nombre mystere etait {nombre_mystere}")
print("La partie est terminée.")
        
