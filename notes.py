notes = [12,8,15,9,17]
def afficher_notes(liste):
    print("Notes :", liste)
afficher_notes(notes)
notes.extend((19,15,11))
print(notes)
def calculer_moyenne(notes):
    return sum(notes)//len(notes)
print("La moyenne est de : ", (calculer_moyenne(notes)))