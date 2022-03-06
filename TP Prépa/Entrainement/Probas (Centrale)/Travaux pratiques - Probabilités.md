---
Noé Daniel : 24 avril 2021
---

# Travaux pratiques - Probabilités.

### Exercice 1 (Centrale Sup-Elec)

a) Écrire une fonction Python T(N,p) qui renvoie TN,p suite à la simulation d’un tournoi.

```python
from random import *

def T(N, p):
    c_max, c, J1, J2 = 0, 0, 0, 0
    while c_max != N:
        J2 += 1
        if random() < p:    #Si Jk gagne...
            c += 1
            print("Joueur", J1, "gagne contre joueur", J2,", nb de matchs gagnés :", c)
            if c > c_max:
                c_max = c
        else:
            print("Joueur {} perd contre Joueur {} avec un nb de matchs de {}".format(J1, J2, c))
            c = 1
            J1 = J2
    return J2  #J2 est aussi le nombre de matchs
```

b) Écrire une fonction moyenne(N, p) qui renvoie la moyenne des TN,p obtenus lors de 10**4 tournois.

```python
def moyenne(N, p):
    somme_matchs = 0
    for i in range(10**4):
        somme_matchs += T(N, p)
    print("Moyenne du nombre de matchs : ",somme_matchs/(10**4))
```

c) Que donnent moyenne(3, 0.7) et moyenne(6, 0.5) ? (Vous devez trouver environ 4,47 et 63.)

```python
moyenne(3, 0.7)
>>> Moyenne du nombre de matchs :  4.4501

moyenne(6, 0.5)
>>> Moyenne du nombre de matchs :  62.4989
```

### Exercice 2 (Centrale Sup-Elec)

a) Rédiger une fonction *experience(n)* qui renvoie la position finale de la balle après une expérience.

```python
from random import *

def experience(n):
    case = 0
    for i in range(n):
        if random() < 0.5:
            case += 1
    return case
```

b) On réitère N fois cette expérience. Rédiger une fonction *simulation(n, N)* qui renvoie un tableau t à n + 1 cases, t[k] étant égale à la proportion de balle dans la case k en position finale.

```python
def simulation(n, N):
    t = [0 for i in range(n+1)]
    for i in range(N):
        r = experience(n)
        t[r] += 1
    return t
```

c) Tracer la courbe donnant cette proportion en fonction de k pour n = 20 et N = 103.

```python
import matplotlib.pyplot as plt

plt.plot(simulation(20, 10**3))
plt.show()
```

Voir "Figure_Exo2.png"

d) On suppose désormais que la probabilité que la balle avance d’une case est égale à p ∈]0,1[. Modifier la fonction *experience* et faire quelques essais pour différentes valeurs de p.

```python
def experience2(n, p):
    case = 0
    for i in range(n):
        if random() < p:
            case += 1
    return case 
```

