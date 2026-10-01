# 🔎 Find Pierrot

> Escape Game développé en Python avec FastAPI, dans le cadre d'un
> projet de cybersécurité / développement.

**Find Pierrot** est un Escape Game backend dans lequel le joueur doit
résoudre plusieurs énigmes, récupérer des objets et progresser à travers
trois salles afin de terminer le jeu.

------------------------------------------------------------------------

## 🎮 Présentation

Le joueur commence dans une salle d'archives et doit progresser dans le
jeu en :

-   🧩 résolvant des énigmes ;
-   🔑 récupérant des morceaux de clé ;
-   🚪 déverrouillant des portes ;
-   📦 ouvrant un coffre ;
-   📖 récupérant un livre ;
-   📚 plaçant le livre dans une bibliothèque ;
-   🔑 récupérant la clé finale ;
-   🎉 ouvrant la porte finale pour terminer le jeu.

Le backend expose une API REST documentée automatiquement avec **Swagger
/ OpenAPI**.

------------------------------------------------------------------------

## 🗺️ Parcours du jeu

``` text
🏛️ Salle 1 — Les archives
        │
        ├── 🧩 Énigme : code 1234
        │
        └── 🔑 key_part_1
                │
                ▼
        🚪 Porte du couloir
                │
                ▼
🏛️ Salle 2 — La salle du coffre
        │
        ├── 🧩 Énigme Hash
        │
        ├── 📦 Coffre
        │
        └── 🔑 key_part_2
                │
                ▼
        🚪 Porte de sortie
                │
                ▼
🏛️ Salle 3 — La bibliothèque
        │
        ├── 📖 Le livre mystérieux
        │
        ├── 📚 Bibliothèque
        │
        └── 🔑 final_key
                │
                ▼
        🚪 Porte finale
                │
                ▼
        🎉 FIN DU JEU
```

------------------------------------------------------------------------

## 🧰 Technologies utilisées

  Technologie            Utilisation
  ---------------------- ----------------------------------------
  🐍 Python              Langage principal
  ⚡ FastAPI             Création de l'API REST
  📚 Pydantic            Validation des données
  🧪 Pytest              Tests unitaires
  📖 Swagger / OpenAPI   Documentation et test de l'API
  🧱 Dataclasses         Modélisation des éléments du jeu
  🧬 POO                 Héritage, abstraction et polymorphisme
  🔐 SHA-256             Vérification de l'énigme Hash
  🐧 Linux               Environnement de développement
  🌱 Git                 Gestion du code et des branches

------------------------------------------------------------------------

## 🏗️ Architecture du projet

