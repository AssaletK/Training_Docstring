#DEMANDER un mot de passe de 8 caractères au moins a l'utilisateur
#SI la LONGUEUR du mot de passe est égale à 0 AFFICHER mdp_trop_court en MAJUSCULE
#SI la LONGUEUR du mot de passe entré est plus petite que 8 AFFICHER mdp_trop_court avec une majuscule sur la première lettre
#SI le mot de passe ne contient que des nombres AFFICHER "Votre mot de passe ne contient que des nombres."
#AFFICHER la phrase "Inscription terminée." si le mot de passe est valide.

mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe est trop court."

if len(mdp) == 0:
    print(mdp_trop_court.upper())
elif len(mdp) < 8:
    mdp_trop_court = mdp_trop_court.replace("votre", "Votre")
    if mdp.isdigit() is True:
        print("Votre mot de passe ne contient que des nombres.")
    else:
        print(mdp_trop_court)
else:
   if mdp.isdigit() is True:
       print("Votre mot de passe ne contient que des nombres.")
   else:
       print("Inscription terminée.")
