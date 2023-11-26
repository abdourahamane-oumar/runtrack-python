def my_function(marches, hauteur_marche):
    
# Conversion en mètres
    hauteur_totale = marches * hauteur_marche / 100  
# Deux allers-retours par jour, cinq jours par semaine    
    distance_par_jour = hauteur_totale * 2 * 5  
# Sept jours par semaine    
    distance_par_semaine = distance_par_jour * 7  

    return distance_par_semaine

x = 100 #100 marche par jour au total
y = 20  # il marche en tout 20 cm par jour
z = my_function(x, y) 

# Affichage du résultat
print(f'Pour {x} marches de {y} cm, le gardien parcourt {z} m par semaine.')
