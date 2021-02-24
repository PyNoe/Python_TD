"""Module d'importation graphique"""

from tkinter import *

#1è fonction :
def page_lancement():

    lancement = Tk()

    lancement.title("Jeu du pendu par Noé !")
    lancement.geometry("800x540")
    lancement.minsize(480, 360)
    lancement.config(background='#196996')

    label_title = Label(lancement, text="Développé par Noé Daniel", font=("Arial", 40), bg='#196996', fg='white')
    label_title.pack(ipady=10, padx=10)

    bouton1 = Button(lancement, text = "Lancer !", font=("Courrier", 25), bg='#FFFFFF', fg='#196996', activeforeground = 'red', command = lancement.destroy)
    bouton1.pack(pady = 5)

    lancement.mainloop()

def reveler_mot_gagné(mot, fautes):

    fautes_txt = "Nombre de fautes : {}".format(fautes)
    mot = str(mot)

    reveler = Tk()

    reveler.title("Mot à trouver !")
    reveler.geometry("800x540")
    reveler.minsize(480, 360)
    reveler.config(background='#196996')

    label_title = Label(reveler, text="Gagné ! Le mot à trouver était :", font=("Arial", 40), bg='#196996', fg='white')
    label_title.pack()

    entry1 = Entry(reveler, font = ("Arial", 20))
    entry1.pack(pady=5, ipady=10, padx=10)

    entry1.insert(0, mot)

    label_title2 = Label(reveler, text=fautes_txt, font=("Arial", 40), bg='#196996', fg='white')
    label_title2.pack()

    bouton1 = Button(reveler, text = "Passer !", font=("Courrier", 25), bg='#FFFFFF', fg='#196996', activeforeground = 'red', command = reveler.destroy)
    bouton1.pack(pady = 5)

    reveler.mainloop()

def reveler_mot_perdu(mot):

    mot = str(mot)

    reveler = Tk()

    reveler.title("Mot à trouver !")
    reveler.geometry("800x540")
    reveler.minsize(480, 360)
    reveler.config(background='#196996')

    label_title = Label(reveler, text="Perdu ! Le mot à trouver était :", font=("Arial", 40), bg='#196996', fg='white')
    label_title.pack()

    entry1 = Entry(reveler, font = ("Arial", 20))
    entry1.pack(pady=5, ipady=10, padx=10)

    entry1.insert(0, mot)

    bouton1 = Button(reveler, text = "Passer !", font=("Courrier", 25), bg='#FFFFFF', fg='#196996', activeforeground = 'red', command = reveler.destroy)
    bouton1.pack(pady = 5)

    reveler.mainloop()


def statistiques_fin(victoires, nb_parties):

    victoires_txt = "Nombre de Victoires : {}".format(victoires)
    parties_txt = "Nombre de Parties : {}".format(nb_parties)

    end = Tk()

    end.title("Jeu du pendu par Noé !")
    end.geometry("720x480")
    end.minsize(480, 360)
    end.config(background='#196996')

    label_title = Label(end, text="Fin du jeu !", font=("Arial", 40), bg='#196996', fg='white')
    label_title.pack(ipady=10, padx=10)

    label_title2 = Label(end, text= victoires_txt, font=("Arial", 40), bg='#196996', fg='white')
    label_title2.pack(ipady=10, padx=10)

    label_title3 = Label(end, text= parties_txt, font=("Arial", 40), bg='#196996', fg='white')
    label_title3.pack(ipady=10, padx=10)

    bouton1 = Button(end, text = "Quitter !", font=("Courrier", 25), bg='#FFFFFF', fg='#196996', activeforeground = 'red', command = end.destroy)
    bouton1.pack(pady = 5)

    end.mainloop()

