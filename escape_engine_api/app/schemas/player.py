from pydantic import BaseModel, Field


class Player(BaseModel):
    id: str
    name: str
    inventory: list[str] = Field(default_factory=list)


class PlayerCreate(BaseModel):
    name: str