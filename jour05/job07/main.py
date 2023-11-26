def my_function(notes):


    return [note if note < 40 or note % 5 < 3 
            else (note // 5 + 1) * 5 
            for note in notes]


notes_etudiants = [37, 82, 68, 95, 43, 73, 58, 11]
print(f"Notes originales : {notes_etudiants}")
notes_arrondies = my_function(notes_etudiants)
print(f"Notes arrondies : {notes_arrondies}")
