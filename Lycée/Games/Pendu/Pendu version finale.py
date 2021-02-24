#Programme dans le but du TP de NSI - Aucune copie n'est tolérée !
from tkinter import *
from random import *

from importation_mots import *
from importation_graphique import *

#Interface graphique

page_lancement()

ensemble_lettres = "abcdefghijklmnopqrstuvwxyz"     #Ensemble de lettres.
dictionnaire = importation_8mots()
graphismes = [
    """
    ---------
     |     |
     |
     |
     |
     |
     |
     ---------""",
    """
    ---------
    |     |
    |     o
    |
    |
    |
    |
    ---------""",
    """
    ---------
    |     |
    |     O
    |    -+-
    |
    |
    |
    ---------""",
    """
    ---------
    |     |
    |     O
    |   /-+-
    |
    |
    |
    ---------""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |
    |
    |
    ---------""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |    |
    |
    |
    ---------""",
    """
    ---------
    |     |
    |     O
    |   /-+-/
    |    | |
    |
    |---------"""]

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


def mot_avec_etoiles(mot, propositions):        #Se réalise à chaque proposition du joueur.

    m = ''                                  #On initialise la chaine de caractère cachée
    for lettre in mot:                      #On prend chaque lettre du mot a trouver,
        if lettre in propositions:              # Si elle a été proposée, on ne la cache pas
            m = m + lettre                      # On ne la cache pas.
        else:                               #Sinon :
            m = m + '*'                         #On met une étoile à sa place.
    return m                                #On retourne au "main" script la chaine cachée


def partie():       #Initialisation de la partie ! Si gagné la fonction renverra l'information "True" sinon elle renverra "False"

    fautes = 0      #Variable permettant de controler le nombre d'erreurs
    mot = dictionnaire[randrange(len(dictionnaire))]    #Choix aléatoire du mot
    propositions = []                                   #Création d'une liste vierge stockant toutes les entrées

    print(graphismes[fautes])                           #On afiche le graphisme correspondant au nombre de fautes

    while True:                                         #Condition tant que les chances ne soient pas épuisées
        print("Lettres déjà proposées : {}".format(propositions))
        print("Réponse actuellle :", mot_avec_etoiles(mot, propositions))
        print("---------------------------------------------------")

        lettre = lire_lettre(propositions)

        if lettre in mot:
            if mot_avec_etoiles(mot, propositions) == mot:
                print("Bravo, vous avez gagné. Le mot en question était : {} ".format(mot))
                print("Nombre de fautes :", fautes)
                return True
        else:
            fautes = fautes + 1
            print(graphismes[fautes])
            if fautes >= fautes_max:
                print("Vous avez échoué, le mot en question était : {}".format(mot))
                return False


# C'est ici que commence l'éxecution du programme, au-dessus on a juste les fonctions !
print("Bienvenue dans le jeu du pendu développé par Noé Daniel")

nb_parties = 0           #Initialisation du nombre de parties
victoires = 0       #Initialisation du nombre de victoires

while True:         #Tant que les chances ne sont pas nulles

    nb_parties += 1         #On rajoute une partie
    if partie():
        victoires += 1      #On rajoute une victoire

    while True:

        again_game = str(input("Voulez-vous continuer de jouer ? oui ou non ?"))
        if (again_game == 'o') or (again_game == 'n'):
            break;

    if again_game == 'n':
        break;

print("Programme développé intégralement par Noé Daniel - DCMA (Noé Daniel)")