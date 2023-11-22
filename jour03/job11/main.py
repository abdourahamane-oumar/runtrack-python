#Création d'une fonction nommée "time_to_text" qui prend en parametre une variable minute.
def time_to_text(minutes):

    heures = minutes // 60
    minutes_restantes = minutes % 60

    if minutes:
        print(f"{heures} heures et {minutes_restantes} minutes")

#Utilisation de la fonction en 1x
time_to_text(160)
