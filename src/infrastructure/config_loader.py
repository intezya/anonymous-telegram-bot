import os
from dataclasses import dataclass

# @dataclass
# class DBConfig[ConfigEntry]:
#     DB_HOST: ConfigEntry
#     DB_NAME: ConfigEntry
#     DB_USER: ConfigEntry
#     DB_PASS: ConfigEntry
#
#     def DB_URL_asyncpg(self) -> str:
#         return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"


@dataclass
class BotConfig[ConfigEntry]:
    BOT_TOKEN: ConfigEntry
    # PARSE_MODE: ConfigEntry
    # ADMINS: List[int, ...]


@dataclass
class Config:
    bot: BotConfig
    # db: DBConfig


def load_config[ConfigEntry]() -> Config:
    bot_token: ConfigEntry = os.environ["BOT_TOKEN"]
    # db_name: ConfigEntry = os.environ["DB_NAME"]
    # db_user: ConfigEntry = os.environ["DB_USER"]
    # db_pass: ConfigEntry = os.environ["DB_PASS"]
    # db_host: ConfigEntry = os.environ["DB_HOST"]

    return Config(
        bot=BotConfig(
            BOT_TOKEN=bot_token
        ),
        # db=DBConfig(
        #     DB_HOST=db_host,
        #     DB_NAME=db_name,
        #     DB_USER=db_user,
        #     DB_PASS=db_pass
        # )
    )
