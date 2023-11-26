# Fonction pour arrondir les nombres dans la liste
# def my_function(liste):
# Liste initiale
liste_nombre = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print("liste non arrondie: ",liste_nombre)

# Fonction personnalisée pour arrondir un nombre à deux décimales
def arrondir(nombre):
    decimales = 0.5
    return (nombre + decimales )



#fonction de trie de la liste dans l'ordre croissant
def my_function(liste):
    n = 0
    for _ in liste:
        n += 1

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if liste[j] > liste[j + 1]:
                # Échanger les éléments
                temp = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = temp
            j += 1
        i += 1

# Arrondir chaque nombre dans la liste à deux décimales
liste_arrondie = [arrondir(nombre) for nombre in liste_nombre]


# Trier la liste arrondie
my_function(liste_arrondie)

# Afficher la liste arrondie et triée
print("Liste trier et arrondie :", liste_arrondie)
