from dataclasses import dataclass
from typing import Optional

from app.domain.game_element import GameElement


@dataclass
class Chest(GameElement):
    is_locked: bool = True
    required_puzzle_id: Optional[str] = None
    reward_item_id: Optional[str] = None

    def open(self) -> bool:
        if self.is_locked:
            return False

        return True

    def unlock(self) -> None:
        self.is_locked = False

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_locked": self.is_locked,
            "required_puzzle_id": self.required_puzzle_id,
            "reward_item_id": self.reward_item_id
        }