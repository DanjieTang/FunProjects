from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__: str = "user"
    id: int 
    name: str | None = Column("name")
    
engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

with Session() as session:
    user = User(name="Danjie")
    session.add(user)
    session.commit()