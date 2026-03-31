with open("catalogue.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip()) # strip() enleve le \n en fin de ligne