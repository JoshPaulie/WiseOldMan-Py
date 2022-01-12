"""Holds custom data types"""


class Player:
    def __init__(self, player_json: dict) -> None:
        self.player_json = player_json
        self.exp = self.player_json["exp"]
        self.id = self.player_json["id"]
        self.username = self.player_json["username"]
        self.display_name = self.player_json["displayName"]

    def __repr__(self) -> str:
        return f"{self.username=}"
