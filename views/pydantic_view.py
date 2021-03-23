
from pydantic import BaseModel
from fastapi import Query
from typing import Optional, List
from datetime import datetime


# BaseModel for accepting request and validate value
# pydantic model

class SongPyd(BaseModel):
    song_name: str
    duration_in_sec: int
    # upload_time: datetime


class PodcastPyd(BaseModel):
    podcast_name: str
    duration_in_sec: int
    # uploaded_time: datetime
    host: str
    participants: Optional[List[str]] = []


# AudioBook
class AudioBookPyd(BaseModel):
    audiobook_title: str
    author_title: str
    narrator: str
    duration_in_sec: int
    # uploaded_time: datetime




