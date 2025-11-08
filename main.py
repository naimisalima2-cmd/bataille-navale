import random
import os
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
import sys
import locale
sys.stdout.reconfigure(encoding='utf-8')

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


SYMBOLS_BATEAU = {"🚢", "⛴", "🚣", "🐟", "⛵"}

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def zone_autour(l, c, grille):
    """Retourne les cases autour d’une position (pour empêcher les bateaux de se coller)."""
    voisins = []
    for dl in (-1, 0, 1):
        for dc in (-1, 0, 1):
            nl, nc = l + dl, c + dc
            if 0 <= nl < grille.nombre_lignes and 0 <= nc < grille.nombre_colonnes:
                voisins.append((nl, nc))
    return voisins


def placer_bateaux(grille, boats):
    for bateau in boats:
        placed = False
        while not placed:
            ligne = random.randint(0, grille.nombre_lignes - 1)
            colonne = random.randint(0, grille.nombre_colonnes - 1)
            vertical = random.choice([True, False])

            bateau.ligne = ligne
            bateau.colonne = colonne
            bateau.vertical = vertical

            ok = True
            for (l, c) in bateau.positions:
                if l >= grille.nombre_lignes or c >= grille.nombre_colonnes:
                    ok = False
                    break
            if not ok:
                continue

            interdit = False

            for (l, c) in bateau.positions:
                idx = l * grille.nombre_colonnes + c
                if grille.matrice[idx] != grille.vide:
                    interdit = True
                    break

                for (vl, vc) in zone_autour(l, c, grille):
                    if grille.matrice[vl * grille.nombre_colonnes + vc] in SYMBOLS_BATEAU:
                        interdit = True
                        break
                if interdit:
                    break

            if interdit:
                continue

            grille.ajoute(bateau)
            placed = True


def afficher_grille(grille, bateaux, debug=False):
    positions_coulees = {}
    for b in bateaux:
        if b.coule(grille):
            for (l, c) in b.positions:
                positions_coulees[(l, c)] = b.marque

    print("    " + " ".join([str(i) for i in range(grille.nombre_colonnes)]))

    print("   " + "-" * (2 * grille.nombre_colonnes))

    for i in range(grille.nombre_lignes):
        ligne = f"{i} | "
        for j in range(grille.nombre_colonnes):
            idx = i * grille.nombre_colonnes + j
            case = grille.matrice[idx]

            if (i, j) in positions_coulees:
                ligne += RED + positions_coulees[(i, j)] + RESET + " "
            elif debug and case in SYMBOLS_BATEAU:
                ligne += YELLOW + case + RESET + " "
            elif case in SYMBOLS_BATEAU:
                ligne += "~ "
            elif case == "💣":
                ligne += GREEN + "💣" + RESET + " "
            elif case == "x":
                ligne += CYAN + "x" + RESET + " "
            else:
                ligne += case + " "

        print(ligne)
    print()



def tirer(grille, bateaux, ligne, colonne, annonces):
    idx = ligne * grille.nombre_colonnes + colonne
    case = grille.matrice[idx]

    if case in ("💣", "x"):
        return YELLOW + "Déjà tiré ici !" + RESET

    if case in SYMBOLS_BATEAU:
        grille.matrice[idx] = "💣"
        msg = GREEN + "Touché ! " + RESET
        for b in trouver_bateaux_touchés(bateaux, ligne, colonne):
            if b.coule(grille) and id(b) not in annonces:
                msg += RED + getattr(b, "message_coule", f"{type(b).__name__} coulé !") + RESET
                annonces.add(id(b))
        return msg

    grille.matrice[idx] = "x"
    return CYAN + "Plouf !" + RESET



def tous_coules(grille, bateaux):
    return all(b.coule(grille) for b in bateaux)


def trouver_bateaux_touchés(bateaux, ligne, colonne):
    return [b for b in bateaux if (ligne, colonne) in b.positions]


def main(debug=False):

    clear()
    print("🎮 Bataille Navale 🎮\n")

    grille = Grille(8, 10)
    bateaux = [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0)
    ]

    placer_bateaux(grille, bateaux)

    coups = 0
    annonces = set()
    message = ""

    while not tous_coules(grille, bateaux):
        clear()
        print("🎮 Bataille Navale 🎮\n")
        afficher_grille(grille, bateaux, debug)
        if message:
            print(message)
        print()

        raw = input("Entrez un tir (ligne,colonne) : ").strip()
        raw = raw.replace(" ", "").replace(";", ",")

        try:
            ligne, colonne = map(int, raw.split(","))
        except:
            message = RED + "Format invalide (ex : 3,7)" + RESET
            continue

        if not (0 <= ligne < grille.nombre_lignes and 0 <= colonne < grille.nombre_colonnes):
            message = RED + "Coordonnées hors-grille !" + RESET
            continue

        coups += 1
        message = tirer(grille, bateaux, ligne, colonne, annonces)

    clear()
    print("🎉🎉🎉 VICTOIRE 🎉🎉🎉")
    afficher_grille(grille, bateaux)
    print(GREEN + f"Tous les bateaux ont été coulés en {coups} tirs !" + RESET)


if __name__ == "__main__":
    main(debug=False)   
