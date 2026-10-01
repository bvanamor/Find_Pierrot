from pydantic import BaseModel


class PlayerInput(BaseModel):
    name: str
    score: int = 0
    life: bool = True


class ScoreUpdate(BaseModel):
    score: int
    life: bool = True
    name: str | None = None