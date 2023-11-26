def my_function(n):
    for i in range(n + 1):
            
        for j in range(n + 1):
            if i == j:
                print('\\', end='')
            else:
                print('#', end='')
        print()

#Utilisation avec n=5
taille_tapis = 5
my_function(taille_tapis)
