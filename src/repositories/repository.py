from abc import ABC, abstractmethod
from select import select

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, tg_id: int, hashed_tg_id: str) -> int:
        raise NotImplemented

    @abstractmethod
    async def find_one(self):
        raise NotImplemented


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, tg_id: int, hashed_tg_id: str) -> None:
        statement = insert(self.model).values(tg_id=tg_id, hashed_tg_id=hashed_tg_id)
        result = await self.session.execute(statement)

    async def find_one(self, **filter_by):
        statement = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(statement)
        result = result.scalar_one().to_read_model()
        return result
