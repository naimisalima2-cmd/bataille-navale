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

print("\n**Tests Touché / Plouf**")
g4 = Grille(3, 3)
g4.ajoute(Bateau(1, 1))  
g4.afficher()


print("\nTir sur une case avec bateau (1,1) ")
g4.tirer(1, 1, touche='T') 
g4.afficher()

print("\nTir sur une case vide (0,0) ")
g4.tirer(0, 0, touche='x')
g4.afficher()
