

# TP Listes LLG (Noé)

### Exercice 1.

Quelle fonction déjà existante en Python lui permet de calculer la durée de sa randonnée ?

```python
L = [1, 2, 3, 4]
print(sum(L))

10
```

Définir en Python une fonction baptisée *altmax*, qui prend en argument une liste alt et qui retourne l’altitude relative maximale atteinte lors de sa randonnée.

```python
def altmax(alt):
    amax = 0
    for altitude in alt:
        if altitude > amax:
            amax = altitude
    return amax

alt = [300, 500, 600, 1000, 800, 900, 500, 600, 200, 0]
print(altmax(alt))

1000
```

Définir en Python une fonction baptisée *denivmax* prenant en argument une liste alt et retournant le dénivelé maximal réalisé en une heure durant sa randonnée.

```python
def denivmax(alt):
    dmax = 0
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > dmax:
            dmax = deniv
    return dmax

print(denivmax(alt))
400
```

Modifier la fonction précédente pour qu’elle retourne non pas le dénivelé maximal mais l’heure à laquelle débute la réalisation de ce dénivelé. Pour la liste donnée en exemple, cette fonction devra donc retourner la valeur 3.

```python
def heure_dmax(alt):
    dmax, h = 0, 1
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > dmax:
            dmax = deniv
            h += i
    return h

heure_dmax(alt)
Out[45]: 3
```

Définir une fonction baptisée *denivtotal* retournant la somme des dénivelés *positifs* réalisés durant cette randonnée. Pour l’exemple donné en illustration cette fonction devra donc retourner la valeur 1200.

```python
def denivtotal(alt):
    dt = 0
    for i in range(len(alt)-1):
        deniv = alt[i+1]-alt[i]
        if deniv > 0:
            dt += deniv
    return dt

print(denivtotal(alt))
900 #Après vérification à la calculatrice, le dénivelé est bien de 900 et non de 1200.
```

Rédiger la fonction *sommets* retournant la liste des sommets de la randonnée.

```python
def sommets(alt):
    L = []
    for i in range(1, len(alt)-1):
        if alt[i] > alt[i+1] and alt[i] > alt[i-1]:
            L.append(alt[i])
    return L
    
sommets(alt)
Out[52]: [1000, 900, 600]
```

### Exercice 2.

On considère un tableau de bits dont les éléments sont égaux aux entiers 0 ou 1. Rédiger en Python une fonction calculant le nombre maximal de 0 consécutifs présents dans ce tableau.

```python
liste = [1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0]

def plateau(liste, motif):
    compteur = []
    for i in range(len(liste)-1):
        c=0
        while liste[i] == motif and i <= len(liste)-1:
            c += 1
            i += 1
        compteur.append(c)
    return max(compteur)

print(plateau(liste, 0))
7
```

### Exercice 3.

Dans le module numpy.random se trouve une fonction nommée randint. Utilisez-la pour créer une tableau de 100 entiers tirés au hasard entre 0 et 99.

Calculer le nombre d’éléments de ⟦0, 99⟧ qui n’appartiennent pas à ce tableau.

Recommencer cette expérience un grand nombre de fois pour évaluer le nombre moyen d’éléments d’absents (la valeur théorique est d’environ 36,6).

```python
rom random import *

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
```

*Résultats obtenus à titre d'exemple pour 25 itérations* :

```python
Eléments réstants : 43
Eléments réstants : 40
Eléments réstants : 40
Eléments réstants : 35
Eléments réstants : 35
Eléments réstants : 36
Eléments réstants : 41
Eléments réstants : 34
Eléments réstants : 35
Eléments réstants : 38
Eléments réstants : 42
Eléments réstants : 36
Eléments réstants : 36
Eléments réstants : 39
Eléments réstants : 34
Eléments réstants : 37
Eléments réstants : 40
Eléments réstants : 34
Eléments réstants : 38
Eléments réstants : 37
Eléments réstants : 37
Eléments réstants : 36
Eléments réstants : 33
Eléments réstants : 42
Eléments réstants : 40
Valeur moyenne sur 25 tests est de 37.52
```



https://info-llg.fr/commun-mpsi/pdf/TP5.pdf