from bateau import Bateau
from grille import Grille

b1 = Bateau(2, 3)
b2 = Bateau(0, 0, 4, True)
print(b1)
print(b2)
print(Bateau(2, 3, 3).positions)
print(Bateau(2, 3,3,True).positions)

print("\n**Test Bateau.coule**")
g = Grille(5, 5)
b3 = Bateau(1, 1, 2)
g.ajoute(b3)
print("Avant tirs :", b3.coule(g))

# On tire sur toutes les positions du bateau
for l, c in b3.positions:
    g.tirer(l, c)
print("Après tirs :", b3.coule(g)) 
