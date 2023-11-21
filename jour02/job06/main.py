def est_premier(nombre):
    # Vérifie si le nombre est inférieur à 2 (non premier)
    if nombre < 2:
        return False

    # Vérifie si le nombre est divisible par un nombre de 2 à nombre - 1
    for i in range(2, nombre):
        if nombre % i == 0:
            return False  # Si divisible, le nombre n'est pas premier

    return True  # Si aucune division n'est trouvée, le nombre est premier

# Boucle pour itérer à travers les nombres de 2 à 1000
for nombre in range(2, 1001):
    # Vérifie si le nombre est premier en utilisant la fonction est_premier
    if est_premier(nombre):
        # Affiche le nombre s'il est premier
        print(nombre)

