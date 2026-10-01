from pydantic import BaseModel, field_validator


class PuzzleSubmission(BaseModel):
    puzzle_id: str
    attempt_code: str
    player_id: str

    @field_validator("attempt_code")
    @classmethod
    def attempt_code_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Le code ne peut pas être vide.")

        return value