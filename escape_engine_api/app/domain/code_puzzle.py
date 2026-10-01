from dataclasses import dataclass

from app.domain.puzzle import Puzzle


@dataclass
class CodePuzzle(Puzzle):
    secret_code: str = ""

    def check_solution(self, answer: str) -> bool:
        return answer == self.secret_code