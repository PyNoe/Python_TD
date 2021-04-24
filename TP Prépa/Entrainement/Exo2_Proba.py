#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 16:07:04 2021

@author: noedaniel
"""

from random import *

def experience(n):
    case = 0
    for i in range(n):
        if random() < 0.5:
            case += 1
    return case
            
def simulation(n, N):
    t = [0 for i in range(n+1)]
    for i in range(N):
        r = experience(n)
        t[r] += 1
    return t

import matplotlib.pyplot as plt

plt.plot(simulation(20, 10**3))
plt.show()

def experience2(n, p):
    case = 0
    for i in range(n):
        if random() < p:
            case += 1
    return case 
