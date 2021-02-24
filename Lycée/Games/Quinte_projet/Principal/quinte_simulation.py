#TP - Quinte (SIMULATION) / Noé DANIEL

"""Attention ! Ce programme est un programme de simulation qui permet de choisir manuellement la liste gagnante"""
"""Le programme officiel est normalement joint avec celui-ci et détermine la liste gagnante aléatoirement"""

from tkinter import *
from random import *

#Initialisation des variables
liste_pari = []                                                                 #On initialise la liste des chevaux que va donner le joueur
"""On n'initialise pas la liste de tous les chevaux puisque ceux-ci vont etre choisis automatiquement par l'admin"""
liste_gagnante = []                                                             #On initialise la liste gagnante

def quinte():

    #Liste du parieur
    for i in range(0, 5):                                                                               #On demande 5 fois un cheval.
        pari = int(input("Entrez le cheval qui va arriver en {} eme/re position :".format(i + 1)))      #Interface de demande input()
        if pari in liste_pari or pari > 16 or pari < 0:                                                 #On vérifie que les valeurs sont bonnes et n'ont pass déja été rentrées
            print("Votre pari est incorrect")
            break                                                                                       #Si elles sont incorrectes, on break() la boucle
        liste_pari.append(pari)                                                                         #On ajoute les chevaux dans l'odre donné à la liste du joueur.
    print("Votre liste dans l'odre d'arrivée est la suivante :", liste_pari)

    #Choix de la liste gagnante.

    for i in range(0, 5):                                                                               #On va choisir 5 fois un cheval aléatoire.
        gagnant = int(input("Entrez le cheval qui va arriver en {}e position ! [MODE ADMIN]".format(i + 1)))
        print("Le {} er/ème cheval gagnant est le {}".format(i + 1, gagnant))                           #On affiche les résultats du tirage avec la position
        liste_gagnante.append(gagnant)                                                                  #On ajoute le cheval à la liste gagnante.
        print("----------------------------------------------------------------")
    print("Liste gagnante :", liste_gagnante)                                                           #On affiche la liste gagnante

    #Pour éviter des soucis de déletion on crée un tuple de la liste gagnante.
    #Ainsi les valeurs ne pourront pas être modifiées.
    tuple_gagnant = liste_gagnante
    tuple_gagnant = tuple(tuple_gagnant)


    print("                                                                    ")                       #Pour rendre l'affichage clair, on laisse des espaces

    #Le quinte ordre et désordre :
        #Initialisation des variables
    quinte_ordre = 0
    quinte_desordre = 0
        #Boucle for de 1 à 5 pour traiter les 5 chevaux des deux listes
    for i in range(0, 5):
        if liste_pari[i] == liste_gagnante[i] :                             #1ère condition, (QUINTE), si elle est bonne, on ajoute 1 au compteur n°1
            quinte_ordre += 1
        if liste_pari[i] in liste_gagnante:                                 #2ème condition, si elle est bonne, on ajoute 1 au compteur n°2
            quinte_desordre += 1

    #Les Bonus

    #Bonus 4:
        #Initialisation des variables
    bonus4 = 0
    liste_bonus4 = liste_gagnante                   #On crée une nouvelle liste de seulement 4 valeurs (les premières)
    del liste_bonus4[4]                             #On supprime le 5ème cheval car inutile
    print("Liste du bonus 4 :", liste_bonus4)
    for i in range(0, 4):
        if liste_pari[i] in liste_bonus4:           #Si le cheval [i] est dans la liste, alors la condition est vérifiée
            bonus4 += 1

    print("                                                                    ")

    #Bonus 3:
        #Initialisation des variables
    bonus3 = 0
    liste_bonus3 = liste_bonus4                     #On crée une nouvelle liste de seulement 3 valeurs (les premières)
    del liste_bonus3[3]                             #On supprime le 4ème cheval car inutile
    print("Liste du Bonus 3 :", liste_bonus3)
    for i in range(0, 3):
        if liste_pari[i] in liste_bonus3:           #Si le cheval [i] est dans la liste, alors la condition est vérifiée
            bonus3 += 1

    print("                                                                    ")

    for i in range(0, len(tuple_gagnant)):                                  #On repète autant de fois qu'il y à de chevaux dans la liste gagnante (soit 5)...
        if liste_pari[i] in tuple_gagnant:                                  #Si le cheval est dans le tuple gagnant...
            a = liste_pari[i]                                               #On assigne à a le numero du cheval.
            print("Le cheval {} est dans les deux listes".format(a))        #On informe le parieur que le cheval est dans les deux listes.
            #Pour trouver la place du cheval dans la liste gagnante et dans la liste du parieur, on utilise la méthode tuple.index(element) qui permet de retrouver la place de l'élement.
            #On y ajoute 1 car on rappelle que la première position d'un tuple est int(0).
            print("Il est à la {} ème/ère position dans votre liste et à la {} ème/ère dans la liste gagnante".format(liste_pari.index(a) + 1, tuple_gagnant.index(a) + 1))
            print("                                                                    ")

    print("                                                                    ")

    #Retour des gains.
    if quinte_ordre == 5:
        print("Gain : QUINTE !")

        #Affichage d'une fenêtre (VOIR MODULE TKINTER)
        quinte_w = Tk()

        quinte_w.title("Quinte - Affichage")        #Nom de la fenêtre
        quinte_w.geometry("620x60")                 #Dimensions
        quinte_w.minsize(620, 60)                   #Dimensions minimales

        label_title = Label(quinte_w, text="Vous avez une quinte", font=("Arial", 40), bg='#AB1B36', fg='white')        #Texte affiché
        label_title.pack()

        quinte_w.mainloop()                         #Affichage.

        return "Quinte"

    elif quinte_desordre == 5:
        print("Gain : QUINTE (Desordre) !")

        #Affichage d'une fenêtre
        quinte_desordre_w = Tk()

        quinte_desordre_w.title("Quinte desordre - Affichage")
        quinte_desordre_w.geometry("800x60")
        quinte_desordre_w.minsize(800, 60)

        label_title = Label(quinte_desordre_w, text="Vous avez une quinte (desordre)", font=("Arial", 40), bg='#AB1B36', fg='white')
        label_title.pack()

        quinte_desordre_w.mainloop()

        return "Quinte désordre"

    elif bonus4 == 4:
        print("Gain : BONUS 4 !")

        #Affichage d'une fenêtre
        bonus4_w = Tk()

        bonus4_w.title("Quinte - Affichage")
        bonus4_w.geometry("620x60")
        bonus4_w.minsize(620, 60)

        label_title = Label(bonus4_w, text="Vous avez un bonus 4", font=("Arial", 40), bg='#AB1B36', fg='white')
        label_title.pack()

        bonus4_w.mainloop()

        return "Bonus 4"

    elif bonus3 == 3:
        print("Gain : BONUS 3 !")

        #Affichage d'une fenêtre
        bonus3_w = Tk()

        bonus3_w.title("Bonus 3 - Affichage")
        bonus3_w.geometry("620x60")
        bonus3_w.minsize(620, 60)

        label_title = Label(bonus3_w, text="Vous avez un bonus 3", font=("Arial", 40), bg='#AB1B36', fg='white')
        label_title.pack()

        bonus3_w.mainloop()

        return "Bonus 3"

    else:
        print("PERDU !")

        #Affichage d'une fenêtre
        perdu_w = Tk()

        perdu_w.title("Perte - Affichage")
        perdu_w.geometry("620x60")
        perdu_w.minsize(620, 60)

        label_title = Label(perdu_w, text="Vous avez perdu !", font=("Arial", 40), bg='#AB1B36', fg='white')
        label_title.pack()

        perdu_w.mainloop()

        return "Perdu !"

quinte()


