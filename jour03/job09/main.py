#Création de la fonction moyenne avec 3 paramètre (note1,note2,note3)
def moyenne(note1,note2,note3):
       
       note1 = int(input("Rentrer la première note de l'élève :" ))
       note2 = int(input("Rentrer la seconde note de l'élève :" ))
       note3 = int(input("Rentrer la troisième note de l'élève :" ))

       result = note1 + note2 + note3 
       print("moyenne_etudiant :", result)

       if result > 15 and 20:
        print("Très bon élève")
       elif result > 11 and 14:
        print("Bon élève")
       elif result > 7 and 10:
        print("Elève moyen")
       elif result > 0 and 6:
        print("Elève devant faire des efforts")

moyenne(1,2,3)
