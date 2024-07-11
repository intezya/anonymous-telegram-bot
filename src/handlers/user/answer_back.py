from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline import cancel as cancel_kb
from other.constants import ANSWER_BACK_TEXT
from states import UserStates


async def answer_back(callback: CallbackQuery, state: FSMContext):
    sender_id = callback.data.split('-')[2]

    await callback.message.answer(
        text=ANSWER_BACK_TEXT,
        reply_markup=cancel_kb(),
    )
    await state.set_state(UserStates.get_text_to_send)
    await state.update_data(receiver_id=sender_id)
