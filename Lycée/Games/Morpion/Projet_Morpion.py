"""Programme du morpion v.1.05"""
"""Noé Daniel 1ère1 NSI"""

#Importation des modules graphiques
from tkinter import *
from tkinter.messagebox import *    #Permet d'ouvrir des fenêtres d'information grâce à la fonction showinfo().

def choix_case(event):
    #Un événement (event) est la survenue d’une action (clavier, souris) dont votre application a besoin d’être informée.
    #Un gestionnaire d’événement (event handler) est une fonction de votre application qui a vocation a être appelée lorsqu’un certain événement se produira.
    #http://tkinter.fdex.eu/doc/event.html

    #On utilise l'instruction global qui restreint l'utilisation des variables uniquement dans notre fonction.

    #Premièrement on initialise la variable qui permet de changer de motif
    global motif

    #On initialise les variables traitant les données des lignes et des colonnes.
    global Colonne1, Colonne2, Colonne3
    global Ligne1, Ligne2, Ligne3

    #On initialise les variables comptant les points du joueur 1 sur les lignes et les colonnes (utiles lors du comptage)
    global Colonne1_Joueur1, Colonne2_Joueur1, Colonne3_Joueur1
    global Ligne1_Joueur1, Ligne2_Joueur1, Ligne3_Joueur1

    #On initialise les variables comptant les points du joueur 2 sur les lignes et les colonnes (utiles lors du comptage)
    global Colonne1_Joueur2, Colonne2_Joueur2, Colonne3_Joueur2
    global Ligne1_Joueur2, Ligne2_Joueur2, Ligne3_Joueur2

    #Grâce aux entrées (event), on peut récuper la position sur la fenêtre du capteur de la souris.
    coordonnes_X = event.x
    coordonnes_Y = event.y

    #Si le motif est une croix, on laisse jouer le Joueur 1 et on dessinera une croix
    if motif == "X":
        """#On pose coordonnes_X < 200 pour la première colonne (c'est-à-dire celle de gauche) !"""
        if coordonnes_X < 200:
            """#On pose coordonnes_Y 200 pour la première ligne en haut !"""
            if coordonnes_Y < 200:
                #Si les conditions coordonnes_X < 200 et coordonnes_Y < 200 sont vérifiés"""
                #Ce qui revient à dire si l'on clique sur la case tout en haut à gauche..."""
                """On cherche a voir si la case n'est pas cochée !"""
                if Colonne1[0] == 2:      #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                    motif = "O"       #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                    Colonne1[0]= 1        #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Ligne1[0]= 1        #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Dessiner_Croix(100,100)    #On crée une croix qui a pour coordonnées centraux (100, 100)
                    print("Joueur 1 : Vous avez coché la case A1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
            #Sinon...
            else :
                #...on passe alors à la deuxième ligne de la première colonne
                if coordonnes_Y < 400:
                    #Si les conditions coordonnes_X < 200 et coordonnes_Y < 400 sont vérifiés"""
                    #Ce qui revient à dire si l'on clique sur la case dans la première colonne deuxième ligne."""
                    """On cherche a voir si la case n'est pas cochée !"""
                    if Colonne1[1] == 2:     #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"      #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne1[1] = 1        #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne2[0] = 1        #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(100,300)       #On crée une croix qui a pour coordonnées centraux (100, 300)
                        print("Joueur 1 : Vous avez coché la case A2 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
                else :
                #Si les deux premières lignes ne correspondent pas à la plage de coordonnées ou figurait le curseur.
                #On en deduit alors que l'on est dans la case de la première colonne troisième ligne.
                    if Colonne1[2]==2:    #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"   #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne1[2]=1     #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne3[0]=1     #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(100,500)       #On crée une croix qui a pour coordonnées centraux (100, 500)
                        print("Joueur 1 : Vous avez coché la case A3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')

        if coordonnes_X > 200 and coordonnes_X < 400:
            """#On pose coordonnes_X > 200 and coordonnes_X < 400 pour la deuxième colonne (c'est-à-dire celle du mileu) !"""
            """#On pose coordonnes_Y < 200 pour la première ligne en haut !"""
            if coordonnes_Y < 200:
                #Si les conditions coordonnes_X entre 200 et 400 et coordonnes_Y < 200 sont vérifiés"""
                #Ce qui revient à dire si l'on clique sur la case de la deuxième colonne mais de la première ligne"""
                if Colonne2[0]==3:        #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                    motif = "O"       #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                    Colonne2[0]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Ligne1[1]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Dessiner_Croix(300,100)           #On crée une croix qui a pour coordonnées centraux (300, 100)
                    print("Joueur 1 : Vous avez coché la case B1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
            else :
                if coordonnes_Y < 400:
                    #Si les conditions 200 < coordonnes_X < 400 et coordonnes_Y < 400 sont vérifiés"""
                    #Ce qui revient à dire si l'on clique sur la case dans la deuxième colonne deuxième ligne."""
                    if Colonne2[1]==3:      #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"     #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne2[1]=1       #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne2[1]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(300,300)         #On crée une croix qui a pour coordonnées centraux (300, 300)
                        print("Joueur 1 : Vous avez coché la case B2 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
                else :
                    #Si les deux premières lignes ne correspondent pas à la plage de coordonnées ou figurait le curseur.
                    #On en deduit alors que l'on est dans la case de la deuxième colonne, troisième ligne.
                    if Colonne2[2]==3:      #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"     #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne2[2]=1       #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne3[1]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(300,500)         #On crée une croix qui a pour coordonnées centraux (300, 500)
                        print("Joueur 1 : Vous avez coché la case B3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title ='Erreur de placement',message = 'Tu ne peux pas jouer sur cette case.')

        if coordonnes_X > 400 and coordonnes_X < 600:
            """#On pose coordonnes_X > 400 and coordonnes_X < 600 pour la troisièmme colonne (c'est-à-dire celle de droite !)"""
            """#On pose coordonnes_Y < 200 pour la première ligne en haut !"""
            if coordonnes_Y < 200:
                #Si les conditions coordonnes_X entre 400 et 600 et coordonnes_Y < 200 sont vérifiés"""
                #Ce qui revient à dire si l'on clique sur la case de la troisième colonne mais de la première ligne"""
                if Colonne3[0]==4:      #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                    motif = "O"         #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                    Colonne3[0]=1       #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Ligne1[2]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                    Dessiner_Croix(500,100)             #On crée une croix qui a pour coordonnées centraux (500, 100)
                    print("Joueur 1 : Vous avez coché la case C1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title = 'Erreur de placement', message ='Tu ne peux pas jouer sur cette case.')

            else :
                if coordonnes_Y < 400:
                    #Si les conditions 400 < coordonnes_X < 600 et coordonnes_Y < 400 sont vérifiés"""
                    #Ce qui revient à dire si l'on clique sur la case dans la troisième colonne deuxième ligne."""
                    if Colonne3[1]==4:      #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"         #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne3[1]=1       #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne2[2]=1         #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(500,300)         #On crée une croix qui a pour coordonnées centraux (500, 300)
                        print("Joueur 1 : Vous avez coché la case C2 !")

                    #Si les conditions ne sont pas respéctées...
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement', message = 'Tu ne peux pas jouer sur cette case.')

                else :
                    #Si les deux premières lignes ne correspondent pas à la plage de coordonnées ou figurait le curseur.
                    #On en deduit alors que l'on est dans la case de la troisième colonne, troisième ligne.
                    if Colonne3[2] == 4:        #Si la valeur atribuée au départ et inchangée, alors le joueur peut obtenir cette case...
                        motif = "O"             #On fait changer de joueur, c'est-à dire que l'on change le motif de croix en rond.
                        Colonne3[2]=1           #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Ligne3[2]=1             #Pour qu'on puisse ne plus reattribuer cette case et permettre le comptage, on change la valeur de celle qui était atribuée au départ
                        Dessiner_Croix(500,500)         #On crée une croix qui a pour coordonnées centraux (500, 300)
                        print("Joueur 1 : Vous avez coché la case C3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')


    #A partir de ce stadee, on a les mêmes fonctions qu'au-dessus mais attribuées au joueur 2 puisque on a plus le motif = "X"
    #Ainsi on aura des ronds
    else:
        if coordonnes_X < 200:
            if coordonnes_Y < 200:
                if Colonne1[0]==2:
                    motif = "X"
                    Colonne1[0]=0
                    Ligne1[0]=0
                    Dessiner_Rond(100,100)
                    print("Joueur 2 : Vous avez coché la case A1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
            else :
                if coordonnes_Y < 400:
                    if Colonne1[1]==2:
                        motif = "X"
                        Colonne1[1]=0
                        Ligne2[0]=0
                        Dessiner_Rond(100,300)
                        print("Joueur 2 : Vous avez coché la case A2 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
                else :
                    if Colonne1[2]==2:
                        motif = "X"
                        Colonne1[2]=0
                        Ligne3[0]=0
                        Dessiner_Rond(100,500)
                        print("Joueur 2 : Vous avez coché la case A3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')

        if coordonnes_X < 400 and coordonnes_X > 200:
            if coordonnes_Y < 200:
                if Colonne2[0]==3:
                    motif = "X"
                    Colonne2[0]=0
                    Ligne1[1]=0
                    Dessiner_Rond(300,100)
                    print("Joueur 2 : Vous avez coché la case B1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')

            else :
                if coordonnes_Y < 400:
                    if Colonne2[1] == 3:
                        motif = "X"
                        Colonne2[1]=0
                        Ligne2[1]=0
                        Dessiner_Rond(300,300)
                        print("Joueur 2 : Vous avez coché la case B2 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')

                else :
                    if Colonne2[2]==3:
                        motif = "X"
                        Colonne2[2]=0
                        Ligne3[1]=0
                        Dessiner_Rond(300,500)
                        print("Joueur 2 : Vous avez coché la case B3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')

        if coordonnes_X < 600 and coordonnes_X > 400:
            if coordonnes_Y < 200:
                if Colonne3[0]==4:
                    motif = "X"
                    Colonne3[0]=0
                    Ligne1[2]=0
                    Dessiner_Rond(500,100)
                    print("Joueur 2 : Vous avez coché la case C1 !")
                else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
            else :
                if coordonnes_Y < 400:
                    if Colonne3[1]==4:
                        motif = "X"
                        Colonne3[1]=0
                        Ligne2[2]=0
                        Dessiner_Rond(500, 300)
                        print("Joueur 2 : Vous avez coché la case C2 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')
                else :
                    if Colonne3[2]==4:
                        motif = "X"
                        Colonne3[2]=0
                        Ligne3[2]=0
                        Dessiner_Rond(500,500)
                        print("Joueur 2 : Vous avez coché la case C3 !")
                    else :
                        #On renvoie le message suivant
                        showinfo(title='Erreur de placement',message='Tu ne peux pas jouer sur cette case.')


#ici on créer la fonction pour afficher les ronds
def Dessiner_Rond(abscisse, ordonnee):
    global Colonne1,Colonne2,Colonne3

    Cases.create_oval(abscisse-90, ordonnee-90, abscisse+90, ordonnee+90)   #create_oval() permet de dessiner un rond à des coordonnées.

    Compte_points()     #Après avoir dessiné le motif on fait appel à la fonction de compatabilisation
                        #Ainsi on sera si un des joueurs a gagné.

#ici on créer la fonction pour afficher les croix
def Dessiner_Croix(abscisse, ordonnee):
    global Colonne1,Colonne2,Colonne3

    Cases.create_line(abscisse-90, ordonnee-90, abscisse+90, ordonnee+90)   #create_line() permet de dessiner une ligne passant par des coordonnées.
    Cases.create_line(abscisse+90, ordonnee-90, abscisse-90, ordonnee+90)   #create_line() permet de dessiner une ligne passant par des coordonnées.

    Compte_points()     #Après avoir dessiné le motif on fait appel à la fonction de compatabilisation
                        #Ainsi on sera si un des joueurs a gagné.


def Compte_points():    #Création de la fonction de comptabilisation des points.

    global Colonne1, Colonne2,Colonne3
    global Ligne1, Ligne2, Ligne3

    global Colonne1_Joueur1, Colonne2_Joueur1, Colonne3_Joueur1
    global Colonne1_Joueur2, Colonne2_Joueur2, Colonne3_Joueur2

    global Ligne1_Joueur1, Ligne2_Joueur1, Ligne3_Joueur1
    global Ligne1_Joueur2, Ligne2_Joueur2, Ligne3_Joueur2

    Colonne1_Joueur1 = Colonne1.count(1)    #On compte le nombre de 1 dans la Colonne 1 (C'est-à-dire le nombre de croix dans la colonne 1)
    Colonne1_Joueur2 = Colonne1.count(0)    #On compte le nombre de 0 dans la Colonne 1 (C'est-à-dire le nombre de ronds dans la colonne 1)
    Colonne2_Joueur1 = Colonne2.count(1)    #On compte le nombre de 1 dans la Colonne 2 (C'est-à-dire le nombre de croix dans la colonne 2)
    Colonne2_Joueur2 = Colonne2.count(0)    #On compte le nombre de 0 dans la Colonne 2 (C'est-à-dire le nombre de ronds dans la colonne 2)
    Colonne3_Joueur1 = Colonne3.count(1)    #On compte le nombre de 1 dans la Colonne 3 (C'est-à-dire le nombre de croix dans la colonne 3)
    Colonne3_Joueur2 = Colonne3.count(0)    #On compte le nombre de 0 dans la Colonne 3 (C'est-à-dire le nombre de ronds dans la colonne 3)

    Ligne1_Joueur1 = Ligne1.count(1)    #On compte le nombre de 1 dans la Ligne 1 (C'est-à-dire le nombre de croix dans la ligne 1)
    Ligne1_Joueur2 = Ligne1.count(0)    #On compte le nombre de 0 dans la Ligne 1 (C'est-à-dire le nombre de ronds dans la ligne 1)
    Ligne2_Joueur1 = Ligne2.count(1)    #On compte le nombre de 1 dans la Ligne 2 (C'est-à-dire le nombre de croix dans la ligne 2)
    Ligne2_Joueur2 = Ligne2.count(0)    #On compte le nombre de 0 dans la Ligne 2 (C'est-à-dire le nombre de ronds dans la ligne 2)
    Ligne3_Joueur1 = Ligne3.count(1)    #On compte le nombre de 1 dans la Ligne 3 (C'est-à-dire le nombre de croix dans la ligne 3)
    Ligne3_Joueur2 = Ligne3.count(0)    #On compte le nombre de 0 dans la Ligne 3 (C'est-à-dire le nombre de ronds dans la ligne 3)


    #ici on affiche le joueur qui a gagner
    if Colonne1_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne1_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne2_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne2_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne3_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne3_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')

    """On traite les victoires par ligne c'est-à-dire que le joueur a une ligne de trois dans trois colonnes différentes"""
    if Colonne1[0]==1 and Colonne2[1]==1 and Colonne3[2]==1:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne1[2]==1 and Colonne2[1]==1 and Colonne3[0]==1:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')

    if Colonne1[0]==0 and Colonne2[1]==0 and Colonne3[2]==0:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Colonne1[2]==0 and Colonne2[1]==0 and Colonne3[0]==0:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')

    if Ligne1_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Ligne1_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Ligne2_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Ligne2_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Ligne3_Joueur1 == 3:
        showinfo(title='Partie terminée',message='Le joueur 1 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')
    if Ligne3_Joueur2 == 3:
        showinfo(title='Partie terminée',message='Le joueur 2 a gagné !')
        showinfo(title='Fermeture',message='Vous pouvez appuyer sur quitter !')


#ici on initialise les variables de comptage des motifs/points pour chaque joueur en fonction des colonnes, des lignes...
Colonne1_Joueur1, Colonne2_Joueur1, Colonne3_Joueur1 = 0, 0, 0  #On peut alors initialiser trois variables en même temps pour gagner de la place.
Colonne1_Joueur2, Colonne2_Joueur2, Colonne3_Joueur2 = 0, 0, 0
Ligne1_Joueur1, Ligne2_Joueur1, Ligne3_Joueur1 = 0, 0, 0
Ligne1_Joueur2, Ligne2_Joueur2, Ligne3_Joueur2 = 0, 0, 0


motif = "X"     #On définit le premier motif, c'est-à-dire que le joueur 1 aura par défaut des croix.

Colonne1 = [2, 2, 2]
Colonne2 = [3, 3, 3]
Colonne3 = [4, 4, 4]

Ligne1 = [2, 2, 2]
Ligne2 = [3, 3, 3]
Ligne3 = [4, 4, 4]

print("Vérification automatique des colonnees / lignes")
print("Ne pas prêter attention à ce qui va suivre !")
print("Colonnes : [1] {}, [2] {}, [3] {}.".format(Colonne1, Colonne2, Colonne2))
print("Lignes : [1] {}, [2] {}, [3] {}.".format(Ligne1, Ligne2, Ligne2))


# Création de la fenêtre principale
GrilleMorpion = Tk()
GrilleMorpion.title("Grille du Jeu")

#On crée le damier de la grille.

#Premièrement on définit les dimensions en pixels de la fenêtre
Dimensions_L = 600  #Largeur
Dimensions_H = 600  #Hauteur

#On crée une rame de Cases qui sera un Canvas.
#On appelle Canvas tout ce qui peut-être considéré comme un widget (cf. Documentation française de Tkinter).

Cases = Canvas(GrilleMorpion, width = Dimensions_L, height = Dimensions_H, bg ="#0779AA")

#On attribue a chaque clique GAUCHE ! de souris la fonction choix_case qui renvoie la fonction définie au-dessus.
Cases.bind("<Button-1>", choix_case)

#On définit les distances d'écart entre les cases
Cases.pack(padx =5, pady =5)


#On va créer les lignes horizontales de la grille grâce à la fonction intégrée create_line()
Cases.create_line(0,200,600,200,fill = "red" ,width=4)      #'fill' permet de remplir la ligne d'une couleur
Cases.create_line(0,400,600,400,fill = "red" ,width=4)      #'width' permet de donner l'épaisseur de la ligne

#On va créer les lignes verticales de la grille grâce à la fonction intégrée create_line()
Cases.create_line(200,600,600,-100000, fill = "green" ,width=4)      #'fill' permet de remplir la ligne d'une couleur
Cases.create_line(400,600,600,-100000, fill = "green" ,width=4)      #'width' permet de donner l'épaisseur de la ligne
#On utilise la valeur -100000 qui permet d'avoir un angle droit


# Création d'un widget Button (bouton Quitter)
Button(GrilleMorpion, text = "Fermer", command = GrilleMorpion.destroy).pack(side=LEFT,padx=5,pady=5)

GrilleMorpion.mainloop()