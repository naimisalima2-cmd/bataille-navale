# Bataille Navale – Projet Python

Ce projet est une implémentation du jeu **Bataille Navale** en Python, jouable dans le terminal.  
L’objectif est de créer un petit jeu complet en console en utilisant une structure de code organisée (classes, fichiers séparés, tests, etc.).

---

## 1. Description du jeu

Le joueur doit trouver et couler plusieurs bateaux placés aléatoirement sur une grille.  
À chaque tour, il saisit une position **ligne,colonne** (ex : `3,7`) et le programme indique s’il a touché ou raté un bateau.

Le jeu se termine lorsque **tous les bateaux sont coulés**.

---

## 2. Fonctionnalités

- Placement aléatoire des bateaux  
- Aucun chevauchement entre les bateaux  
- Les bateaux restent cachés tant qu’ils ne sont pas coulés  
- Messages spécifiques selon le bateau détruit  
- Comptage du nombre total de tirs  

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

python main.py

---

## Auteur  

Projet réalisé par **Salima Naimi**  
Élève ingénieure à l’**École Centrale Méditerranée**  
Dans le cadre de la matière **Coder et Développer en Python**  
Année académique **2025–2026**  

