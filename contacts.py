def lire_contacts():
    """Affiche tous les contacts formatés"""
    with open('contacts.txt', 'r') as f:
        for ligne in f:
            nom, tel = ligne.strip().split('|')
            print(f"Contact : {nom} (Tél: {tel})")

def chercher_contact(nom_recherche):
    """Recherche un contact par son nom"""
    trouve = False
    with open('contacts.txt', 'r') as f:
        for ligne in f:
            nom, tel = ligne.strip().split('|')
            if nom_recherche.lower() in nom.lower():
                print(f"Résultat : {nom} -> {tel}")
                trouve = True
    if not trouve: print("Aucun résultat.")