from pydantic import Field
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, Unicode
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from sqlmodel import Field, SQLModel
from datetime import datetime

ENCRYPTION_KEY="SpecialForBotEncryptionKey"

class Chats(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    chat_id: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    title: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    added_date: datetime


class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    belonging_chat_id: int = Field(default=None, foreign_key='chats.id')
    first_name: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    last_name: str | None = Field(
        default=None,
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    username: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )


class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    belonging_chat_id: int = Field(default=None, foreign_key='chats.id')
    belonging_user_id: int = Field(default=None, foreign_key='users.id')
    text: str | None = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    date: datetime
