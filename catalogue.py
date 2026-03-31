
        
with open("catalogue.txt", 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        en_tete = lignes[0]
        
        for ligne in lignes[1:]: 
            #on separe en liste
            donnees = ligne.strip().split(';')
            
            note= (len(donnees))-1
            nom= donnees[0]
            date = donnees[1]
            realisateur= donnees[2]
            
            print(f"{nom} ({date}), réalisateur: {realisateur} note: {note}/10")
            
            