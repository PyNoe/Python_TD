#Représenter le triangle de Pascal jusqu'à la n-ième ligne de façon pyramidale.
#Noé DANIEL - 25/04/2021


def factorielle(n):
    a = n
    if a == 0:
        return 1
    for i in range(1, n):
        a = a*i
    return int(a)

def binomial(n, p):
    a = (factorielle(n))/((factorielle(p))*(factorielle(n-p)))
    return int(a)

def triangle(n):
    T = []
    for i in range(0, n+1):
        T2 = []
        for j in range(0, i+1):
            T2.append(binomial(i, j))
        T.append(T2)

    b = ""
    for elt in T[-1]:
        b += str(elt)

    nb_max = len(b)+len(T[-1])-1

    for i in range(len(T)):
        a = ""  #Espacement à rajouter avant le 1er chiffre
        c = ""
        for elt in T[i]:
            c += str(elt)
        nb = len(c)
        nb += len(T[i])-1
        
        a += " " * ((nb_max - nb)//2)

        for j in range(len(T[i])):
            a += str(T[i][j])
            if j != len(T[i])-1:
                a += " "
        print(a)

#Noé DANIEL - 25/04/2021
        
