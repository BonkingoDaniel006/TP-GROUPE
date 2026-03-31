import csv

with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecture = csv.DictReader(fichier)
    for ligne in lecture:
        print(f"Date : {ligne['date']}, Catégorie : {ligne['categorie']}, Description : {ligne['description']}, Montant : {ligne['montant']}")

with open("depenses.csv", "r", encoding="utf-8") as fichier:
    lecture = csv.DictReader(fichier)
    depenses_total = sum(float(ligne["montant"]) for ligne in lecture)
    print("Le total des dépenses est de : ", depenses_total)