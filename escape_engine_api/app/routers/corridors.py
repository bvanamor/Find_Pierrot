from fastapi import APIRouter, HTTPException

from app.services.corridors import (
    get_all_corridors,
    get_corridor_by_id
)


router = APIRouter()


@router.get("/corridors")
def get_corridors():
    corridors = get_all_corridors()

    return [corridor.to_dict() for corridor in corridors]


@router.get("/corridors/{corridor_id}")
def get_corridor(corridor_id: str):
    corridor = get_corridor_by_id(corridor_id)

    if corridor is None:
        raise HTTPException(
            status_code=404,
            detail="Couloir introuvable."
        )

    return corridor.to_dict()