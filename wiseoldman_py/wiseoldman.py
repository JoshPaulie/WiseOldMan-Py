import requests

from wiseoldman_py.wom_exceptions import PlayerNotFoundError

from .groups import Group
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

        if player_json.get("message", None):
            message = player_json["message"]
            if message == "Player not found.":
                raise PlayerNotFoundError(f"Player not found.")

        return Player(**player_json)

    def get_player_achievements(
        self, *, username: str | None = None, user_id: int | None = None
    ) -> list[Achievement]:
        """Searches WOM for player, returns Player with latest snapshot"""
        if username is None and user_id is None:
            raise ValueError("Either a username or user id must be provided")

        player_achievement_json = {}
        if username:
            player_achievement_json = requests.get(
                f"{self.base_url}/players/username/{username}/achievements"
            ).json()
        if user_id:
            player_achievement_json = requests.get(f"{self.base_url}/players/{user_id}/achievements").json()

        if isinstance(player_achievement_json, dict):
            if player_achievement_json.get("message", None):
                message = player_achievement_json["message"]
                if message == "Player not found.":
                    raise PlayerNotFoundError(f"Player not found.")

        # ? No comp to make sure an empty list can be returned
        achievements = []
        for a in player_achievement_json:
            achievements.append(Achievement(**a))

        return achievements

    def get_group(self, *, group_id: int | None) -> Group:
        """Searches WOM for player, returns Player with latest snapshot"""
        if group_id is None:
            raise ValueError("A group id must be provided")

        group_json = requests.get(f"{self.base_url}/groups/{id}").json()

        return Group(**group_json)
