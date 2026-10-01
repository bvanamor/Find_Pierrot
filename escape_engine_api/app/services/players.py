from app.schemas.player import Player


players: dict[str, Player] = {}


def create_player(player: Player) -> Player:
    players[player.id] = player
    return player


def get_player(player_id: str) -> Player | None:
    return players.get(player_id)


def update_player(player_id: str, player: Player) -> Player | None:
    if player_id not in players:
        return None

    players[player_id] = player
    return player


def delete_player(player_id: str) -> bool:
    if player_id not in players:
        return False

    del players[player_id]
    return True

def get_all_players() -> list[Player]:
    return list(players.values())