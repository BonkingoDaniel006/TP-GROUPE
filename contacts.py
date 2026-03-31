def lire_contacts():
    with open('contacts.txt', 'r') as f:
        for ligne in f:
            nom, tel = ligne.strip().split('|')
            print(f"Contact : {nom} (Tél: {tel})")

def chercher_contact(nom_recherche):
    trouve = False
    with open('contacts.txt', 'r') as f:
        for ligne in f:
            nom, tel = ligne.strip().split('|')
            if nom_recherche.lower() in nom.lower():
                print(f"Résultat : {nom} -> {tel}")
                trouve = True
    if not trouve: print("Aucun résultat.")

def ajouter_contact(nom, tel):
    with open('contacts.txt', 'a') as f: # 'a' pour append (ajouter)
        f.write(f"\n{nom}|{tel}")
    print(f"Contact {nom} ajouté avec succès !")
if __name__ == "__main__":
    ajouter_contact("Charlie", "0600000000")
    lire_contacts()