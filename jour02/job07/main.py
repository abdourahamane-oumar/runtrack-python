chaine = "abcdefghijklmnopqrstuvwxyz"

# À partir du premier caractère
indice_depart = 0

for i in range(indice_depart, len(chaine)):
    # Crée une sous-chaîne du premier caractère jusqu'à l'indice i
    sous_chaine = chaine[indice_depart:i+1]
    
    # Affiche la sous-chaîne avec un espace entre chaque caractère
    print("" * (len(chaine) - i - 1) + ''.join(sous_chaine))

