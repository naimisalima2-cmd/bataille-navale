class Bateau:
    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = "⛵"
    def __repr__(self):
        orientation = "Vertical" if self.vertical else "Horizontal"
        return (f"Bateau(ligne={self.ligne}, colonne={self.colonne}, "f"longueur={self.longueur}, orientation={orientation})")
    @property
    def positions(self):
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))  
            else:
                pos.append((self.ligne, self.colonne + i))  
        return pos
    def coule(self, grille):
        for (l, c) in self.positions:
            index = l * grille.nombre_colonnes + c
            if grille.matrice[index] != '💣':
                return False
        return True

    
class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical)
        self.marque = "🚢"
        self.message_coule = "Le Porte-Avion a sombré en mer !"


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical)
        self.marque = "⛴"
        self.message_coule = "Le Croiseur a été coulé !"


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🚣"
        self.message_coule = "Le Torpilleur a disparu sous l'eau !"


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical)
        self.marque = "🐟"
        self.message_coule = "Le Sous-Marin est perdu dans les profondeurs !"
