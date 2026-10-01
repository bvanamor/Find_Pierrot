from fastapi import APIRouter, HTTPException

from app.services.rooms import get_all_rooms, get_room_by_id


router = APIRouter()


@router.get("/rooms")
def get_rooms():
    rooms = get_all_rooms()

    return [room.to_dict() for room in rooms]


@router.get("/rooms/{room_id}")
def get_room(room_id: str):
    room = get_room_by_id(room_id)

    if room is None:
        raise HTTPException(
            status_code=404,
            detail="Salle introuvable."
        )

    return room.to_dict()