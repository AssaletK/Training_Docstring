import sys

liste_de_course = []
choix = " "
separator = "_" * 70

while choix:
    print("Choisissez parmis les 5 options suivantes : ")
    print("1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme")
    choix = input("Votre Choix : ")
    
    if not (choix.isdigit() and "1" <= choix <= "5"):
        print("Choisissez parmis les 5 options suivantes : ")
        print("1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme")
        choix = input("Votre Choix : ")
        print(f"{separator}\n")
        
    else:
        if choix == "1":
            element = input("Entrer le nom d'un élément à ajouter à la liste de courses : ")
            liste_de_course.append(element)
            print(f"L'élément {element} a bien été ajouté à la liste")
            print(f"{separator}\n")
        
        elif choix == "2":
            element_retire = input("Entrer le nom d'un élément à rétirer à la liste de courses : ")
            if element_retire not in liste_de_course:
                print(f"L'élément {element_retire} n'est pas dans la liste.")
            
            else:   
                liste_de_course.remove(element_retire)
                print(f"L'élément {element_retire} a bien été rétiré à la liste.")
            print(f"{separator}\n")
        
        elif choix == "3":
            if liste_de_course:
                for i, element in enumerate(liste_de_course, 1):
                    print(f"{i}. {element}")
            
            else:
                print("La liste ne contient pas d'élément.")
            print(f"{separator}\n")
        
        elif choix == "4":
            while liste_de_course:
                for element in liste_de_course:
                   liste_de_course.remove(element)
            print("La liste a été vidée de son contenu")
            print(f"{separator}\n")
        
        else:
            sys.exit("A bientot")
            