class Bateau:
    def __init__(self, ligne: int, colonne: int, longueur: int = 1, vertical: bool = False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
    def __repr__(self):
        orientation = "Vertical" if self.vertical else "Horizontal"
        return (f"Bateau(ligne={self.ligne}, colonne={self.colonne}, "f"longueur={self.longueur}, orientation={orientation})")
    