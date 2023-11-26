def my_function(tab): #Crée une fonction prenant en argument un tableau(tab)
# Initialise la somme de base a 0
    o = 0
# Crée une boucle qui tourne autant de fois que il y a d'élément dans le liste
    for i in range(len(tab)): #len() prend directement la taille du tableau 
        if(24<tab[i]<91): #Si dans la postion actuel i ma valeur est supérieur a 24 et inférieur a 91 :
            o+= tab[i] #Alors j'ajoute ma valeur dans o sans écraser o
   
    return o #Je renvoie ma valeur o en résultat de ma fonction
  
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
resultat = my_function(L) #Crée une variable qui contient le résultat de ma fonction avec le tableu L
print("Le calcule est :", resultat)


