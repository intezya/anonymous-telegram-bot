from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import share_tg_link
from other.constants import CANCEL_INLINE_TEXT


async def cancel(callback: CallbackQuery, state: FSMContext, bot: Bot):
    bot_info = await bot.me()
    link = f"https://t.me/{bot_info.username}?start={callback.from_user.id}"

    await callback.message.edit_text(text=CANCEL_INLINE_TEXT.format(link=link),
                                     reply_markup=share_tg_link(link))
    await state.clear()
    await state.update_data(sender_id="")
