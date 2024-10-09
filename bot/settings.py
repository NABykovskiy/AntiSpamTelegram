from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = "7850327363:AAFoLDC1yij7ftqK8_e88p6gs3mllzfotNs"


settings = Settings()
