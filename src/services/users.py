from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork
from schemas.user import UserSchema


class UsersService:
    async def add_user(self, uow: IUnitOfWork, tg_id: int) -> None:
        async with uow:
            hashed_tg_id = get_hash(tg_id)
            await uow.users.add_one(tg_id, hashed_tg_id)
            await uow.commit()

    async def get_user(self, uow: IUnitOfWork, user_id: str) -> UserSchema:
        async with uow:
            return await uow.users.find_one(hashed_tg_id=user_id)
