"""Holds Player (and related) models"""
import datetime
from typing import Optional

import requests
from pydantic import BaseModel, Field

from wiseoldman_py.competitions import Competition

from .modules.calculators import get_level
from .modules.static import WOM_BASE_URL


class Achievement(BaseModel):
    """Parses Achievement"""

    threshold: int
    player_id: int = Field(alias="playerId")
    name: str
    metric: str
    created_at: Optional[datetime.datetime] = Field(alias="createdAt")
    measure: str


class Skill(BaseModel):
    """Parses skill and offers level and virtual level"""

    rank: int
    exp: int = Field(alias="experience")
    ehp: float

    @property
    def level(self) -> int:
        """Returns Skill's level up to 99"""
        return get_level(self.exp)

    @property
    def virtual_level(self) -> int:
        """Returns Skill's level up to and beyond 99"""
        return get_level(self.exp, virtual_level=True)


class BossKC(BaseModel):
    """Parses a Player's boss 'kill count'"""

    rank: int
    kills: int
    ehb: float


class EstimatedHours(BaseModel):
    """Parses estimated hours played in given activity"""

    rank: int
    value: float


class CluesAndBounties(BaseModel):
    """Parses Clues and Bounties, provides rank and score (amount)"""

    rank: int
    score: float


class Snapshot(BaseModel):
    """Parses the a WOM 'snapshot'. This is essentially a player's stats at a given time"""

    created_at: Optional[datetime.datetime] = Field(alias="createdAt")
    imported_at: Optional[datetime.datetime] = Field(alias="importedAt")
    overall: Skill
    attack: Skill
    defence: Skill
    strength: Skill
    hitpoints: Skill
    ranged: Skill
    prayer: Skill
    magic: Skill
    cooking: Skill
    woodcutting: Skill
    fletching: Skill
    fishing: Skill
    firemaking: Skill
    crafting: Skill
    smithing: Skill
    mining: Skill
    herblore: Skill
    agility: Skill
    thieving: Skill
    slayer: Skill
    farming: Skill
    runecrafting: Skill
    hunter: Skill
    construction: Skill

    league_points: CluesAndBounties
    bounty_hunter_hunter: CluesAndBounties
    bounty_hunter_rogue: CluesAndBounties
    clue_scrolls_all: CluesAndBounties
    clue_scrolls_beginner: CluesAndBounties
    clue_scrolls_easy: CluesAndBounties
    clue_scrolls_medium: CluesAndBounties
    clue_scrolls_hard: CluesAndBounties
    clue_scrolls_elite: CluesAndBounties
    clue_scrolls_master: CluesAndBounties
    last_man_standing: CluesAndBounties
    soul_wars_zeal: CluesAndBounties

    abyssal_sire: BossKC
    alchemical_hydra: BossKC
    barrows_chests: BossKC
    bryophyta: BossKC
    callisto: BossKC
    cerberus: BossKC
    chambers_of_xeric: BossKC
    chambers_of_xeric_challenge_mode: BossKC
    chaos_elemental: BossKC
    chaos_fanatic: BossKC
    commander_zilyana: BossKC
    corporeal_beast: BossKC
    crazy_archaeologist: BossKC
    dagannoth_prime: BossKC
    dagannoth_rex: BossKC
    dagannoth_supreme: BossKC
    deranged_archaeologist: BossKC
    general_graardor: BossKC
    giant_mole: BossKC
    grotesque_guardians: BossKC
    hespori: BossKC
    kalphite_queen: BossKC
    king_black_dragon: BossKC
    kraken: BossKC
    kreearra: BossKC
    kril_tsutsaroth: BossKC
    mimic: BossKC
    nex: BossKC
    nightmare: BossKC
    phosanis_nightmare: BossKC
    obor: BossKC
    sarachnis: BossKC
    scorpia: BossKC
    skotizo: BossKC
    tempoross: BossKC
    the_gauntlet: BossKC
    the_corrupted_gauntlet: BossKC
    theatre_of_blood: BossKC
    theatre_of_blood_hard_mode: BossKC
    thermonuclear_smoke_devil: BossKC
    tzkal_zuk: BossKC
    tztok_jad: BossKC
    venenatis: BossKC
    vetion: BossKC
    vorkath: BossKC
    wintertodt: BossKC
    zalcano: BossKC
    zulrah: BossKC

    ehp: EstimatedHours
    ehb: EstimatedHours


class Player(BaseModel):
    """
    Represents a player from Wiseoldman. 🧙‍♂️

    🔌 Endpoint(s): /players/, /players/achievements, /players/competitions

    At initialization this is just WOM account data, as well as the latest snapshot WOM has.

    Additional 'get' methods are used to access additional information endpoints to the same player (ie achievements, competitions)
    """

    total_exp: int = Field(alias="exp")
    player_id: int = Field(alias="id")  # ? 'id' is a keyword
    username: str
    display_name: str = Field(alias="displayName")
    account_type: str = Field(alias="type")  # ? 'type' is a keyword
    build: str
    country: Optional[str]
    flagged: bool
    ehp: float
    ehb: float
    ttm: float
    tt200m: float
    last_imported_at: Optional[datetime.datetime] = Field(alias="lastImportedAt")
    last_changed_at: Optional[datetime.datetime] = Field(alias="lastChangedAt")
    registered_at: Optional[datetime.datetime] = Field(alias="registeredAt")
    updated_at: Optional[datetime.datetime] = Field(alias="updatedAt")
    combat_level: int = Field(alias="combatLevel")
    latest_snapshot: Snapshot = Field(alias="latestSnapshot")

    def get_achievements(self) -> list[Achievement]:
        """📞 Makes another call to the API. Returns any achievements the player has."""
        player_achievement_json = requests.get(f"{WOM_BASE_URL}/players/{self.player_id}/achievements").json()

        achievements = []
        for a in player_achievement_json:
            achievements.append(Achievement(**a))

        return achievements

    def get_competitions(self) -> list[Competition]:
        """📞 Makes another call to the API. Returns any competitions the player has ever been in"""
        player_competition_json = requests.get(f"{WOM_BASE_URL}/players/{self.player_id}/competitions").json()

        competitions = []
        for c in player_competition_json:
            competitions.append(Competition(**c))
        return competitions
