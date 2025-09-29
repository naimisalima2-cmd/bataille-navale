from grille import Grille
g = Grille(5, 8)
print("Grille initiale :")
g.afficher()
print("\nAprès le tir à la case (2,3) :")
g.tirer(2, 3)
g.afficher()

