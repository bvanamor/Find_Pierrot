from dataclasses import dataclass

from app.domain.game_element import GameElement


@dataclass
class Book(GameElement):
    is_placed_in_library: bool = False

    def place_in_library(self) -> None:
        self.is_placed_in_library = True

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_placed_in_library": self.is_placed_in_library
        }