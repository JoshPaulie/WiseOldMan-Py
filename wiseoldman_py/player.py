"""Holds custom Player data types"""
import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Skill(BaseModel):
    rank: int
    experience: int
    ehp: float


class BossKC(BaseModel):
    rank: int
    kills: int
    ehb: float


class EstimatedHours(BaseModel):
    rank: int
    value: float


class CluesAndBounties(BaseModel):
    rank: int
    score: float


class Snapshot(BaseModel):
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
    exp: int
    player_id: int = Field(alias="id")
    username: str
    display_name: str = Field(alias="displayName")
    account_type: str = Field(alias="type")
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
    latestSnapshot: Snapshot  # Not sure what to do with this one 🤔 It needs to be both a Field and a Snapshot
