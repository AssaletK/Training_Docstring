#Deux Joueurs : Utilisateur et enemi (l'ordinateur) avec 50 points nombres de depart
#JOUEUR_UTILISATEUR a 3 potion a utiliser; JOUEUR_ENEMI n'a pas de potion
#DEMANDER à l'utilisateur s'il attaque (1) ou prend une potion (2)
#SI (1) JOUEUR_UTILISATEUR perd entre 5 et 15 de ses points; JOUEUR_ENEMI perd entre 5 et 10 de ses points
#SI (2) JOUEUR_UTILISATEUR gagne entre 15 et 50 sur ses points et perd entre 5 et 15 sur ses points

import random

nombre_point_utilisateur, nombre_point_ennemi = 50, 50
choix = (1, 2)
potion_restante = 3
separateur = "_" * 50

while choix:
    
    choix_utilisateur = input("Souhaitez vous attaquer (1) ou prendre une potion (2) ? ")
    
    if not (choix_utilisateur.isdigit() and (choix_utilisateur == "1" or choix_utilisateur == "2")):
        continue
    else:
        choix_utilisateur = int(choix_utilisateur)
        points_infliges_par_utilisateur = random.randint(5, 10)
        points_infliges_par_ennemi = random.randint(5, 15)
        
        
        if choix_utilisateur == 1:
            nombre_point_ennemi = nombre_point_ennemi - points_infliges_par_utilisateur
            print(f"Vous avez infligé {points_infliges_par_utilisateur} points de dégats à l'ennemi.")
            
            if nombre_point_ennemi <= 0:
                print("Tu as gagné.\nFin du jeu.")
                break
            else:
                nombre_point_utilisateur = nombre_point_utilisateur - points_infliges_par_ennemi
                if nombre_point_utilisateur <= 0:
                    print(f"L'ennemi vous a infligé {points_infliges_par_ennemi} points de dégats.")
                    print("Tu as perdu.\nFin du jeu.")
                    break
                else:
                    print(f"L'ennemi vous a infligé {points_infliges_par_ennemi} points de dégats.")
            
                    print(f"Il vous reste {nombre_point_utilisateur} points de vie.")
                    print(f"Il reste {nombre_point_ennemi} points de vie à l'ennemi.")
                    print(f"{separateur}\n")
        elif choix_utilisateur == 2:
            
            while potion_restante > 0:
                potion_restante -= 1
                print(f"Vous passez votre tour...Il vous reste {potion_restante} potion(s).")
                
                points_potion = random.randint(15, 50)
                nombre_point_utilisateur = nombre_point_utilisateur + points_potion - points_infliges_par_ennemi
                
                if nombre_point_utilisateur <= 0:
                    print(f"L'ennemi vous a infligé {points_infliges_par_ennemi} points de dégats.")
                    print("Tu as perdu.\nFin du jeu.")
                    break
                else:
                    print(f"L'ennemi vous a infligé {points_infliges_par_ennemi} points de dégats.")
            
                    print(f"Il vous reste {nombre_point_utilisateur} points de vie.")
                    print(f"Il reste {nombre_point_ennemi} points de vie à l'ennemi.")
                    break
                break
            print(f"{separateur}\n")
                