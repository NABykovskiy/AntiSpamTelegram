from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str = "7606587036:AAFotId4AI3Oyd3TFjucmub2WMAE6NEHqoY"


settings = Settings()
