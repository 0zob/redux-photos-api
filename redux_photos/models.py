from sqlalchemy import  Boolean, Column,  Integer, String, Text
from sqlalchemy.orm import Relationship
from sqlalchemy.orm.properties import ForeignKey

from .database import Base


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(244))
    like =  Column(Boolean, default=False)
    img_src = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = Relationship("User", back_populates="photos")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(244), index=True)
    icon_src = Column(Text)
    photos = Relationship("Photo", back_populates="owner")
    
