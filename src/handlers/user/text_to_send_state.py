from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import answer_back as answer_back_kb
from other.constants import MSG_SENT_TEXT


async def get_text_to_send(
    msg: Message,
    state: FSMContext,
    bot: Bot,
) -> None:
    state_data = await state.get_data()
    receiver_id = state_data.get('receiver_id')
    hashed_sender_id = state_data.get('hashed_sender_id')

    if msg.text:
        text_for_msg = 'Получено новое сообщение!\n\n{text}'.format(text=msg.text)
        await bot.send_message(
            chat_id=receiver_id,
            text=text_for_msg,
            reply_markup=answer_back_kb(hashed_sender_id),
        )
    else:
        await bot.copy_message(
            from_chat_id=msg.chat.id,
            message_id=msg.message_id,
            chat_id=receiver_id,
            reply_markup=answer_back_kb(hashed_sender_id),
        )

    await bot.delete_message(
        chat_id=state_data.get('msg_chat_id_to_delete'),
        message_id=state_data.get('msg_id_to_delete'),
    )

    await msg.answer(text=MSG_SENT_TEXT)
    await state.clear()
