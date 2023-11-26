def my_function():
    height = int(input("Entrez la hauteur du triangle : "))

    if height < 2:
        print("La hauteur doit être supérieure à 1.")
        return

    for i in range(height):
        if i == height - 1:
            print('/' + '_' * (2 * i) + '\\')
        else:
            print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')

# Appeler la fonction pour dessiner le triangle
my_function()
