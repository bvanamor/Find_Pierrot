from pydantic import BaseModel


class ObjetResponse(BaseModel):
    id: int
    salle_id: int
    nom: str
    position: str
    health_effect: bool
    enigme_effect: bool
    points: int


class EnigmeResponse(BaseModel):
    id: int
    salle_id: int
    question: str
    resolue: bool
    recompense: str


class NoteResponse(BaseModel):
    id: int
    salle_id: int
    nom: str
    contenu: str
    points: int


class SalleResponse(BaseModel):
    id: int
    nom: str
    description: str
    terminee: bool
    objets: list[ObjetResponse]
    enigmes: list[EnigmeResponse]
    notes: list[NoteResponse]


class ReponseInput(BaseModel):
    reponse: str


class GameStateResponse(BaseModel):
    player_id: int | None
    player_name: str
    score: int
    life: bool
    etape: int
    salle_actuelle: int
    salle: SalleResponse