from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()

class Superhero(Base):
    __tablename__ = "superhero"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)
    real_name: str = Column(String)
    age: int = Column(Integer)
    team_id: int = Column(Integer, ForeignKey("team.id"), nullable=True)
    
class Team(Base):
    __tablename__ = "team"
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String)