``` text
escape_engine_api/
│
├── app/
│   │
│   ├── domain/              # Logique métier et objets du jeu
│   │   ├── game_element.py
│   │   ├── item.py
│   │   ├── door.py
│   │   ├── puzzle.py
│   │   ├── code_puzzle.py
│   │   ├── hash_puzzle.py
│   │   ├── room.py
│   │   ├── corridor.py
│   │   ├── chest.py
│   │   ├── book.py
│   │   ├── library.py
│   │   └── diagram.md
│   │
│   ├── routers/             # Routes HTTP de l'API
│   │   ├── puzzles.py
│   │   ├── rooms.py
│   │   ├── players.py
│   │   ├── corridors.py
│   │   ├── chests.py
│   │   ├── doors.py
│   │   ├── books.py
│   │   └── libraries.py
│   │
│   ├── schemas/             # Modèles Pydantic
│   │   ├── puzzle.py
│   │   ├── player.py
│   │   └── chest.py
│   │
│   ├── services/            # Gestion des données et logique applicative
│   │   ├── rooms.py
│   │   ├── players.py
│   │   └── corridors.py
│   │
│   ├── tests/
│   │   └── test_domain.py
│   │
│   └── main.py              # Point d'entrée FastAPI
│
├── environment.yml
├── .env
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 🧱 Modèle objet

Le projet utilise la programmation orientée objet.

La classe principale est :

``` text
GameElement
├── Item
├── Door
├── Puzzle
│   ├── CodePuzzle
│   └── HashPuzzle
├── Room
├── Corridor
├── Chest
├── Book
└── Library
```

### Puzzle

`Puzzle` est une classe abstraite.

Elle définit la méthode :

``` python
check_solution(answer: str) -> bool
```

Deux types d'énigmes sont disponibles :

-   `CodePuzzle` : compare une réponse avec un code secret.
-   `HashPuzzle` : calcule le SHA-256 de la réponse et le compare au
    hash attendu.

------------------------------------------------------------------------

## 🚀 Installation

### 1. Cloner le projet

``` bash
git clone <URL_DU_DEPOT>
cd escape_engine_api
```

### 2. Installer les dépendances

Si l'environnement Python du projet est déjà configuré, active-le puis
installe les dépendances nécessaires.

Pour une installation classique :

``` bash
pip install fastapi uvicorn pytest
```

### 3. Lancer le serveur

Depuis la racine du projet :

``` bash
uvicorn app.main:app --reload
```

Le serveur est alors disponible sur :

``` text
http://127.0.0.1:8000
```

------------------------------------------------------------------------

## 📖 Documentation API

Une fois le serveur lancé :

### Swagger UI

``` text
http://127.0.0.1:8000/docs
```

### OpenAPI

``` text
http://127.0.0.1:8000/openapi.json
```

------------------------------------------------------------------------

## 🔌 Principales routes

### Système

``` http
GET /health
```

Retourne l'état du moteur de jeu.

### Salles

``` http
GET /rooms
GET /rooms/{room_id}
```

### Couloirs

``` http
GET /corridors
GET /corridors/{corridor_id}
```

### Joueurs

``` http
POST /players
GET /players/{player_id}
PUT /players/{player_id}
DELETE /players/{player_id}
```

### Énigmes

``` http
POST /puzzles/submit
```

### Coffres

``` http
POST /chests/{chest_id}/open
```

### Portes

``` http
POST /doors/{door_id}/open
```

### Livres

``` http
POST /books/{book_id}/take
```

### Bibliothèques

``` http
POST /libraries/{library_id}/place-book
```

------------------------------------------------------------------------

## 🧪 Tests

Les tests du domaine sont réalisés avec Pytest.

Lancer les tests :

``` bash
pytest
```

Résultat actuel :

``` text
5 passed
```

Les tests couvrent notamment :

-   `Item`
-   `Door`
-   `CodePuzzle`
-   `HashPuzzle`
-   `Room`

------------------------------------------------------------------------

## 🔐 Validation des données

Les données envoyées à certaines routes sont validées avec **Pydantic**.

Par exemple, une tentative d'énigme vide est refusée :

``` json
{
  "puzzle_id": "puzzle_1",
  "attempt_code": "",
  "player_id": "player_1"
}
```

L'API retourne alors :

``` text
422 Unprocessable Entity
```

------------------------------------------------------------------------

## 👤 Gestion du joueur

Chaque joueur possède :

``` json
{
  "id": "player_1",
  "name": "Van",
  "inventory": []
}
```

L'inventaire permet notamment de conserver :

``` text
key_part_1
key_part_2
book_1
final_key
```

Les joueurs sont actuellement stockés **en mémoire**. Un redémarrage du
serveur réinitialise donc les joueurs et leur inventaire.

------------------------------------------------------------------------

## 🎯 Objectifs techniques du projet

Ce projet permet de mettre en pratique :

-   la programmation orientée objet ;
-   les classes et les dataclasses ;
-   l'héritage ;
-   l'abstraction ;
-   le polymorphisme ;
-   les type hints ;
-   la création d'une API REST ;
-   FastAPI ;
-   Pydantic ;
-   la validation des données ;
-   les tests unitaires avec Pytest ;
-   la documentation OpenAPI ;
-   Git et la gestion des branches.

------------------------------------------------------------------------

## 📊 Diagramme UML

Le diagramme UML du domaine est disponible ici :

``` text
app/domain/diagram.md
```

Il représente les principales relations entre :

-   `GameElement`
-   `Item`
-   `Door`
-   `Puzzle`
-   `CodePuzzle`
-   `HashPuzzle`
-   `Room`
-   `Corridor`
-   `Chest`
-   `Book`
-   `Library`

------------------------------------------------------------------------

## 🌱 Git

Le développement est organisé avec Git.

Branche actuelle de développement :

``` text
feature/game-management
```

Exemple de workflow :

``` bash
git status
git add .
git commit -m "message"
git push
```

------------------------------------------------------------------------

## 👨‍💻 Auteur

**Van Christ Amor Junior BALOUCKOU**

Étudiant en cybersécurité --- Ynov Campus Nantes.

Projet réalisé dans le cadre de la formation en cybersécurité et
développement.

------------------------------------------------------------------------

## 📌 Statut du projet

**Backend fonctionnel ✅**

-   [x] Architecture POO
-   [x] API FastAPI
-   [x] 3 salles
-   [x] Couloirs
-   [x] Énigmes
-   [x] Coffre
-   [x] Gestion des joueurs
-   [x] Inventaire
-   [x] Livre
-   [x] Bibliothèque
-   [x] Porte finale
-   [x] Fin du jeu
-   [x] Tests Pytest
-   [x] Documentation Swagger
-   [x] Diagramme UML

### 🚧 Prochaine évolution

Connexion du backend à une interface frontend afin de transformer l'API
en véritable interface de jeu **Find Pierrot**.
