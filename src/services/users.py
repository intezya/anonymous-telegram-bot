from utils.get_hash import get_hash
from db.unitofwork import IUnitOfWork
from schemas.user import UserSchema


class UsersService:
    @staticmethod
    async def add_user(self, uow: IUnitOfWork, tg_id: int) -> None:
        async with uow:
            user = await UsersService().get_user(uow, user_id=tg_id)
            if user is not None:
                return

            hashed_id = get_hash(tg_id)
            await uow.users.add_one(tg_id, hashed_id)
            await uow.commit()

    @staticmethod
    async def get_user(self, uow: IUnitOfWork, **kwargs) -> UserSchema | None:
        if len(kwargs) > 1:
            raise ValueError('Too many kwargs')

        async with uow:
            return await uow.users.find_one(**kwargs)
