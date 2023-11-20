# Création d'un dictionnaire pour représenter le produit
produit = {
    "nom": "Mozarella",
    "prix_unitaire": 2.40,
    "quantite_stock": 55
}

# Affichage des informations initiales du produit
print("Informations initiales du produit:")
print(f"Produit: {produit['nom']}")
print(f"Prix unitaire: {produit['prix_unitaire']} €")
print(f"Quantité en stock: {produit['quantite_stock']}")

# Demander à l'utilisateur la quantité de produits à acheter
quantite_achetee = int(input("Combien de produits souhaitez-vous acheter ? "))

# Mettre à jour le stock
produit['quantite_stock'] -= quantite_achetee

# Augmenter le prix en raison de l'inflation (10%)
produit['prix_unitaire'] *= 1.10

# Afficher à nouveau les informations du produit après les modifications
print("\nInformations après les mises à jour:")
print(f"Produit: {produit['nom']}")
print(f"Prix unitaire: {produit['prix_unitaire']} €")
print(f"Quantité en stock: {produit['quantite_stock']}")


