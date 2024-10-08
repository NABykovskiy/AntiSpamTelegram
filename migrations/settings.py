
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_user: str = "internaluser"
    database_pass: str = "internalpass"
    database_name: str = "internaldb"
    service_url: str = "localhost:5432"

    def get_db_url(self) -> str:
        return f"postgresql+psycopg2://{self.database_user}:{self.database_pass}@{self.service_url}/{self.database_name}"


settings = Settings()
