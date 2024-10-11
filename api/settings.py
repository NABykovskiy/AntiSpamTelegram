from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base


class Settings(BaseSettings):
    internal_db_name: str = "internaldb"
    internal_db_user: str = "internaluser"
    internal_db_pass: str = "internalpass"
    internal_db_port: int = 5432
    internal_db_url: str = "127.0.0.1"


settings = Settings()

db_url = f"postgresql+psycopg2://{settings.internal_db_user}:{settings.internal_db_pass}@{settings.internal_db_url}/{settings.internal_db_name}"
engine = create_engine(db_url)


def create_session() -> Session:
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db: Session = session_local()
    return db