from aiogram import Bot
from aiogram.types import Message

from keyboards.inline import share_tg_link
from other.constants import START_TEXT


async def start(msg: Message, bot: Bot):
    bot_info = await bot.me()
    link = f"https://t.me/{bot_info.username}?start={msg.from_user.id}"

    await msg.answer(text=START_TEXT.format(link=link),
                     reply_markup=share_tg_link(link))
