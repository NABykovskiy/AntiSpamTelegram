from pydantic import BaseModel
from datetime import datetime


class RootResponse(BaseModel):
    message: str


class Chats(BaseModel):
    id: int | None = None
    chat_id: int
    title: str
    added_date: datetime
