import tkinter as tk
from tkinter import messagebox
import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

COLOR_BG = "#0f172a"          
COLOR_PANEL = "#1e40af"       
COLOR_BLUE = "#3b82f6"        
COLOR_BLUE_HOVER = "#2563eb"  
COLOR_CYAN = "#06b6d4"        
COLOR_GREEN = "#22c55e"       
COLOR_RED = "#f14242"         
COLOR_YELLOW = "#facc15"      
COLOR_TEXT = "white"

SYMBOLS_BATEAU = {"🚢", "⛴", "🚣", "🐟"}


class BatailleNavaleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("⚓ Bataille Navale")
        self.root.configure(bg=COLOR_BG)

        self.grille = Grille(8, 10)
        self.bateaux = [
            PorteAvion(0, 0),
            Croiseur(0, 0),
            Torpilleur(0, 0),
            SousMarin(0, 0)
        ]

        self.coups = 0
        self.annonces = set()
        self.boutons = []
        self.boat_labels = {}

        self.placer_bateaux()
        self.creer_interface()

    # Placement bateaux
    def zone_autour(self, l, c):
        voisins = []
        for dl in (-1, 0, 1):
            for dc in (-1, 0, 1):
                nl, nc = l + dl, c + dc
                if 0 <= nl < 8 and 0 <= nc < 10:
                    voisins.append((nl, nc))
        return voisins

    def placer_bateaux(self):
        for bateau in self.bateaux:
            placed = False
            while not placed:
                ligne = random.randint(0, 7)
                colonne = random.randint(0, 9)
                vertical = random.choice([True, False])

                bateau.ligne = ligne
                bateau.colonne = colonne
                bateau.vertical = vertical

                valid = True
                for (l, c) in bateau.positions:
                    if l >= 8 or c >= 10:
                        valid = False
                        break
                if not valid:
                    continue

                interdit = False
                for (l, c) in bateau.positions:
                    idx = l * 10 + c
                    if self.grille.matrice[idx] != self.grille.vide:
                        interdit = True
                        break

                    for (vl, vc) in self.zone_autour(l, c):
                        if self.grille.matrice[vl * 10 + vc] in SYMBOLS_BATEAU:
                            interdit = True
                            break

                if interdit:
                    continue

                self.grille.ajoute(bateau)
                placed = True

    # Interface
    def creer_interface(self):
        tk.Label(self.root, text="⚓ Bataille Navale ⚓",
                 font=("Arial", 28, "bold"),
                 fg="white", bg=COLOR_BG).pack(pady=10)

        info_frame = tk.Frame(self.root, bg=COLOR_BG)
        info_frame.pack()

        self.label_coups = tk.Label(
            info_frame, text="Tirs: 0",
            font=("Arial", 14), bg=COLOR_PANEL, fg="white",
            padx=12, pady=5
        )
        self.label_coups.pack(side=tk.LEFT, padx=10)

        self.label_coules = tk.Label(
            info_frame, text=f"Coulés: 0/{len(self.bateaux)}",
            font=("Arial", 14), bg=COLOR_PANEL, fg="white",
            padx=12, pady=5
        )
        self.label_coules.pack(side=tk.LEFT, padx=10)

        tk.Button(
            info_frame, text="🔄 Nouvelle Partie",
            command=self.nouvelle_partie,
            font=("Arial", 12, "bold"),
            bg="#16a34a", fg="white",
            padx=10, pady=5
        ).pack(side=tk.LEFT, padx=10)

        self.label_message = tk.Label(
            self.root, text="", font=("Arial", 16, "bold"),
            bg=COLOR_BG, fg="white", height=2
        )
        self.label_message.pack()

        grille_frame = tk.Frame(self.root, bg=COLOR_BG)
        grille_frame.pack()

        tk.Label(grille_frame, text="", bg=COLOR_BG, width=3).grid(row=0, column=0)
        for j in range(10):
            tk.Label(grille_frame, text=str(j),
                     font=("Arial", 12, "bold"),
                     fg="white", bg=COLOR_BG).grid(row=0, column=j+1)

        for i in range(8):
            tk.Label(grille_frame, text=str(i),
                     font=("Arial", 12, "bold"),
                     fg="white", bg=COLOR_BG).grid(row=i+1, column=0)

            ligne = []
            for j in range(10):
                btn = tk.Button(
                    grille_frame,
                    text="~",
                    width=4, height=2,
                    font=("Arial", 14),
                    bg=COLOR_BLUE, fg="white",
                    activebackground=COLOR_BLUE_HOVER,
                    command=lambda l=i, c=j: self.tirer(l, c)
                )
                btn.grid(row=i+1, column=j+1, padx=1, pady=1)
                ligne.append(btn)
            self.boutons.append(ligne)

        
        flotte_frame = tk.Frame(self.root, bg=COLOR_BG)
        flotte_frame.pack(pady=15)

        tk.Label(flotte_frame, text="Flotte ennemie :",
                 font=("Arial", 16, "bold"),
                 fg="white", bg=COLOR_BG).pack()

        self.flotte_container = tk.Frame(flotte_frame, bg=COLOR_BG)
        self.flotte_container.pack()

        for b in self.bateaux:
            card = tk.Frame(self.flotte_container, bg=COLOR_PANEL,
                            padx=12, pady=6, relief="ridge", bd=2)
            card.pack(side=tk.LEFT, padx=6)

            label = tk.Label(
                card,
                text=f"{b.marque}  {type(b).__name__} ({len(b.positions)})",
                font=("Arial", 12), fg="white", bg=COLOR_PANEL
            )
            label.pack()

            self.boat_labels[id(b)] = label

   
    def tirer(self, l, c):
        idx = l * 10 + c
        case = self.grille.matrice[idx]

        if case in ("💣", "x"):
            self.label_message.config(text="⚠️ Déjà tiré ici !", fg=COLOR_YELLOW)
            return

        self.coups += 1
        self.label_coups.config(text=f"Tirs: {self.coups}")

        if case in SYMBOLS_BATEAU:
            self.grille.matrice[idx] = "💣"
            self.boutons[l][c].config(text="💣", bg=COLOR_GREEN)

            msg = "🎯 Touché !"
            touches = [b for b in self.bateaux if (l, c) in b.positions]

            for b in touches:
                # Bateau COULÉ ?
                if b.coule(self.grille) and id(b) not in self.annonces:
                    self.annonces.add(id(b))
                    msg += f" 💥 {getattr(b, 'message_coule', type(b).__name__+' coulé !')}"

                    # MAJ carte flotte
                    card = self.boat_labels[id(b)]
                    card.config(bg=COLOR_RED, font=("Arial", 12, "overstrike"))

                    # 👉 AFFICHER LE BATEAU COULÉ 🛑
                    for (x, y) in b.positions:
                        self.boutons[x][y].config(
                            text=b.marque,
                            bg=COLOR_RED,
                            fg="white"
                        )

            self.label_coules.config(text=f"Coulés: {len(self.annonces)}/{len(self.bateaux)}")
            self.label_message.config(text=msg, fg=COLOR_GREEN)

            if self.tous_coules():
                self.victoire()

        else:
            self.grille.matrice[idx] = "x"
            self.boutons[l][c].config(text="x", bg=COLOR_CYAN)
            self.label_message.config(text="💦 Plouf !", fg=COLOR_CYAN)

    def tous_coules(self):
        return all(b.coule(self.grille) for b in self.bateaux)

    def victoire(self):
        self.label_message.config(
            text=f"🎉 VICTOIRE ! {self.coups} tirs 🎉",
            fg=COLOR_YELLOW
        )
        for ligne in self.boutons:
            for btn in ligne:
                btn.config(state="disabled")

    def nouvelle_partie(self):
        self.root.destroy()
        root = tk.Tk()
        BatailleNavaleGUI(root)
        root.mainloop()


def main():
    root = tk.Tk()
    BatailleNavaleGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
