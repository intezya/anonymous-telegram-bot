from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.exc import NoResultFound

from keyboards.inline import cancel as cancel_kb
from other.constants import SUCCESSFUL_LINK_TEXT
from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork
from services.users import UsersService
from states import UserStates


async def start_with_params(msg: Message, command: CommandObject, state: FSMContext, uow: IUnitOfWork):
    receiver_hashed_id = command.args
    kb = None

    try:
        receiver_user = await UsersService().get_user(uow, receiver_hashed_id)
    except NoResultFound:
        text = 'Такого пользователя не существует! ❌'
    else:
        receiver_id = receiver_user.tg_id

        if receiver_id == msg.from_user.id:
            text = 'Нельзя отправить сообщение самому себе! ❌'
        else:
            text = SUCCESSFUL_LINK_TEXT
            kb = cancel_kb()
            await state.set_state(UserStates.get_text_to_send)
            await state.update_data(
                receiver_id=receiver_id,
                hashed_sender_id=get_hash(msg.from_user.id),
            )

    await msg.answer(
        text=text,
        reply_markup=kb,
    )
