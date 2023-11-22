#Création de la fonction ce nommant calcule avec les 3 paramètres (num1,operator,num2).
def calcule (num1, operator, num2):

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    print (result)

# Voila tout les resultat en fesant les calcule.
resultat = calcule(5, "+", 3)
resultat = calcule(10, "*", 4)
resultat = calcule(8, "-", 1)
resultat = calcule(5, "/", 2)
resultat = calcule(9, "%", 7)

