from sqlalchemy.orm import Query
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base
from datetime import datetime
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import PickleType






# model for Song

class SongModel(Base):
    __tablename__ = "song"
    id = Column(Integer, primary_key=True, autoincrement=True)
    song_name = Column(String(length=100))
    duration_in_sec = Column(Integer)
    upload_time = Column(DateTime(timezone=True), default=func.now())


# model for Podcast
class Podcast(Base):
    __tablename__ = 'podcast'
    id = Column(Integer, primary_key=True, autoincrement=True)
    podcast_name = Column(String(length=100))
    duration_in_sec = Column(Integer)
    uploaded_time = Column(DateTime(timezone=True), default=func.now())
    host = Column(String(length=100))
    participants = Column(String)

# model for Audiobook
class Audiobook(Base):
    __tablename__ = 'audiobook'
    id = Column(Integer, primary_key=True, autoincrement=True)
    audiobook_title = Column(String(100))
    author_title = Column(String(100))
    narrator = Column(String(100))
    duration_in_sec = Column(Integer)
    uploaded_time = Column(DateTime(timezone=True), default=func.now())
