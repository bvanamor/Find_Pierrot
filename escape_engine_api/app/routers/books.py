from fastapi import APIRouter, HTTPException

from app.services.players import get_player
from app.services.rooms import get_all_rooms
from app.domain.book import Book

router = APIRouter()


@router.post("/books/{book_id}/take")
def take_book(book_id: str, player_id: str):

    player = get_player(player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    book = None

    for room in get_all_rooms():
        for item in room.items:
            if isinstance(item, Book) and item.id == book_id:
                book = item
                break

        if book is not None:
            break

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Livre introuvable."
        )

    if book_id in player.inventory:
        return {
            "success": True,
            "message": "Le livre est déjà dans votre inventaire.",
            "inventory": player.inventory
        }

    player.inventory.append(book_id)

    return {
        "success": True,
        "message": "Livre récupéré !",
        "item_id": book_id,
        "inventory": player.inventory
    }