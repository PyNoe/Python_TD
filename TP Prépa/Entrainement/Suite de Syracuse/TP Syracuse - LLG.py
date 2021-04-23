#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:03:26 2021

@author: noedaniel
"""

 
"""Définition de la fonction temps de vol"""
def tempsdevol(c): 
    u, n = c, 0
    while u != 1:
        n += 1
        if u % 2 == 0:
            u = u/2 
        else:
            u = 3*u + 1
    return n


 
"""Définition de la fonction altitude maximale"""
def altitudemaximale(c):
    umax = 0
    u=c 
    while u != 1:
        if u%2 == 0:
            u = u/2
        else:
            u = 3*u + 1
        if u > umax:
            umax = u
    return umax

 
def tempdarr(c): 
    u=c
    n=0
    while u >= c:
        n += 1
        if u%2 == 0:
            u = u/2 
        else:
            u = 3*u + 1
    return n

from time import *
 
def verification(m):
    t0 = time()
    for i in range(2, m+1):
        a = tempdarr(i)
        if int(a) != a:
            return "Erreur"
    tf = time()
    duree = tf - t0
    return "Vérification réussie", duree

 
def verification2(m):
    depart = time()
    for c in range(2, m+1):
        if c%4 == 3:
            u=c
            while u >= c:
                if u % 2 == 0:
                    u = u // 2
                else:
                    u=3*u+1
    fin = time()
    print("durée de la vérification :", fin-depart)
    
def altitudemax():
    amax = 0
    cmin = 0
    for c in range(1, 1000001):
        if altitudemaximale(c) > amax:
            cmin = c
            amax = altitudemaximale(c)
    return amax, cmin
            

def tempsvolmax(m):
    a, x = 1, 1
    for c in range(2, m+1):
        u=c
        n=0
        while u >= c:
            n += 1
            if u%2 == 0:
                u = u/2 
            else:
                u = 3*u + 1
        if n > a:
            a, x = n, c
    print("Valeur max de {} atteinte pour {}".format(a, x))
    
def dureerecord(m): 
    d=0
    for c in range(2, m): 
        n, u = 0, c
        while u > 1: 
            n += 1
            if u % 2 == 0: 
                u = u // 2
            else: 
                u=3*u+1
            if n > d: 
                d=n
    print('pour c = {}, record de durée = {}'.format(c, d))

import matplotlib.pyplot as plt

def tempsdevol_g(c):
    u, n = c, 0
    L = [c]
    while u != 1:
        n += 1
        if u % 2 == 0:
            u = u/2 
        else:
            u = 3*u + 1
        L.append(u)
    plt.plot(L)
    plt.show()
            
    
    

    
