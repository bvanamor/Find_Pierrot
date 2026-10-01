from fastapi import APIRouter, HTTPException

from app.services.players import get_player
from app.services.rooms import get_all_rooms
from app.domain.library import Library

router = APIRouter()


@router.post("/libraries/{library_id}/place-book")
def place_book(library_id: str, player_id: str, book_id: str):

    player = get_player(player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    library = None

    for room in get_all_rooms():
        for item in room.items:
            if isinstance(item, Library) and item.id == library_id:
                library = item
                break

        if library is not None:
            break

    if library is None:
        raise HTTPException(
            status_code=404,
            detail="Bibliothèque introuvable."
        )

    if book_id not in player.inventory:
        return {
            "success": False,
            "message": "Vous n'avez pas ce livre dans votre inventaire."
        }

    if library.is_completed:
        return {
            "success": True,
            "message": "La bibliothèque est déjà complétée.",
            "reward_item_id": library.reward_item_id
        }

    success = library.place_book(book_id)

    if not success:
        return {
            "success": False,
            "message": "Ce livre ne correspond pas à la bibliothèque."
        }

    if library.reward_item_id is not None:
        if library.reward_item_id not in player.inventory:
            player.inventory.append(library.reward_item_id)

    return {
        "success": True,
        "message": "Le livre a été placé dans la bibliothèque !",
        "reward_item_id": library.reward_item_id,
        "inventory": player.inventory
    }