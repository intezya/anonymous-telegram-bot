from aiogram import Bot
from aiogram.types import Message

from keyboards.inline import share_tg_link
from other.constants import START_TEXT
from repositories.unitofwork import IUnitOfWork
from services.users import UsersService


async def start(msg: Message, bot: Bot, uow: IUnitOfWork):
    hashed_tg_id = await UsersService().add_user(uow, msg.from_user.id)

    bot_info = await bot.me()
    link = f"https://t.me/{bot_info.username}?start={hashed_tg_id}"

    await msg.answer(text=START_TEXT.format(link=link),
                     reply_markup=share_tg_link(link))
