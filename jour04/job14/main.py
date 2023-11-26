def lettre(char):
    # Vérifie si le caractère est une lettre alphabétique
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def my_long_word(n, phrase):
    current_word_length = 0
    current_word = ''
    result = ''
    space_flag = False  # Pour gérer les espaces entre les mots

    # Parcourir chaque caractère de la phrase
    for char in phrase:
        if lettre(char):
            # Si le caractère est une lettre, l'ajouter au mot en cours
            current_word_length += 1
            current_word += char
        elif current_word_length > 0:
            # Si le mot en cours est non vide
            if current_word_length > n:
                # Si la longueur du mot dépasse le seuil, l'ajouter au résultat
                if space_flag:
                    result += ' '  # Ajouter un espace avant le mot si nécessaire
                    space_flag = False
                result += current_word
                space_flag = True  # Activer le drapeau pour ajouter un espace avant le prochain mot
            current_word_length = 0
            current_word = ''

    # Vérifier le dernier mot de la phrase
    if current_word_length > 0 and current_word_length > n:
        if space_flag:
            result += ' '  # Ajouter un espace avant le mot si nécessaire
        result += current_word

    return result

# Exemple d'utilisation
seuil = 2
phrase_test ="j'ai trois amis qui jouent au football, je les rejoins, et nous faisons une parti de foot."
print("My_long_word",(seuil,phrase_test),"\n" )

resultat = my_long_word (seuil, phrase_test)
print("Output:",resultat)
