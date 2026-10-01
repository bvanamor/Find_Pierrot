from app.data import players


def get_players():
    return players


def get_player(player_id: int):
    for player in players:
        if player["id"] == player_id:
            return player

    return None


def get_player_score(player_id: int):
    player = get_player(player_id)

    if player is None:
        return None

    return {
        "player_id": player_id,
        "score": player.get("score", 0),
        "life": player.get("life", True),
        "name": player.get("name", ""),
    }


def create_player(name: str, score: int = 0, life: bool = True):
    new_player = {
        "id": len(players) + 1,
        "name": name,
        "score": score,
        "life": life,
    }

    players.append(new_player)

    return new_player


def update_player(
    player_id: int,
    name: str,
    score: int,
    life: bool,
):
    player = get_player(player_id)

    if player is None:
        return None

    player["name"] = name
    player["score"] = score
    player["life"] = life

    return player


def delete_player(player_id: int):
    player = get_player(player_id)

    if player is None:
        return False

    players.remove(player)
    return True

