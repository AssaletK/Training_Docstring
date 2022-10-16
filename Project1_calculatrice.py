#!/usr/bin/python3

#Demander un premier nombre a l'utilisateur
#Demander un deuxieme nombre a l'utilisateur
#Additionner ces deux nombres
#Afficher le resultat

nombre1 = input("Entrer un premier nombre: ")
nombre1 = int(nombre1)
nombre2 = input("Entrer un deuxieme nombre; ")
nombre2 = int(nombre2)

resultat = nombre1 + nombre2

print(f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {resultat}")