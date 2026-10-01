from dataclasses import dataclass


@dataclass
class GameElement:
    id: str
    name: str
    description: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }