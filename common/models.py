from pydantic import BaseModel, Field
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Unicode
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import Field, SQLModel
from datetime import datetime

ENCRYPTION_KEY="SpecialForBotEncryptionKey"


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    telegram_id: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    additor_name: str | None = Field(default=None)
    leaved: bool  = Field(default=False)
    leaved_date: datetime | None = Field(default=None)
    added_date: datetime
    

# class Messages(SQLModel, table=True):
#     Id: int | None  = Field(default=None, primary_key=True)
#     UserID: int = Field(default=None, foreign_key='characteristic.Id')
#     Date: date
#     UserID: int = Field(default=None, foreign_key='characteristic.Id')
#     Series: str
#     Value: float