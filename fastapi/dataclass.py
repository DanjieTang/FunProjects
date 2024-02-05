from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True)
    username: str = Column(String, index=True)
    real_name: str = Column(String)
    age: int = Column(Integer)
    hashed_password: str = Column(String)
    
class Storage(Base):
    __tablename__ = "storage"
    id: int = Column(Integer, primary_key=True)
    store_name: str = Column(String)
    user_id: int = Column(String, ForeignKey("user.id"))
    store_location: str = Column(String)
    
class Item(Base):
    __tablename__ = "item"
    id: int = Column(Integer, primary_key=True)
    item_name: str = Column(String)
    num: int = Column(Integer)
    storage_id: int = Column(Integer, ForeignKey("storage.id"))