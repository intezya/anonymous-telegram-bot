from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import answer_back as answer_back_kb
from other.constants import MSG_SENT_TEXT, USER_NOT_FOUND_TEXT


async def get_text_to_send(msg: Message, state: FSMContext, bot: Bot):
    state_data = await state.get_data()
    receiver_id = state_data.get("receiver_id")

    # TODO: remove try/except construction
    # (It will be removed when logic in .utils.is_correct_id will be implemented)
    try:
        await bot.send_message(chat_id=receiver_id,
                               text='Получено новое сообщение!')
        await bot.copy_message(from_chat_id=msg.chat.id,
                               message_id=msg.message_id,
                               chat_id=receiver_id,
                               reply_markup=answer_back_kb(msg.from_user.id),
                               )
        text = MSG_SENT_TEXT
    except TelegramBadRequest as e:
        text = USER_NOT_FOUND_TEXT
        print(e, receiver_id)

    await msg.answer(text=text)
    await state.clear()
