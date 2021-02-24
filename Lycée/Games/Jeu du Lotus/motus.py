"""Programme Motus - NSI - Noé Daniel"""

from random import *


gagne = False

def importation_mots():
    fichier = open("Liste_mots.txt", "r")
    contenu = fichier.read()
    contenu = contenu.split("-")
    fichier.close()
    return contenu

liste_mots = importation_mots()
mot_choisi = choice(liste_mots)
mot_choisi.lower()
print("ADMIN >>> Le mot aléatoire est :", mot_choisi)

def proposition(liste_mots, essais):

    verification = False
    while verification == False:
        proposition = str(input("Entrez un mot de 7 lettres."))
        proposition.lower()
        if len(proposition) == 7:
            verification = True
        else:
            print("Veuillez entrer un mot de 7 lettres.")

    liste_bonne_combinaison = ""

    if proposition == mot_choisi:
        print("Vous avez gagné avec {} essai(s)!".format(essais))
        return True

    else:
        for lettre in proposition:
            if lettre in mot_choisi:
                liste_bonne_combinaison = liste_bonne_combinaison + "< " + lettre + " >"
            else:
                liste_bonne_combinaison = liste_bonne_combinaison + "< * >"
        print("Voici la liste des similitues :", liste_bonne_combinaison)
        return False

essais = 0

while gagne == False:

    essais += 1
    gagne = proposition(liste_mots, essais)

    if gagne == False:
        reessayer = str(input("Voule-vous reessayer une combinaison ? oui/non ?"))
        if reessayer == "non":
            break

