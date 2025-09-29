class Grille:
    def __init__(self,nombre_lignes,nombre_colonnes):
        self.nombre_colonnes=nombre_colonnes
        self.nombre_lignes=nombre_lignes
        self.vide='~'
        self.touche="x"
        self.matrice=[]
        for i in range(nombre_lignes*nombre_colonnes):
            self.matrice.append(self.vide)
    def afficher(self):
        for i in range(self.nombre_lignes):
            for j in range(self.nombre_colonnes):
                index=i*self.nombre_colonnes+j
                print(self.matrice[index],end='')
    
            


        
