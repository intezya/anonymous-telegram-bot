from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import answer_back as answer_back_kb
from other.constants import MSG_SENT_TEXT, USER_NOT_FOUND_TEXT


async def get_text_to_send(msg: Message, state: FSMContext, bot: Bot):
    state_data = await state.get_data()
    receiver_id = state_data.get('receiver_id')
    hashed_sender_id = state_data.get('hashed_sender_id')

    try:
        await bot.send_message(
            chat_id=receiver_id,
            text='Получено новое сообщение!',
        )
    except TelegramBadRequest:
        text = USER_NOT_FOUND_TEXT
    else:
        await bot.copy_message(
            from_chat_id=msg.chat.id,
            message_id=msg.message_id,
            chat_id=receiver_id,
            reply_markup=answer_back_kb(hashed_sender_id),
        )
        text = MSG_SENT_TEXT

    await bot.delete_message(
        chat_id=state_data.get('msg_chat_id_to_delete'),
        message_id=state_data.get('msg_id_to_delete'),
    )

    await msg.answer(text=text)
    await state.clear()
