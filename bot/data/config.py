import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

path_to_env_file = Path(__file__).parent.parent.parent / '.env'

load_dotenv(dotenv_path=path_to_env_file)


@dataclass
class BotConfig:
    token: str


@dataclass
class Settings:
    bot: BotConfig


settings = Settings(
    bot=BotConfig(
        token=os.environ['BOT_TOKEN'],
    )
)
