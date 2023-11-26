def my_function(liste):
    taille = 0
    for _ in liste:
         taille += 1

    while taille > 1:
        i = 0
        while i < taille - 1:
            if liste[i] > liste[i+1]:
                # Échange les éléments s'ils sont dans le mauvais ordre
                liste[i], liste[i+1] = liste[i+1], liste[i]
            i += 1
        taille -= 1
    return liste

L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print("Liste avant :", L)

resultat = my_function(L)
print("Liste après :", resultat)


