from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork


class UsersService:
    async def add_user(self, uow: IUnitOfWork, tg_id: int):
        async with uow:
            hashed_tg_id = get_hash(tg_id)
            await uow.users.add_one(tg_id, hashed_tg_id)
            await uow.commit()
            return hashed_tg_id

    async def get_user(self, uow: IUnitOfWork):
        async with uow:
            return await uow.users.find_one()
