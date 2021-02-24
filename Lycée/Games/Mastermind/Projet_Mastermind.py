"""Version 1.O Mastermind by Noé Daniel"""
"""Cette version ne contient aucune intégration graphique, ni de modules externes"""
"""Fait pour le cours de NSI - 21/12/2019"""

#Importation du module random.
from random import *

#Initialisation de la variable "gagne" indispensable à la boucle infinie
gagne = False

#Fonction de géneration aléatoire de la liste cachée.
def generer():
    L = []          #On initialise la liste interne à la fonction qui contient la combinaison.
    for i in range(4):          #Boucle for permettant de génerer 4 fois une valeur.
        L.append(randint(1, 5))     #On ajoute à la liste un entier entre 1 et 5.
    return L            #On retourne la liste.

liste_hide = generer()      #On fait appel à la fonction pour génerer la liste.


#Initialisation de la liste joueur.
def liste_joueur():
    liste_joueur = []       #On initialise la liste "entry"

    for i in range(4):      #On va répeter les instructions 4 fois.
        verification = False        #On crée notre variable à "l'infini"

        while verification == False:        #Tant que la vérification de la valeur n'est pas bonne.
            ajout = int(input("Donnez un chiffre entree 1 et 5 en {}e position".format(i + 1)))     #On demande une valeur entière à l'utilisateur.
            if ajout >= 0 and ajout <= 5:       #Si elle est comprise entre 1 et 5,
                liste_joueur.append(ajout)      #On l'ajoute à la liste de combinaisons
                print("Vous avez saisi l'entrée : {}".format(ajout))
                verification = True             #La vérification est vérifiée, la boucle à l'infini s'arrête
            else:   #Sinon,
                print("Merci d'entrer un chiffre entre 1 et 5")     #On indique l'erreur

    return liste_joueur     #On renvoie la liste du joueur.


#Traitement des entrées des listes :
def partie(liste_hide, liste_joueur, parties):      #Fonction centrale qui demande les 3 paramètres...
    bonne_combinaisons = 0          #Initialisation Compteur de chiffres en commun

    if liste_joueur == liste_hide:          #Si la liste choisie est la bonne, on renvoie...
        print("Bravo ! Vous avez gagné !")
        print("Nombre d'essais : {}".format(parties))
        return True     #On renvoie True.

    else:       #Si la liste n'est pas la même...
        for i in range(len(liste_hide)):        #On prend un curseur "i" qui parcourt les listes
            if liste_hide[i] == liste_joueur[i]:    #Dès qu'un chiffre est commun à la bonne position
                bonne_combinaisons += 1     #Le compteur s'incrémente.
        print("Vous avez {} chiffre(s) bien placé(s)".format(bonne_combinaisons))   #On renvoie le nombre de bons chiffres
        return False        #Mais on renvoie False pour que le programme continue.


essais = 0          #Initialisation de la variable du nombre de tentaives réalisées

#Boucle infinie qui contient toutes les fonctions initialisées.

while gagne == False:       #Tant que je joueur n'a pas gagné, on repète les instructions
    liste_pl = liste_joueur()           #On demande à chaque tour la liste du joueur en appelant la fonction.
    print("                                ")
    print("Votre combinaison est :", liste_pl)      #On affiche la liste que le joueur a choisi

    #Mode Admin - Verif
    if admin_on == True:            #Si le mode admin est activé,...
        print("                                ")
        print("Admin :", liste_hide)            #On renvoie la liste qui a été génerée aléatoirement.

    gagne = partie(liste_hide, liste_pl, essais)        #On vérifie si la liste du joueur est compatible avec celle génerée...
                                                        #Si c'est le cas la fonction renvoie True, le jeu s'arrête sinon, on continue.
    essais += 1                                         #On ajoute une tentative.

    if gagne == True:              #Si le joueur a gagné, on arrête la boucle instantanément et on n'execute pas ce qui est en dessous.
        break           #Break stoppe la boucle While

    #On demande à l'utilisateur si il veut continuer de faire des combinaisons.
    arreter = str(input("Voule-vous essayer une nouvelle combinaison ou arreter le jeu ? c (=continuer)/a (=arrêter) ?"))
    if arreter == "a":
        break

