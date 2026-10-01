classDiagram

    class GameElement {
        +str id
        +str name
        +str description
        +to_dict() dict
    }

    class Item {
    }

    class Door {
        +bool is_locked
        +Optional~str~ required_item_id
        +unlock(inventory: list[str]) bool
        +to_dict() dict
    }

    class Puzzle {
        <<abstract>>
        +check_solution(answer: str) bool
    }

    class CodePuzzle {
        +str secret_code
        +check_solution(answer: str) bool
    }

    class HashPuzzle {
        +str expected_hash
        +check_solution(answer: str) bool
    }

    class Room {
        +list~GameElement~ items
        +list~Door~ doors
        +list~Puzzle~ puzzles
        +add_item(item: GameElement)
        +add_door(door: Door)
        +add_puzzle(puzzle: Puzzle)
        +to_dict() dict
    }

    class Corridor {
        +str from_room_id
        +str to_room_id
        +to_dict() dict
    }

    class Chest {
        +bool is_locked
        +Optional~str~ required_puzzle_id
        +Optional~str~ reward_item_id
        +open() bool
        +unlock()
        +to_dict() dict
    }

    class Book {
        +bool is_placed_in_library
        +place_in_library()
        +to_dict() dict
    }

    class Library {
        +Optional~str~ required_book_id
        +Optional~str~ reward_item_id
        +bool is_completed
        +place_book(book_id: str) bool
        +to_dict() dict
    }

    GameElement <|-- Item
    GameElement <|-- Door
    GameElement <|-- Puzzle
    GameElement <|-- Room
    GameElement <|-- Corridor
    GameElement <|-- Chest
    GameElement <|-- Book
    GameElement <|-- Library

    Puzzle <|-- CodePuzzle
    Puzzle <|-- HashPuzzle

    Room "1" o-- "*" GameElement : contient
    Room "1" o-- "*" Door : possède
    Room "1" o-- "*" Puzzle : possède

    Corridor --> Room : relie
    Chest --> Puzzle : nécessite
    Library --> Book : accepte