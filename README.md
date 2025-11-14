# Bataille Navale – Projet Python

Ce projet propose une implémentation complète du jeu **Bataille Navale** en Python.  
Il contient deux versions :  
- une version **console**, jouable dans le terminal ;  
- une version **graphique Tkinter**, inspirée d'une interface moderne.

---

## 1. Description du jeu

Le jeu consiste à trouver et couler plusieurs bateaux placés aléatoirement sur une grille.  
À chaque tir, le programme indique si le joueur a touché, raté ou coulé un bateau.  
La partie se termine lorsque **tous les bateaux sont détruits**.

Les bateaux restent invisibles tant qu’ils ne sont pas complètement coulés.

---

## 2. Fonctionnalités principales

### ✔ Version console
- Affichage de la grille dans le terminal  
- Placement aléatoire des bateaux sans chevauchement  
- Saisie des tirs au format `ligne,colonne`  
- Détection : *Plouf*, *Touché*, *Coulé*  
- Compteur de tirs  
- Messages spécifiques selon le bateau coulé  

### ✔ Version Tkinter
- Interface graphique composée de boutons interactifs  
- Couleurs distinctes pour les tirs : touché, plouf, coulé  
- Affichage des bateaux uniquement lorsqu'ils sont coulés  
- Suivi en temps réel : nombre de tirs, bateaux coulés  
- Liste des bateaux mise à jour automatiquement  
- Bouton pour démarrer une nouvelle partie  

---

## 3. Types de bateaux

| Bateau       | Longueur | Symbole | Message de coulé |
|--------------|----------|---------|------------------|
| Porte-Avion  | 4 cases  | 🚢      | Le Porte-Avion a sombré ! |
| Croiseur     | 3 cases  | ⛴      | Le Croiseur a été coulé ! |
| Torpilleur   | 2 cases  | 🚣      | Le Torpilleur a disparu sous l'eau ! |
| Sous-Marin   | 2 cases  | 🐟      | Le Sous-Marin est perdu dans les profondeurs ! |

---


## 4. Structure du projet

```
bataille-navale/
│── main.py            # la partie principale du jeu
│── interface.py       # version graphique Tkinter
│── grille.py          # gestion de la grille et des tirs
│── bateau.py          # définition des bateaux
│── test_grille.py     # tests unitaires
│── test_bateau.py     # tests unitaires
│── story_bateau.py    # user story : chevauchement
│── story_grille.py    # user story : tirs (plouf)
│── README.md
```

---


## 5. Exécution du jeu

### ▶ Version console
```bash
python main.py
```
### ▶ Version graphique
```bash
python interface.py
```
---

## Auteur  

Projet réalisé par **Salima Naimi**  
Élève ingénieure à l’**École Centrale Méditerranée**  
Dans le cadre de la matière **Coder et Développer en Python**  
Année académique **2025–2026**  

