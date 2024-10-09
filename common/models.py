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
    chat_info: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    added_date: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )

class Users(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    belonging_chat_id: int = Field(default=None, foreign_key='chats.id')
    user_info: str = Field(
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )
    added_date: str | None = Field(
        default=None,
        sa_column=Column(
            StringEncryptedType(Unicode, ENCRYPTION_KEY, AesEngine, "pkcs5")
        )
    )

