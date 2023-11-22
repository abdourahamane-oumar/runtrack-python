#Création de la fonction avec la string langage.
def ma_fonction(langage):
    
#Création des "si..., sinon si..., sinon..,"
    if langage == "JavaScript":
     print('tu es un développeur web')
    elif langage == "python":
       print('tu es un développeut IA')
    elif langage == "java":
       print('tu es un développeur logiciel')
    elif langage == "reactjs":
       print('tu es un developpeur mobile')
    else:
       print('un jour, je serai le meilleur développeur')
       
   

#Affichage des résultats, afin d'avoir un résulats.
ma_fonction("JavaScript")
ma_fonction("python")
ma_fonction("java")
ma_fonction("reactjs")
ma_fonction(1)
