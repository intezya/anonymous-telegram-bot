import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
from pydantic import PostgresDsn

path_to_env_file = Path(__file__).parent / '.env'

load_dotenv(dotenv_path=path_to_env_file)


@dataclass
class BotConfig:
    token: str


@dataclass
class DBConfig:
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str

    @property
    def database_url(self) -> PostgresDsn:
        return 'postgresql+asyncpg://{user}:{passw}@{host}:{port}/{name}'.format(
            user=self.db_user,
            passw=self.db_pass,
            host=self.db_host,
            port=self.db_port,
            name=self.db_name,
        )

    @property
    def naming_convention(self):
        return {
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
            'ck': 'ck_%(table_name)s_%(constraint_name)s',
            'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
            'pk': 'pk_%(table_name)s',
        }


@dataclass
class Settings:
    bot: BotConfig
    db: DBConfig


settings = Settings(
    bot=BotConfig(
        token=os.environ['BOT_TOKEN'],
    ),
    db=DBConfig(
        db_user=os.environ['DB_USER'],
        db_pass=os.environ['DB_PASS'],
        db_host=os.environ['DB_HOST'],
        db_port=int(os.environ['DB_PORT']),
        db_name=os.environ['DB_NAME'],
    ),
)
