from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Superhero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    hero_name: int | None = Field(default=None, index=True)
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Optional["Team"] = Relationship(back_populates="heros")
    
class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    headquarter: str
    heros: list[Superhero] = Relationship(back_populates="team")