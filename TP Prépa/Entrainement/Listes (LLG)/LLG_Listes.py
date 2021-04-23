#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:52:04 2021

@author: noedaniel
"""

L = [1, 2, 3, 4]
#print(sum(L))

def altmax(alt):
    amax = 0
    for altitude in alt:
        if altitude > amax:
            amax = altitude
    return amax

alt = [300, 500, 600, 1000, 800, 900, 500, 600, 200, 0]
#print(altmax(alt))

def denivmax(alt):
    dmax = 0
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > dmax:
            dmax = deniv
    return dmax

#print(denivmax(alt))

def heure_dmax(alt):
    dmax, h = 0, 1
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > dmax:
            dmax = deniv
            h += i
    return h

def denivtotal(alt):
    dt = 0
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > 0:
            dt += deniv
    return dt

#print(denivtotal(alt))

def sommets(alt):
    L = []
    for i in range(1, len(alt)-1):
        if alt[i] > alt[i+1] and alt[i] > alt[i-1]:
            L.append(alt[i])
    return L

liste = [1, 0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0]

def plateau(liste, motif):
    compteur = []
    for i in range(len(liste)-1):
        c=0
        while liste[i] == motif and i <= len(liste)-1:
            c += 1
            i += 1
        compteur.append(c)
    return max(compteur)

#print(plateau(liste, 0))
        
from random import *

from numpy import mean

def elements_r():
    tableau = []
    for i in range(100):
        tableau.append(randint(0, 99))

    n = list(range(0, 100))

    for nb in tableau:
        if nb in n:
            n.remove(nb)
        
    print("Eléments réstants :", len(n))
    return len(n)

def test(i):
    moy = []
    for j in range(i):
        moy.append(elements_r())
    print("Valeur moyenne sur {} tests est de {}".format(i, mean(moy)))
           
        
    

