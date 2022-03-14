import requests

from wiseoldman_py.wom_exceptions import PlayerNotFoundError

from .groups import Group
from .player import Player


class WiseOldMan:
    """Core WiseOldMan-Py"""

    def __init__(self) -> None:
        self.base_url = "https://api.wiseoldman.net"

    def get_player(self, *, username: str | None = None, user_id: int | None = None) -> Player:
        """Searches WOM for player, returns Player with latest snapshot"""
        if username is None and user_id is None:
            raise ValueError("Either a username or user id must be provided")

        player_json = {}
        if username:
            player_json = requests.get(f"{self.base_url}/players/username/{username}").json()
        if user_id or (username and user_id):
            player_json = requests.get(f"{self.base_url}/players/{user_id}").json()

        # ? Maybe this could be made into a validator within the
        # ? Player model but idk how right now
        if player_json.get("message", None):
            message = player_json["message"]
            if message == "Player not found.":
                raise PlayerNotFoundError(f"Player not found.")

        return Player(**player_json)

    def get_group(self, *, group_id: int | None) -> Group:
        """Searches WOM for group, returns Group"""
        if group_id is None:
            raise ValueError("A group id must be provided")

        group_json = requests.get(f"{self.base_url}/groups/{id}").json()

        # TODO: handel if group not found

        return Group(**group_json)
