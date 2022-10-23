#!/usr/bin/python3

#Demander un premier nombre a l'utilisateur
#Demander un deuxieme nombre a l'utilisateur
#Additionner ces deux nombres
#Afficher le resultat

tentative = 0

while tentative >= 0:

    nombre1 = input("Entrer un premier nombre: ")
    nombre2 = input("Entrer un deuxieme nombre: ")

    if nombre1.isdigit() and nombre2.isdigit():
        nombre1 = int(nombre1)
        nombre2 = int(nombre2)
        print(f"Le résultat de l'addition de {nombre1} avec {nombre2} est égal à {nombre1 + nombre2}")
        break
    else:
        print("Veuillez entrer deux nombres valides")
    tentative += 1