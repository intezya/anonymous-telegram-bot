from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import cancel as cancel_kb
from utils.constants import ANSWER_BACK_TEXT
from utils.get_hash import get_hash
from db.unitofwork import UnitOfWork
from services.users import UsersService
from states import UserStates


async def answer_back(
    callback: CallbackQuery,
    state: FSMContext,
    uow: UnitOfWork,
) -> None:
    sender_hashed_id = callback.data.split('_')[2]
    receiver_user = await UsersService().get_user(uow, hashed_id=sender_hashed_id)

    sent_message = await callback.message.answer(
        text=ANSWER_BACK_TEXT,
        reply_markup=cancel_kb(),
    )
    await state.set_state(UserStates.get_text_to_send)
    await state.update_data(
        receiver_id=receiver_user.id,
        hashed_sender_id=get_hash(callback.from_user.id),
        msg_id_to_delete=sent_message.message_id,
        msg_chat_id_to_delete=sent_message.chat.id,
    )
