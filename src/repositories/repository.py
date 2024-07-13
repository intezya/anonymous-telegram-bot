from abc import ABC
from abc import abstractmethod

from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from other.get_hash import get_hash
from schemas.user import UserSchema


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, tg_id: int, hashed_tg_id: str) -> int:
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **filter_by):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, tg_id: int, hashed_id: str) -> None:
        statement = insert(self.model).values(id=tg_id, hashed_id=get_hash(tg_id))
        await self.session.execute(statement)

    async def find_one(self, **filter_by) -> UserSchema | None:
        if 'user_id' in filter_by.keys():
            filter_by['id'] = int(filter_by.pop('user_id'))
        statement = select(self.model).filter_by(**filter_by)
        query_result = await self.session.execute(statement)
        try:
            return query_result.scalar_one().to_read_model()
        except NoResultFound:
            return None
