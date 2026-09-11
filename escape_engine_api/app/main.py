from fastapi import FastAPI
from app.models import Player
from app.data import players


app = FastAPI(title="EscapeEngine API Test")

app = FastAPI(
    title="Players API",
    description="API REST de gestion des joueurs",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API d'ajout de joueurs"}


@app.get("/players")
def get_players():
    return players

@app.get("/players/{player_id}")
def get_player(player_id: int):

    for player in players:
        if player["id"] == player_id:
            return player

    return {"erreur": "Le joueur n'existe pas"}


@app.post("/players")
def create_player(player: Player):

    new_player = player.model_dump()

    new_player["id"] = len(players) + 1

    players.append(new_player)

    return new_player

@app.put("/players/{player_id}")
def update_player(player_id: int, player: Player):

    for existing_player in players:
        if existing_player["id"] == player_id:

            existing_player["name"] = player.name
            existing_player["score"] = player.score

            return existing_player

    return {"erreur": "Le joueur n'existe pas"}


@app.delete("/players/{player_id}")
def delete_player(player_id: int):

    for player in players:
        if player["id"] == player_id:

            players.remove(player)

            return {"message": "Joueur supprimé avec succès"}

    return {"erreur": "Le joueur n'existe pas"}