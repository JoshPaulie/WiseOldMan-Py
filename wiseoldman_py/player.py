"""Holds custom data types"""


class Player:
    def __init__(self, player_data: dict) -> None:
        self.player_data = player_data
        self.exp = self.player_data["exp"]
        self.id = self.player_data["id"]
        self.username = self.player_data["username"]
        self.display_name = self.player_data["displayName"]
        self.type = self.player_data["type"]
        self.build = self.player_data["build"]
        self.country = self.player_data["country"]
        self.flagged = self.player_data["flagged"]
        self.ehp = self.estimated_hours_played = self.player_data["ehp"]
        self.ehb = self.player_data["ehb"]
        self.ttm = self.player_data["ttm"]
        self.tt200m = self.player_data["tt200m"]
        self.last_imported_at = self.player_data["lastImportedAt"]
        self.last_changed_at = self.player_data["lastChangedAt"]
        self.registered_at = self.player_data["registeredAt"]
        self.updated_at = self.player_data["updatedAt"]
        self.combat_level = self.player_data["combatLevel"]
        self.latest_snapshot = self.player_data["latestSnapshot"]
        self.skill = Skills(self.latest_snapshot)

    def __repr__(self) -> str:
        return f"{self.username=}"


class Skills:
    def __init__(self, latest_snapshot) -> None:
        self.latest_snapshot = latest_snapshot
        self.overall_rank = self.latest_snapshot["overall"]["rank"]
        self.overall_experience = self.latest_snapshot["overall"]["experience"]
        self.overall_ehp = self.latest_snapshot["overall"]["ehp"]

        self.attack_rank = self.latest_snapshot["attack"]["rank"]
        self.attack_experience = self.latest_snapshot["attack"]["experience"]
        self.attack_ehp = self.latest_snapshot["attack"]["ehp"]
