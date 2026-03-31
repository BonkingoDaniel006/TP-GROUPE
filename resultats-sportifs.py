import csv


with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecture = csv.DictReader(fichier)
    for ligne in lecture:
        print(f"Date : {ligne['date']}, Catégorie : {ligne['categorie']}, Description : {ligne['description']}, Montant : {ligne['montant']}")

with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecture = csv.DictReader(fichier)
    montants = [float(ligne["montant"]) for ligne in lecture]
    depenses_total = sum(montants)
    depenses_max = max(montants)
    depenses_min = min(montants)

print("Le total des dépenses est de : ", depenses_total)
print("Le maximum des dépenses est de : ", depenses_max)
print("Le minimum des dépenses est de : ", depenses_min)

date = "2026-01-05"
categorie = "informatique"
description = "RTX 6090"
montant = 3000
with open("depenses.csv", "a", encoding="utf-8") as nvfichier:
    nvfichier.write (f"{date}, {categorie}, {description},{montant}\n")

with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecture = csv.DictReader(fichier)
    for ligne in lecture:
        print(f"Date : {ligne['date']}, Catégorie : {ligne['categorie']}, Description : {ligne['description']}, Montant : {ligne['montant']}")