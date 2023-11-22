#Création de la fonction ce nommant ma_fonction avec les 2 paramètres (type, saison).
def ma_fonction(type, saison):

    if type == 'fruits' and saison == 'hiver':
      print("orange, mandarine et kiwi")
    
    if type == 'fruits' and saison == 'ete':
       print("Poire,Fraise,cassis")

    if type == 'legume' and saison == 'hiver':
       print("carotte,topinambour,endive")

    if type == 'legume' and saison == 'ete':
       print("artichaut,aubergine,navet")


ma_fonction('fruits', 'hiver')
ma_fonction('legume', 'hiver')
ma_fonction('fruits', 'ete')
ma_fonction('legume', 'ete')
