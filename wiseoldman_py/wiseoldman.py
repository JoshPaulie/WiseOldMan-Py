import requests

from .player import Achievement, Player


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
        if user_id:
            player_json = requests.get(f"{self.base_url}/players/{user_id}").json()

        return Player(**player_json)

    def get_player_achievements(
        self, *, username: str | None = None, user_id: int | None = None
    ) -> list[Achievement]:
        """Searches WOM for player, returns Player with latest snapshot"""
        if username is None and user_id is None:
            raise ValueError("Either a username or user id must be provided")

        player_json = {}
        if username:
            player_json = requests.get(f"{self.base_url}/players/username/{username}/achievements").json()
        if user_id:
            player_json = requests.get(f"{self.base_url}/players/{user_id}/achievements").json()

        achievements = []
        for a in player_json:
            achievements.append(Achievement(**a))

        return achievements
