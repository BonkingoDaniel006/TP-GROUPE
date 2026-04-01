notes = [12,8,15,9,17]
def afficher_notes(liste):
    print("Notes :", liste)
afficher_notes(notes)
notes.extend((19,15,11))
print(notes)
def calculer_moyenne(notes):
    return sum(notes)//len(notes)
print("La moyenne est de : ", (calculer_moyenne(notes)))
def afficher_min_max(notes):
    print("Le maximum est : ", max(notes))
    print("Le minimum est : ", min(notes))
print(afficher_min_max(notes))