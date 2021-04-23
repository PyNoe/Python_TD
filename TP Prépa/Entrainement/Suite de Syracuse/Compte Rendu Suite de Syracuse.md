# TP Suite de Syracuse - LLG (Noé)

**Question 1**. Le *temps de vol* d’un entier c et le plus petit entier n (en admettant qu’il existe) pour lequel :
$$
u_n = 1
$$
Par exemple, le temps de vol pour c = 14 est égal à 17. Définir une fonction nommée *tempsdevol* prenant un paramètre entier c et retournant le plus petit entier n pour lequel un = 1.

```python
"""Définition de la fonction temps de vol"""

def tempsdevol(c):
    u = c
    n = 0
    while u != 1:
        n += 1
        if u % 2 == 0:
            u = u/2
        else:
            u = 3*u + 1
    return n

print(tempsdevol(14))
>>> 1
```



**Question 2.** De manière tout aussi imagée, on appelle *altitude maximale* de c la valeur maximale de la suite. Par exemple, l’altitude maximale de c = 14 est égale à 52.
Modifier votre algorithme pour définir une fonction nommée altitude qui calcule cette fois-ci l’altitude maximale pour un entier c donné en paramètre.

```python
"""Définition de la fonction altitude maximale"""

def altitudemaximale(c):
    umax = 0
    u = c
    print(u)
    while u != 1:
        if u%2 == 0:
            u = u/2
        else:
            u = 3*u + 1
        if u > umax:
            umax = u
    return umax

print(altitudemaximale(14))
>>> 52.0
```

**Question 3.** On appelle *temps d’arrêt* (ou encore *temps de vol en altitude*) le premier entier n (s’il existe) pour lequel un < c.

- Écrire une fonction tempsdarret prenant un paramètre entier c et retournant le temps d’arrêt de la suite de Syracuse correspondante.

```python
def tempdarr(c):        
    u = c               
    n = 0               
    while u >= c:       
        n += 1          
        if u%2 == 0:    
            u = u/2     
        else:           
            u = 3*u + 1       
    return n            
```

- À l’aide de cette fonction écrire une fonction verification qui prend en argument un paramètre entier m et retourne le temps nécessaire pour vérifier que toutes les valeurs c ∈ ⟦2, m⟧ ont bien un temps d’arrêt fini. Quelle durée d’exécution obtient-t’on pour m = 1 000 000 ?

```python
def verification(m):                        
    t0 = time()                             
    for i in range(2, m+1):                 
        a = tempdarr(i)                     
        if int(a) != a:                     
            return "Erreur"                 
    tf = time()                             
    duree = tf - t0                         
    return "Vérification réussie", duree
    
verification(1000000)
('Vérification réussie', 0.7589230537414551)
```

- Si c est entier est pair, son temps d'arrêt est de 1, de façon évidente.

- Si c est de la forme 4n + 1, alors :
  $$
  u_1 = 3*(4n+1)+1=12n+4 \quad u_2 = \frac{12n+4}{2}=6n+2 \quad u_3 = 3n+1
  $$

  Donc le temps d'arrêt vaudra 3.
  
- Quel est le temps d’arrêt d’un entier pair ? et d’un entier de la forme c = 4n + 1 ? En déduire qu’on peut restreindre la recherche aux entiers de la forme 4n + 3, et modifier en conséquence la fonction précédente. Combien de temps gagne-t’on par rapport à la version précédente pour m = 1 000 000 ?
  Vérifier ensuite la conjecture pour m = 10 000 000.

```python
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
    
verification2(1000000)
>>> Durée de la vérification : 0.3061978816986084
```



**Question 4.**

a) Déterminer l’altitude maximale que l’on peut atteindre lorsque c ∈ ⟦1, 1 000 000⟧, ainsi que la valeur minimale de c permettant d’obtenir cette altitude.

```python
def altitudemax():
    amax = 0
    cmin = 0
    for c in range(1, 1000001):
        if altitudemaximale(c) > amax:
            cmin = c
            amax = altitudemaximale(c)
    return amax, cmin
    
altitudemax()
Out[14]: (56991483520.0, 704511)
```

b) Déterminer le temps de vol en altitude (autrement dit le temps d’arrêt) de durée maximale lorsque c ∈ ⟦1, 1 000 000⟧ ainsi que la valeur de c correspondante.

```python
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

tempsvolmax(1000000)
Valeur max de 287 atteinte pour 626331

```

**Question 5** On appelle *vol en altitude de durée record* un vol dont tous les temps d’arrêt de rangs inférieurs sont plus courts. Par exemple, le vol réalisé pour c = 7 est un vol en altitude de durée record (égale à 11) car tous les vols débutant par c = 1, 2, 3, 4, 5, 6 ont des temps d’arrêt de durées inférieures à 11. Déterminez tous les vols en altitude de durée record pour 
$$
c \in [1, 1000000]
$$

```python
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

dureerecord(1000000)
pour c = 999999, record de durée = 524
```

**Question 6.** Définir une fonction nommée graphique qui prend un entier c en paramètre et qui construit le graphe de la suite (un)n∈N durant son temps de vol.

```python
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
```

*Résultat obtenu pour c = 27* :

<img src="/Users/noedaniel/Library/Application Support/typora-user-images/image-20210411113738001.png" alt="image-20210411113738001" style="zoom:150%;" />

[^Noé Daniel]: Droits réservés, copies non autorisées.

