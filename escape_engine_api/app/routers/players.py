from fastapi import APIRouter, HTTPException

from app.schemas.player import Player, PlayerCreate
from app.services.players import (
    create_player,
    get_player,
    get_all_players,
    update_player,
    delete_player
)


router = APIRouter()


@router.post("/players")
def create_player_route(player: PlayerCreate):
    new_player = Player(
        id=f"player_{len(get_all_players()) + 1}",
        name=player.name
    )

    return create_player(new_player)


@router.get("/players/{player_id}")
def get_player_route(player_id: str):
    player = get_player(player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    return player


@router.put("/players/{player_id}")
def update_player_route(player_id: str, player: Player):
    updated_player = update_player(player_id, player)

    if updated_player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    return updated_player


@router.delete("/players/{player_id}")
def delete_player_route(player_id: str):
    deleted = delete_player(player_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    return {
        "message": "Joueur supprimé."
    }