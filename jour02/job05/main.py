# Boucle pour itérer à travers les nombres de 1 à 100
for nombre in range(1, 101):
    # Vérifie si le nombre est à la fois un multiple de 3 et de 5
    if nombre % 3 == 0 and nombre % 5 == 0:
        print("FizzBuzz")
    # Vérifie si le nombre est un multiple de 3 mais pas de 5
    elif nombre % 3 == 0:
        print("Fizz")
    # Vérifie si le nombre est un multiple de 5 mais pas de 3
    elif nombre % 5 == 0:
        print("Buzz")
    # Si le nombre n'est ni un multiple de 3 ni de 5, imprime le nombre lui-même
    else:
        print(nombre)

