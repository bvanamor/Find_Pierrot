print("MAIN.PY EST LANCÉ")

from app.models.enigme import Enigme
from app.models.note import Note
from app.services.game import Game

game = Game()

enigme1 = Enigme(
    "Combien font 2 + 3 ?",
    "5",
    "PARTIE_CLE_1"
)

game.ajouter_enigme(enigme1)

note1 = Note(
    "Indice mystérieux",
    "Le résultat se trouve en additionnant les deux nombres."
)

game.ajouter_note(note1)
