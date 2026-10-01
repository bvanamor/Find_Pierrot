from dataclasses import dataclass

from app.domain.game_element import GameElement


@dataclass
class Corridor(GameElement):
    from_room_id: str = ""
    to_room_id: str = ""

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "from_room_id": self.from_room_id,
            "to_room_id": self.to_room_id
        }