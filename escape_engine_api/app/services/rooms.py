from app.domain.room import Room
from app.domain.item import Item
from app.domain.door import Door
from app.domain.code_puzzle import CodePuzzle
from app.domain.hash_puzzle import HashPuzzle
from app.domain.chest import Chest
from app.domain.book import Book
from app.domain.library import Library


room_1 = Room(
    id="room_1",
    name="Les archives",
    description="Une pièce sombre remplie de vieux documents."
)

room_1.add_item(
    Item(
        id="key_part_1",
        name="Morceau de clé",
        description="Une partie de la clé permettant de progresser."
    )
)

room_1.add_door(
    Door(
        id="door_1",
        name="Porte du couloir",
        description="Une porte verrouillée.",
        is_locked=True,
        required_item_id="key_part_1"
    )
)

room_1.add_puzzle(
    CodePuzzle(
        id="puzzle_1",
        name="Le code des archives",
        description="Trouve le code caché dans les archives.",
        secret_code="1234"
    )
)


room_2 = Room(
    id="room_2",
    name="La salle du coffre",
    description="Une salle contenant un mystérieux coffre."
)

room_2.add_item(
    Item(
        id="key_part_2",
        name="Deuxième morceau de clé",
        description="Le deuxième morceau de la clé."
    )
)

room_2.add_item(
    Chest(
        id="chest_1",
        name="Vieux coffre",
        description="Un coffre poussiéreux contenant un morceau de clé.",
        is_locked=True,
        required_puzzle_id="puzzle_2",
        reward_item_id="key_part_2"
    )
)

room_2.add_door(
    Door(
        id="door_2",
        name="Porte de sortie",
        description="Une porte menant vers la dernière salle.",
        is_locked=True,
        required_item_id="key_part_2"
    )
)

room_2.add_puzzle(
    HashPuzzle(
        id="puzzle_2",
        name="Le mot secret",
        description="Trouve le mot permettant d'ouvrir le coffre.",
        expected_hash="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    )
)

room_3 = Room(
    id="room_3",
    name="La bibliothèque",
    description="Une immense bibliothèque remplie de vieux livres."
)

room_3.add_item(
    Book(
        id="book_1",
        name="Le livre mystérieux",
        description="Un vieux livre couvert de poussière."
    )
)

room_3.add_item(
    Library(
        id="library_1",
        name="Bibliothèque ancienne",
        description="Une bibliothèque qui semble attendre un livre précis.",
        required_book_id="book_1",
        reward_item_id="final_key"
    )
)

room_3.add_door(
    Door(
        id="door_3",
        name="Porte finale",
        description="Une grande porte menant vers la sortie.",
        is_locked=True,
        required_item_id="final_key"
    )
)


rooms = [
    room_1,
    room_2,
    room_3
]


def get_all_rooms() -> list[Room]:
    return rooms


def get_room_by_id(room_id: str) -> Room | None:
    for room in rooms:
        if room.id == room_id:
            return room

    return None

def get_chest_by_id(chest_id: str) -> Chest | None:
    for room in rooms:
        for item in room.items:
            if isinstance(item, Chest) and item.id == chest_id:
                return item

    return None