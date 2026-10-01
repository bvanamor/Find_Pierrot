from dataclasses import dataclass
from typing import Optional

from app.domain.game_element import GameElement


@dataclass
class Door(GameElement):
    is_locked: bool = True
    required_item_id: Optional[str] = None

    def unlock(self, inventory: list[str]) -> bool:
        if not self.is_locked:
            return True

        if self.required_item_id is None:
            self.is_locked = False
            return True

        if self.required_item_id in inventory:
            self.is_locked = False
            return True

        return False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_locked": self.is_locked,
            "required_item_id": self.required_item_id
        }