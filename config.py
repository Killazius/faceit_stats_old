from dataclasses import dataclass
import os
import dotenv

@dataclass
class TgBot:
    token:str
    admin_id: str

@dataclass
class Config:
    tg_bot: TgBot

def load_config() -> Config:
    dotenv.load_dotenv()
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    ADMIN_ID = os.getenv('ADMIN_ID')
    return Config(
        tg_bot=TgBot(
        token = BOT_TOKEN,
        admin_id=ADMIN_ID)
        )


