#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 15:44:06 2021

@author: noedaniel
"""

from random import *

def T(N, p):
    c_max, c, J1, J2 = 0, 0, 0, 0
    while c_max != N:
        J2 += 1
        if random() < p:    #Si Jk gagne...
            c += 1
            #print("Joueur", J1, "gagne contre joueur", J2,", nb de matchs gagnés :", c)
            if c > c_max:
                c_max = c
        else:
            #print("Joueur {} perd contre Joueur {} avec un nb de matchs de {}".format(J1, J2, c))
            c = 1
            J1 = J2
    return J2  #J2 est aussi le nombre de matchs
    
            
def moyenne(N, p):
    somme_matchs = 0
    for i in range(10**4):
        somme_matchs += T(N, p)
    print("Moyenne du nombre de matchs : ",somme_matchs/(10**4))
    

    
