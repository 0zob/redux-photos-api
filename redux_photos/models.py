from sqlalchemy import  Boolean, Column,  Integer, String, Text

from .database import Base


class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(244))
    like =  Column(Boolean, default=False)
    img_src = Column(Text)
