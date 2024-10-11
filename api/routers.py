from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from settings import create_session
from models import Chats
from common.models import Chats as SqlChats

router = APIRouter(prefix="/database", tags=["database"])


@router.post("/new_chat")
async def create_new_chat(item: Chats, db: Session = Depends(create_session)):
    item = SqlChats(**item.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
