import requests

from .player import Player


class WiseOldMan:
    """Core WiseOldMan-Py"""

    def __init__(self) -> None:
        self.base_url = "https://api.wiseoldman.net"

    def get_player(self, *, osrs_username: str | None = None, osrs_user_id: int | None = None) -> Player:
        """Searches WOM for player, returns Player with latest snapshot"""
        if osrs_username is None and osrs_user_id is None:
            raise ValueError("Either a username or user id must be provided")

        player_json = {}
        if osrs_username:
            player_json = requests.get(f"{self.base_url}/players/username/{osrs_username}").json()
        if osrs_user_id:
            player_json = requests.get(f"{self.base_url}/players/{osrs_user_id}").json()

        return Player(**player_json)
