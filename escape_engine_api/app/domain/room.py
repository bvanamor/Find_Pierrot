from dataclasses import dataclass, field

from app.domain.game_element import GameElement
from app.domain.door import Door
from app.domain.puzzle import Puzzle


@dataclass
class Room(GameElement):
    items: list[GameElement] = field(default_factory=list)
    doors: list[Door] = field(default_factory=list)
    puzzles: list[Puzzle] = field(default_factory=list)

    def add_item(self, item: GameElement) -> None:
        self.items.append(item)

    def add_door(self, door: Door) -> None:
        self.doors.append(door)

    def add_puzzle(self, puzzle: Puzzle) -> None:
        self.puzzles.append(puzzle)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "items": [item.to_dict() for item in self.items],
            "doors": [door.to_dict() for door in self.doors],
            "puzzles": [puzzle.to_dict() for puzzle in self.puzzles],
        }