from grille import Grille
from bateau import Bateau

g = Grille(5, 8)
print("Grille initiale :")
g.afficher()

print("\nAprès le tir à la case (2,3) :")
g.tirer(2, 3)
g.afficher()

g = Grille(2, 3)
print("\nAjout bateau horizontal qui rentre :")
print(g.ajoute(Bateau(1, 0, longueur=2, vertical=False)))
g.afficher()

g2 = Grille(2, 3)
print("\nAjout bateau vertical qui ne rentre pas :")
print(g2.ajoute(Bateau(1, 0, longueur=2, vertical=True)))
g2.afficher()

g3 = Grille(2, 3)
print("\nAjout bateau vertical trop grand :")
print(g3.ajoute(Bateau(1, 0, longueur=4, vertical=True)))
g3.afficher()

