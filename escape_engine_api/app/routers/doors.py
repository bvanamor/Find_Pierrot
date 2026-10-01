from fastapi import APIRouter, HTTPException

from app.services.players import get_player
from app.services.rooms import get_all_rooms


router = APIRouter()


@router.post("/doors/{door_id}/open")
def open_door(door_id: str, player_id: str):

    # 1. Vérifier que le joueur existe
    player = get_player(player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    # 2. Chercher la porte
    door = None

    for room in get_all_rooms():
        for room_door in room.doors:
            if room_door.id == door_id:
                door = room_door
                break

        if door is not None:
            break

    # 3. Vérifier que la porte existe
    if door is None:
        raise HTTPException(
            status_code=404,
            detail="Porte introuvable."
        )

    # 4. Essayer de déverrouiller la porte
    unlocked = door.unlock(player.inventory)

    if not unlocked:
        return {
            "success": False,
            "message": "La porte est verrouillée.",
            "required_item_id": door.required_item_id
        }

    if door.id == "door_3":
        return {
            "success": True,
            "message": "🎉 Félicitations ! Tu as retrouvé Pierrot et terminé le jeu !",
            "game_completed": True,
            "door_id": door.id
        }

    return {
        "success": True,
        "message": "Porte déverrouillée !",
        "game_completed": False,
        "door_id": door.id
    }