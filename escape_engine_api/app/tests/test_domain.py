from app.domain.item import Item
from app.domain.door import Door
from app.domain.code_puzzle import CodePuzzle
from app.domain.hash_puzzle import HashPuzzle
from app.domain.room import Room


def test_item():
    item = Item(
        id="item_1",
        name="Clé",
        description="Une petite clé."
    )

    result = item.to_dict()

    assert result["id"] == "item_1"
    assert result["name"] == "Clé"


def test_door():
    door = Door(
        id="door_1",
        name="Porte",
        description="Une porte verrouillée.",
        is_locked=True,
        required_item_id="key_1"
    )

    result = door.to_dict()

    assert result["is_locked"] is True
    assert result["required_item_id"] == "key_1"


def test_code_puzzle():
    puzzle = CodePuzzle(
        id="puzzle_1",
        name="Code",
        description="Trouve le code.",
        secret_code="1234"
    )

    assert puzzle.check_solution("1234") is True
    assert puzzle.check_solution("9999") is False


def test_hash_puzzle():
    puzzle = HashPuzzle(
        id="puzzle_2",
        name="Mot secret",
        description="Trouve le mot secret.",
        expected_hash="5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"
    )

    assert puzzle.check_solution("password") is True
    assert puzzle.check_solution("bonjour") is False


def test_room():
    room = Room(
        id="room_1",
        name="Salle 1",
        description="Une salle."
    )

    item = Item(
        id="item_1",
        name="Clé",
        description="Une clé."
    )

    door = Door(
        id="door_1",
        name="Porte",
        description="Une porte."
    )

    puzzle = CodePuzzle(
        id="puzzle_1",
        name="Énigme",
        description="Une énigme.",
        secret_code="1234"
    )

    room.add_item(item)
    room.add_door(door)
    room.add_puzzle(puzzle)

    result = room.to_dict()

    assert len(result["items"]) == 1
    assert len(result["doors"]) == 1
    assert len(result["puzzles"]) == 1