from pydantic import BaseModel


class Group(BaseModel):
    group_id: int
    name: str
    clan_chat: str
    description: str
    homeworld: int
    score: int
    verified: bool
    created_at: str
    updated_at: str
    member_count: int
