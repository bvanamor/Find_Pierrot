from fastapi import APIRouter, HTTPException

from app.schemas.chest import ChestOpenSubmission
from app.services.rooms import get_chest_by_id, get_all_rooms
from app.services.players import get_player


router = APIRouter()


@router.post("/chests/{chest_id}/open")
def open_chest(chest_id: str, submission: ChestOpenSubmission):

    # 1. Vérifier que le joueur existe
    player = get_player(submission.player_id)

    if player is None:
        raise HTTPException(
            status_code=404,
            detail="Joueur introuvable."
        )

    # 2. Vérifier que le coffre existe
    chest = get_chest_by_id(chest_id)

    if chest is None:
        raise HTTPException(
            status_code=404,
            detail="Coffre introuvable."
        )

    # 3. Vérifier si le coffre est déjà ouvert
    if not chest.is_locked:
        return {
            "success": True,
            "message": "Le coffre est déjà ouvert.",
            "reward_item_id": chest.reward_item_id
        }

    # 4. Chercher l'énigme associée au coffre
    puzzle = None

    for room in get_all_rooms():
        for room_puzzle in room.puzzles:
            if room_puzzle.id == chest.required_puzzle_id:
                puzzle = room_puzzle
                break

        if puzzle is not None:
            break

    # 5. Vérifier que l'énigme existe
    if puzzle is None:
        raise HTTPException(
            status_code=404,
            detail="Énigme du coffre introuvable."
        )

    # 6. Vérifier la réponse
    if not puzzle.check_solution(submission.attempt_code):
        return {
            "success": False,
            "message": "Mauvaise réponse."
        }

    # 7. Déverrouiller le coffre
    chest.unlock()

    # 8. Donner la récompense au joueur
    if chest.reward_item_id is not None:
        if chest.reward_item_id not in player.inventory:
            player.inventory.append(chest.reward_item_id)

    return {
        "success": True,
        "message": "Coffre ouvert !",
        "reward_item_id": chest.reward_item_id,
        "inventory": player.inventory
    }