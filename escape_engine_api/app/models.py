from pydantic import BaseModel, Field


class Player(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(min_length=3)
    score: int = Field(ge=0)
    level: int = Field(ge=1)


class PlayerInput(BaseModel):
    name: str = Field(min_length=3)
    score: int = Field(ge=0)
    level: int = Field(ge=1)