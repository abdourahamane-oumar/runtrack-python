# Initialisation des variables
montant_initial = 10000
taux_rendement_annuel = 5

# Affichage du gain annuel initial
print("Gain annuel initial :", (taux_rendement_annuel / 100) * montant_initial, "euros")

# Modification des variables
montant_initial += 5000
taux_rendement_annuel += 2

# Calcul du nouveau gain annuel
nouveau_gain_annuel = (taux_rendement_annuel / 100) * montant_initial
print("Nouveau gain annuel :", nouveau_gain_annuel, "euros")

# Retrait de 10% du montant total, le rendement diminue de 1%
retrait = 0.1 * montant_initial
montant_initial -= retrait
taux_rendement_annuel -= 1

# Calcul du montant final de l'investissement
montant_final = montant_initial + nouveau_gain_annuel
print("Montant final de l'investissement :", montant_final, "euros")
