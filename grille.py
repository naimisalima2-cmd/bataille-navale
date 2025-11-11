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

    def afficher_grille(grille, bateaux):
        marques_coulees = set()
        for b in bateaux:
            if b.coule(grille):
                marques_coulees.add(b.marque)

        for i in range(grille.nombre_lignes):
            ligne = ""
            for j in range(grille.nombre_colonnes):
                index = i * grille.nombre_colonnes + j
                case = grille.matrice[index]

            if case in ["🚢", "⛴", "🚣", "🐟"] and case not in marques_coulees:
                ligne += "~"
            else:
                ligne += case

        print(ligne)
    print()


    def tirer(self, ligne, colonne, touche='x'):
        if 0 <= ligne < self.nombre_lignes and 0 <= colonne < self.nombre_colonnes:
            index = ligne * self.nombre_colonnes + colonne
            case = self.matrice[index]
            if case == touche:
                print("Déjà tiré ici !")
                return "Déjà tiré ici !"
            elif case in ['🚢', '⛴', '🚣', '🐟', '⛵']:
                self.matrice[index] = '💣'
                print("Touché !")
                return "Touché !"
            else:
                self.matrice[index] = touche
                print("Plouf, dans l’eau...")
            return "Plouf, dans l’eau..."
        else:
             print("Coordonnées invalides.")
        return "Coordonnées invalides."


    def ajoute(self, bateau: Bateau):
        for (ligne, col) in bateau.positions:
            if ligne >= self.nombre_lignes or col >= self.nombre_colonnes:
                return "Grille inchangée"  
        for (ligne, col) in bateau.positions:
            index = ligne * self.nombre_colonnes + col
            self.matrice[index] = bateau.marque
        return "Bateau placé avec succès"

