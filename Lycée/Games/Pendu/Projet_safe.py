#Programme dans le but du TP de NSI - Aucune copie n'est tolérée !

from random import *
from importation_mots import *


ensemble_lettres = "abcdefghijklmnopqrstuvwxyz"
dictionnaire = importation_8mots()
graphismes = [
    """
    ---------
     |     |
     |
     |
     |
     |
     |""",
    """
    ---------
    |     |
    |     o
    |
    |
    |
    |""",
    """
    ---------
    |     |
    |     O
    |    -+-
    |
    |
    |""",
    """
    ---------
    |     |
    |     O
    |   /-+-
    |
    |
    |""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |
    |
    |""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |    |
    |
    |""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |    | |
    |
    |"""]

fautes_max = len(graphismes) - 1


def lire_lettre(propositions):
    #Demande une lettre à l'utilisateur en s'assurant qu'elle n'a pas déjà
    #été proposée, puis ajoute cette lettre à la liste des lettres déjà
    #proposées.

    while True:                                 #Condition qui affirme que les chances ne sont pass épuisées sinon -> "return False"
        lettre = input("Entrez une proposition de lettre : ")       #On demande le choix de l'utilisateur

        if lettre in propositions:                                  #1ere Condition : Grace à la liste regroupant les entrée on peut controler les doublons
            print("Cette lettre a déjà été proposée.")
        elif lettre not in ensemble_lettres or len(lettre) != 1:    #2eme Condition : On regarde si la lettre est bien en majuscule et qu'il n'y en ait pas plusieurs
            print("Veuillez réessayez avec uniquement 1 lettre en majuscule.")
            print("Entrée donnée : {}".format(lettre))
        else:                                                       #Sinon on continue !
            break;

    propositions.append(lettre)                                     #Permet d'ajouter grâce à une "class" la proprosition dans la liste
    return lettre                                                   #On retourne la variable au programme


def mot_avec_tirets(mot, propositions):

    m = ''
    for lettre in mot:                      #Pour la lettre dans le mot :
        if lettre in propositions:              # Si elle est dans les propositions
            m = m + lettre                      # On l'ajoute
        else:                               #Sinon :
            m = m + '-'                         #On met un tiret
    return m


def partie():       #Initialisation de la partie ! Si gagné la fonction renverra l'information "True" sinon elle renverra "False"

    fautes = 0      #Variable permettant de controler le nombre d'erreurs
    mot = dictionnaire[randrange(len(dictionnaire))]    #Choix aléatoire du mot
    propositions = []                                   #Création d'une liste vierge stockant toutes les entrées

    print(graphismes[fautes])                           #On afiche le graphisme correspondant au nombre de fautes

    while True:                                         #Condition tant que les chances ne soient pas épuisées
        print("Lettres déjà proposées : {}".format(propositions))
        print("Réponse courante :", mot_avec_tirets(mot, propositions))

        lettre = lire_lettre(propositions)

        if lettre in mot:
            if mot_avec_tirets(mot, propositions) == mot:
                print("Bravo, vous avez gagné. Le mot en question était : {} ".format(mot))
                print("Nombre de fautes :", fautes)
                return True
        else:
            fautes = fautes + 1
            print(graphismes[fautes])
            if fautes >= fautes_max:
                print("Vous avez échoué, le mot en question était : {}".format(mot))
                return False


# C'est ici que commence l'éxecution du programme, au-dessus : fonctions !
print("Bienvenue dans le jeu du pendu développé par Noé Daniel")

games = 0           #"Reset" des variables
victoires = 0       #"Reset" des variables

while True:         #Tant que les chances ne sont pas nulles

    games += 1         #On rajoute une partie
    if partie():
        victoires += 1      #On rajoute une victoire

    while True:

        again_game = input("Voulez-vous continuer de jouer ? o = oui, n = non : ")
        if (again_game == 'o') or (again_game == 'n'):
            break;

    if again_game == 'n':
        break;

print("Nombre de parties réalisées {}".format(games))
print("Nombre de victoires {}".format(victoires))
print("Programme développé intégralement par Noé Daniel - DCMA (Noé Daniel / AezioxDev")