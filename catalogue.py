
        
with open("catalogue.txt", 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        en_tete = lignes[0]
        somme= 0
        Len= 0
        
        for ligne in lignes[1:]: 
            #on separe en liste
            donnees = ligne.strip().split(';')
            
            ind= (len(donnees))-1
            note= int(donnees[ind])
            nom= donnees[0]
            date = donnees[1]
            realisateur= donnees[2]
            
            
            print(f"{nom} ({date}), réalisateur: {realisateur} note: {note}/10")
        print("-------------------------------------------")
        print("les mieux cotés sont:")
        for ligne in lignes[1:]:
            donnees = ligne.strip().split(';')
            
            ind= (len(donnees))-1
            note= int(donnees[ind])
            somme+=note
            nom= donnees[0]
            date = donnees[1]
            realisateur= donnees[2]
            Len+=1
            if note>= 9:
                  
                  print(f"{nom} ({date}), réalisateur: {realisateur} note: {note}/10")

            
        
        moy= somme/Len
        print (f"la moyenne est de: {moy}")
            