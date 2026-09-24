from fastapi import APIRouter

from app.data import players
from app.game import Game
from app.Perso import Perso
from app.models.game import (
    ObjetResponse,
    EnigmeResponse,
    NoteResponse,
    SalleResponse,
    ReponseInput,
    GameStateResponse,
)

from app.services.game_service import GameService


premier_joueur = next(
    (player for player in players if player["id"] == 1),
    None,
)
game_service = GameService(
    Game(
        joueur=Perso.depuis_joueur_api(premier_joueur)
        if premier_joueur is not None
        else None
    )
)

router = APIRouter(tags=["Game"])


@router.get("/objets", response_model=list[ObjetResponse])
def get_all_objets():
    return game_service.get_objets()


@router.get("/objets/{objet_id}", response_model=ObjetResponse)
def get_one_objet(objet_id: int):
    return game_service.get_objet(objet_id)


@router.get("/salles", response_model=list[SalleResponse])
def get_all_salles():
    return game_service.get_salles()


@router.get("/salles/{salle_id}", response_model=SalleResponse)
def get_one_salle(salle_id: int):
    return game_service.get_salle(salle_id)


@router.get("/salles/{salle_id}/objets")
def get_objects_from_salle(salle_id: int):
    return game_service.get_salle_objets(salle_id)


@router.get("/salles/{salle_id}/enigmes")
def get_enigmes_from_salle(salle_id: int):
    return game_service.get_salle_enigmes(salle_id)


@router.get("/salles/{salle_id}/notes")
def get_notes_from_salle(salle_id: int):
    return game_service.get_salle_notes(salle_id)


@router.get("/enigmes", response_model=list[EnigmeResponse])
def get_all_enigmes():
    return game_service.get_enigmes()


@router.get("/enigmes/{enigme_id}", response_model=EnigmeResponse)
def get_one_enigme(enigme_id: int):
    return game_service.get_enigme(enigme_id)


@router.get("/notes", response_model=list[NoteResponse])
def get_all_notes():
    return game_service.get_notes()


@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_one_note(note_id: int):
    return game_service.get_note(note_id)


@router.get("/game/state", response_model=GameStateResponse)
def get_state():
    return game_service.get_game_state()


@router.post("/game/answer", response_model=GameStateResponse)
def answer(answer: ReponseInput):
    return game_service.answer_enigme(answer.reponse)


@router.post(
    "/game/objects/{objet_id}/pickup",
    response_model=GameStateResponse,
)
def pickup(objet_id: int):
    return game_service.pickup_object(objet_id)