from fastapi import APIRouter, HTTPException

from app.domain.code_puzzle import CodePuzzle
from app.schemas.puzzle import PuzzleSubmission


router = APIRouter()


puzzle = CodePuzzle(
    id="puzzle_1",
    name="Énigme des archives",
    description="Trouve le code caché dans les archives.",
    secret_code="1234"
)


@router.post("/puzzles/submit")
def submit_puzzle(submission: PuzzleSubmission):
    if submission.puzzle_id != puzzle.id:
        raise HTTPException(
            status_code=404,
            detail="Énigme introuvable."
        )

    success = puzzle.check_solution(submission.attempt_code)

    if success:
        return {
            "success": True,
            "message": "Porte déverrouillée !"
        }

    return {
        "success": False,
        "message": "Mauvaise réponse."
    }