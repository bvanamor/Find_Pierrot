from dataclasses import dataclass
from typing import Optional

from app.domain.game_element import GameElement


@dataclass
class Library(GameElement):
    required_book_id: Optional[str] = None
    reward_item_id: Optional[str] = None
    is_completed: bool = False

    def place_book(self, book_id: str) -> bool:
        if self.required_book_id != book_id:
            return False

        self.is_completed = True
        return True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "required_book_id": self.required_book_id,
            "reward_item_id": self.reward_item_id,
            "is_completed": self.is_completed
        }