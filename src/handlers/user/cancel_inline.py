from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import share_tg_link
from other.constants import CANCEL_INLINE_TEXT
from other.get_hash import get_hash


async def cancel(callback: CallbackQuery, state: FSMContext, bot: Bot):
    hashed_tg_id = await get_hash(callback.from_user.id)

    bot_info = await bot.me()
    link = 'https://t.me/{bot_username}?start={hashed_tg_id}'.format(
        bot_username=bot_info.username,
        hashed_tg_id=hashed_tg_id,
    )

    await callback.message.edit_text(
        text=CANCEL_INLINE_TEXT.format(link=link),
        reply_markup=share_tg_link(link),
    )
    await state.clear()
    await state.update_data(sender_id='')
