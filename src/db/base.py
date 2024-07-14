from abc import abstractmethod
from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from config import settings
from utils.case_converter import camel_case_to_snake_case


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @classmethod
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return '{0}'.format(camel_case_to_snake_case(cls.__name__))

    @abstractmethod
    def to_read_model[SomeModel](self) -> SomeModel:
        raise NotImplementedError


engine = create_async_engine(
    url=settings.db.database_url,
    echo=False,
)
session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session:
        yield session
