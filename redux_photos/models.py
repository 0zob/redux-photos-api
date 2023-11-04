from __future__ import annotations

from sqlalchemy import Boolean, Column, Integer, String, Table, Text
from sqlalchemy.orm import Mapped, Relationship
from sqlalchemy.orm.properties import ForeignKey

from .database import Base

likes_table = Table(
    "likes",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("photo_id", ForeignKey("photos.id")),
)


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(244))
    img_src = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = Relationship("User", back_populates="photos")
    likes: Mapped[list[User]] = Relationship(secondary=likes_table)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(244), index=True)
    icon_src = Column(Text)
    photos = Relationship("Photo", back_populates="owner")
