import requests
from .player import Player


class WiseOldMan:
    def __init__(self) -> None:
        self.base_url = "https://api.wiseoldman.net"

    def get_player(self, osrs_username: str) -> Player:
        player_json = requests.get(f"{self.base_url}/players/username/{osrs_username}").json()
        return Player(player_json)
