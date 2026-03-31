def lire_contacts():
    """Affiche tous les contacts formatés"""
    with open('contacts.txt', 'r') as f:
        for ligne in f:
            nom, tel = ligne.strip().split('|')
            print(f"Contact : {nom} (Tél: {tel})")