from bateau import Bateau
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
            print()

    def tirer(self, ligne, colonne, touche='x'):
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            if self.matrice[index] == '⛵':
                self.matrice[index] = touche
                print("Touché !")
            else:
                self.matrice[index] = touche
                print("Plouf, dans l’eau...")
        else:
            print("Coordonnées invalides.")

    def ajoute(self, bateau: Bateau):
        for (ligne, col) in bateau.positions:
            if ligne >= self.nombre_lignes or col >= self.nombre_colonnes:
                return "Grille inchangée"  
        for (ligne, col) in bateau.positions:
            index = ligne * self.nombre_colonnes + col
            self.matrice[index] = '⛵'
        return "Bateau placé avec succès"

