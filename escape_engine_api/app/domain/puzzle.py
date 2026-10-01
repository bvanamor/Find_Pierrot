from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.domain.game_element import GameElement


@dataclass
class Puzzle(GameElement, ABC):

    @abstractmethod
    def check_solution(self, answer: str) -> bool:
        pass