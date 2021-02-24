import os

def importation_8mots():
    fichier = open("listedemots.txt", 'r')
    contenu = fichier.read()
    contenu = contenu.split(" - ")
    fichier.close()
    return contenu