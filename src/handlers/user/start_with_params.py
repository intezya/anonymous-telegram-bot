from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import cancel as cancel_kb
from other.constants import SUCCESSFUL_LINK_TEXT
from states import UserStates


async def start_with_params(msg: Message, command: CommandObject, state: FSMContext):
    args = command.args

    # x = await is_correct_id(msg.from_user.id, args)
    x = args
    kb = None

    #  TODO: do try/except
    match x:
        case ValueError():
            text = '❌ Некорректная ссылка! ❌'
        case False:
            text = '❌ Вы не можете написать сами себе! ❌'
        case KeyError():
            text = '❌ Такого пользователя не существует! ❌'
        case _:
            text = SUCCESSFUL_LINK_TEXT
            kb = cancel_kb()
            await state.set_state(UserStates.get_text_to_send)
            await state.update_data(receiver_id=x)

    await msg.answer(
        text=text,
        reply_markup=kb,
    )
