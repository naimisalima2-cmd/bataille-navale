from bateau import Bateau
def chevauche(bateau1: Bateau, bateau2: Bateau):
    positions1 = set(bateau1.positions)
    positions2 = set(bateau2.positions)
    return not positions1.isdisjoint(positions2)

b1 = Bateau(2, 3, 3)
b2 = Bateau(2, 4, 2)
print(f"Les deux bateaux de positions: {b1.positions} et {b2.positions} se chevauchent ?: {chevauche(b1, b2)}")
b3 = Bateau(0, 0, 2)      
b4 = Bateau(1, 0, 2)          
print(f"Les deux bateaux de positions: {b3.positions} et {b4.positions} se chevauchent ?: {chevauche(b3, b4)}")
