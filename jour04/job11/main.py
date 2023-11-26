def my_function(liste):
    
    for i in range(len(liste)):
        liste[i] += 1

L = [7, 11, 42, 39, 2]
print("Liste de base :", L)
my_function(L)
print("Liste modifiée :", L)

