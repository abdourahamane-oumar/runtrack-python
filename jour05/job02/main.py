def draw_rectangle(width, height):
    if width < 2 or height < 2:
        print("Les dimensions doivent être supérieures à 1.")
        return

#la première ligne du rectangle
    print('-' * width)

#les côtés verticaux et les espaces intérieurs
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

#la dernière ligne du rectangle
    print('-' * width)

# Exemple d'utilisation avec width=10 et height=3
draw_rectangle(10, 3)
