import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Competition(BaseModel):
    competition_id: int = Field(alias="id")  # ? 'id' is a keyword
    title: str
    metric: str
    score: int
    starts_at: Optional[datetime.datetime] = Field(alias="startsAt")
    ends_at: Optional[datetime.datetime] = Field(alias="endsAt")
    competition_type: str = Field(alias="type")  # ? 'type' is a keyword
    group_id: Optional[int]
    created_at: Optional[datetime.datetime] = Field(alias="createdAt")
    updated_at: Optional[datetime.datetime] = Field(alias="updatedAt")
    duration: str  # ? You'd think this would be an int, it's not
    participant_count: int = Field(alias="participantCount")


class Participation(BaseModel):
    player_id: int = Field(alias="playerId")
    competition_id: int = Field(alias="competitionId")
    start_snapshot_id: int = Field(alias="startSnapshotId")
    end_snapshot_id: int = Field(alias="endSnapshotId")
