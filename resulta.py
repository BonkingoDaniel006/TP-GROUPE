try:
    fichier= open("csv.DictReader","r",encoding="utf-8")
    contenu=fichier.read()
    fichier.close()
except FileNotFoundError:
    print ("fichier introuvable")   