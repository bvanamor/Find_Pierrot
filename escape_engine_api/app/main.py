from fastapi import FastAPI
from pydantic import BaseModel

from app.data import players
from app.models.enigme import Enigme
from app.models.note import Note
from app.services.game import Game


class PlayerInput(BaseModel):
    name: str
    score: int = 0
    life: bool = True


class ScoreUpdate(BaseModel):
    score: int
    life: bool = True
    name: str | None = None


print("MAIN.PY EST LANCÉ")

game = Game()

enigme1 = Enigme(
    "Combien font 2 + 3 ?",
    "5",
    "PARTIE_CLE_1",
)

game.ajouter_enigme(enigme1)

note1 = Note(
    "Indice mystérieux",
    "Le résultat se trouve en additionnant les deux nombres.",
)

game.ajouter_note(note1)


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


@app.get("/players/{player_id}/score")
def get_player_score(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return {"player_id": player_id, "score": player["score"], "life": player.get("life", True), "name": player["name"]}
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
            existing_player["life"] = player.life
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


@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            players.remove(player)
            return {"message": "Joueur supprimé avec succès"}
    return {"erreur": "Le joueur n'existe pas"}

