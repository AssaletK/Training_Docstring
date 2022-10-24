import sys

liste = []
choix = " "

while choix:
    print("Choisissez parmis les 5 options suivantes : ")
    print("1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme")
    choix = input("Votre Choix : ")
    
    if choix < "1" or choix > "5":
        print("Choisissez parmis les 5 options suivantes : ")
        print("1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme")
        choix = input("Votre Choix : ")
    elif not choix.isdigit():
        print("Choisissez parmis les 5 options suivantes : ")
        print("1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme")
        choix = input("Votre Choix : ")
    else:
        if choix == "1":
            element = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
            liste.append(element)
            print(f"L'élément {element} a bien été ajouté à la liste")
            print("_______________________________________________________________________________________________________\n")
        elif choix == "2":
            element_retire = input("Entrer le nom d'un élément à rétirer à la liste de courses : ")
            if element_retire not in liste:
                print(f"L'élément {element_retire} n'est pas dans la liste.")
            else:   
                liste.remove(element_retire)
                print(f"L'élément {element_retire} a bien été rétiré à la liste.")
            print("_______________________________________________________________________________________________________\n")
        elif choix == "3":
            if liste:
                for i, element in enumerate(liste):
                    print(f"{i + 1}. {element}")
            else:
                print("La liste ne contient pas d'élément.")
            print("_______________________________________________________________________________________________________\n")
        elif choix == "4":
            while liste:
                for element in liste:
                   liste.remove(element)
            print("La liste a été vidée de son contenu")
            print("_______________________________________________________________________________________________________\n")
        else:
            sys.exit()