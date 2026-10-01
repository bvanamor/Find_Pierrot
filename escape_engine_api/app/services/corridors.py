from app.domain.corridor import Corridor


corridors = [
    Corridor(
        id="corridor_1",
        name="Couloir sombre",
        description="Un long couloir mal éclairé.",
        from_room_id="room_1",
        to_room_id="room_2"
    ),
    Corridor(
        id="corridor_2",
        name="Couloir de la bibliothèque",
        description="Un couloir menant vers la dernière salle.",
        from_room_id="room_2",
        to_room_id="room_3"
    )
]


def get_all_corridors() -> list[Corridor]:
    return corridors


def get_corridor_by_id(corridor_id: str) -> Corridor | None:
    for corridor in corridors:
        if corridor.id == corridor_id:
            return corridor

    return None