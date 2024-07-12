from aiogram import Bot
from aiogram.types import Message

from keyboards.inline import share_tg_link
from other.constants import START_TEXT
from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork
from services.users import UsersService


async def start(
    msg: Message,
    bot: Bot,
    uow: IUnitOfWork,
) -> None:
    user_from_db = await UsersService().get_user(uow, user_id=msg.from_user.id)

    if user_from_db is None:
        await UsersService().add_user(uow, msg.from_user.id)

    hashed_tg_id = get_hash(msg.from_user.id)

    bot_info = await bot.me()
    link = 'https://t.me/{bot_username}?start={hashed_tg_id}'.format(
        bot_username=bot_info.username,
        hashed_tg_id=hashed_tg_id,
    )

    await msg.answer(
        text=START_TEXT.format(link=link),
        reply_markup=share_tg_link(link),
    )
