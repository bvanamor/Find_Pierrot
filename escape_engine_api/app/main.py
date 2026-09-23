from fastapi import FastAPI
from pydantic import BaseModel
from app.models import PlayerInput
from app.data import players
import requests


class ScoreUpdate(BaseModel):
    score: int
    life: bool = True
    name: str | None = None


app = FastAPI(title="EscapeEngine API Test")

app = FastAPI(
    title="Players API",
    description="API REST de gestion des joueurs",
    version="1.0.0",
)


@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API de Find Pierrot"}


@app.get("/players")
def get_players():
    return players

@app.get("/players/{player_id}")
def get_player(player_id: int):

    for player in players:
        if player["id"] == player_id:
            return player

    return {"erreur": "Le joueur n'existe pas"}


@app.get("/players/{player_id}/score")
def get_player_score(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return {"player_id": player_id, "score": player["score"], "life": player["life"], "name": player["name"]}

    return {"erreur": "Le joueur n'existe pas"}


@app.post("/players")
def create_player(player: PlayerInput):

    new_player = player.model_dump()

    new_player["id"] = len(players) + 1

    players.append(new_player)

    return new_player

@app.put("/players/{player_id}")
def update_player(player_id: int, player: PlayerInput):

    for existing_player in players:
        if existing_player["id"] == player_id:

            existing_player["name"] = player.name
            existing_player["score"] = player.score

            return existing_player

    return {"erreur": "Le joueur n'existe pas"}


@app.put("/players/{player_id}/score")
def update_player_score(player_id: int, score_update: ScoreUpdate):
    for existing_player in players:
        if existing_player["id"] == player_id:
            if score_update.name is not None:
                existing_player["name"] = score_update.name
            existing_player["score"] = score_update.score
            existing_player["life"] = score_update.life
            return existing_player

    return {"erreur": "Le joueur n'existe pas"}


def envoyer_score(self):
    url = f"http://localhost:8000/personnages/{self.id}/score"

    data = {
        "score": self.score
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print("Score envoyé à l'API !")
    else:
        print("Erreur lors de l'envoi du score :", response.status_code)



@app.delete("/players/{player_id}")
def delete_player(player_id: int):

    for player in players:
        if player["id"] == player_id:

            players.remove(player)

            return {"message": "Joueur supprimé avec succès"}

    return {"erreur": "Le joueur n'existe pas"}