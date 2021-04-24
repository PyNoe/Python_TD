#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:53:10 2021

@author: noedaniel
"""

def estegyptienne(lst):
    for i in range(0, len(lst)):
        ref = lst[i]
        if ref < 2:
            return False
        
        j = i
        while j > 0:
            if lst[i] < lst[j]:
                return False
            j += -1
            
    return True
        

def rationnel(lst):
    numf = 0
    for i in range(len(lst)):
        num = 1
        for j in range(len(lst)):
            if j != i:
                num = num*lst[j]
        numf += num
    deno = 1
    for elt in lst:
        deno = deno*elt
    print("La fraction est {}/{}".format(numf, deno))
    div = deno%numf
    print("Simplifiée, la fraction est {}/{}".format(int(numf / div), int(deno / div)))
    
lst = [3, 15]
        

        
