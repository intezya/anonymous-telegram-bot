from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import answer_back as answer_back_kb
from keyboards.inline import send_more
from utils.constants import MSG_SENT_TEXT, RECEIVED_NEW_MESSAGE
from utils.get_hash import get_hash


async def get_text_to_send(  # noqa: WPS217
    msg: Message,
    state: FSMContext,
    bot: Bot,
) -> None:
    state_data = await state.get_data()
    receiver_id = state_data.get('receiver_id')
    hashed_sender_id = state_data.get('hashed_sender_id')
    msg_chat_id_to_delete = state_data.get('msg_chat_id_to_delete')
    msg_id_to_delete = state_data.get('msg_id_to_delete')

    if msg.text:
        text_for_msg = '{INJECTED_MESSAGE}\n\n{text}'.format(
            INJECTED_MESSAGE=RECEIVED_NEW_MESSAGE,
            text=msg.text
        )
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

    await msg.answer(
        text=MSG_SENT_TEXT,
        reply_markup=send_more(get_hash(receiver_id)),
    )

    await bot.delete_message(
        chat_id=msg_chat_id_to_delete,
        message_id=msg_id_to_delete,
    )

    await state.clear()
