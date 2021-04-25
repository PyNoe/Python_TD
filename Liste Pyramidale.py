#Test avec une liste T quelconque.
T = [[1],[1,2],[1,2,3],[1,10,10,1], [1, 15, 20, 25, 1]]

#Nombre de caractères avec espaces pour la dernière ligne !
b = ""
for elt in T[-1]:
    b += str(elt)   
#Longueur des chiffres seuls : len(b)
#Longueur des espaces " " entre chaque nombre : len(T[-1])-1

#Longueur en caractères de la dernière ligne :
nb_max = len(b)+len(T[-1])-1


for i in range(len(T)):
    
    a = ""  #Espacement à rajouter avant le 1er chiffre
    c = ""
    for elt in T[i]:
        c += str(elt)
    nb = len(c)     #Longueur des chiffres seuls : len(c) à la i-ème ligne
    nb += len(T[i])-1   #On ajoute la longueur des espaces : len(T[i])-1 à la i-ème ligne
    #On a le nombre de caractères de la i-ème ligne avec les espaces :
    #Par exemple pour [1, 2], on a 3 car "1 2"
    
    a += " " * ((nb_max - nb)//2)
    #On soustrait au nombre de caractères de la dernière ligne celui de la i-ème ligne
    #On le divise par 2 car on veut mettre des espaces que devant.

    #On se contente de rajouter les espaces (c'est-à-dire a) devant les chiffres déja espacés.
    for j in range(len(T[i])):
        a += str(T[i][j])
        if j != len(T[i])-1:
            a += " "
    print(a)
    
"""
On obtient :
     1
    1 2
   1 2 3
 1 10 10 1
1 15 20 25 1
"""
       
