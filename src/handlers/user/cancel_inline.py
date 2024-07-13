from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import share_tg_link
from other.constants import CANCEL_INLINE_TEXT, BASE_SHARE_LINK
from other.get_hash import get_hash


async def cancel(
    callback: CallbackQuery,
    state: FSMContext,
    bot: Bot,
) -> None:
    hashed_id = get_hash(callback.from_user.id)

    bot_info = await bot.me()
    link = BASE_SHARE_LINK.format(
        bot_username=bot_info.username,
        hashed_id=hashed_id,
    )

    await callback.message.edit_text(
        text=CANCEL_INLINE_TEXT.format(link=link),
        reply_markup=share_tg_link(link),
    )
    await state.clear()
    await state.update_data(sender_id='')
