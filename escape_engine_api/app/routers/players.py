from fastapi import APIRouter, HTTPException

from app.data import players
from app.models.player import PlayerInput, ScoreUpdate

router = APIRouter(prefix="/players", tags=["Players"])


@router.get("")
def get_players():
    return players


@router.get("/{player_id}")
def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player

    raise HTTPException(
        status_code=404,
        detail="Le joueur n'existe pas"
    )


@router.get("/{player_id}/score")
def get_player_score(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return {
                "player_id": player_id,
                "score": player.get("score", 0),
                "life": player.get("life", True),
                "name": player.get("name", ""),
            }

    return {"erreur": "Le joueur n'existe pas"}


@router.post("")
def create_player(player: PlayerInput):
    new_player = player.model_dump()
    new_player["id"] = len(players) + 1

    players.append(new_player)

    return new_player


@router.put("/{player_id}/score")
def update_player_score(player_id: int, score_update: ScoreUpdate):
    for existing_player in players:
        if existing_player["id"] == player_id:
            if score_update.name is not None:
                existing_player["name"] = score_update.name
            existing_player["score"] = score_update.score
            existing_player["life"] = score_update.life
            return existing_player

    raise HTTPException(
        status_code=404,
        detail="Le joueur n'existe pas",
    )


@router.put("/{player_id}")
def update_player(player_id: int, player: PlayerInput):
    for existing_player in players:
        if existing_player["id"] == player_id:
            existing_player["name"] = player.name
            existing_player["score"] = player.score
            existing_player["life"] = player.life

            return existing_player

    raise HTTPException(
        status_code=404,
        detail="Le joueur n'existe pas",
    )


@router.delete("/{player_id}")
def delete_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            players.remove(player)
            return {"message": "Joueur supprimé"}

    return {"erreur": "Le joueur n'existe pas"}