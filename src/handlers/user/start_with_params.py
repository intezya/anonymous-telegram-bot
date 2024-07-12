from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import cancel as cancel_kb
from other.constants import SUCCESSFUL_LINK_TEXT
from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork
from services.users import UsersService
from states import UserStates


async def start_with_params(
    msg: Message,
    command: CommandObject,
    state: FSMContext,
    uow: IUnitOfWork,
) -> None:
    user_from_db = await UsersService().get_user(uow, user_id=msg.from_user.id)

    if user_from_db is None:
        await UsersService().add_user(uow, msg.from_user.id)

    receiver_hashed_id = command.args

    receiver_user = await UsersService().get_user(uow, hashed_id=receiver_hashed_id)

    if receiver_user is None:
        await msg.answer('Такого пользователя не существует! ❌')
        return

    receiver_id = receiver_user.id

    if receiver_id == msg.from_user.id:
        await msg.answer('Нельзя отправить сообщение самому себе! ❌')
        return
    else:
        text = SUCCESSFUL_LINK_TEXT
        await state.set_state(UserStates.get_text_to_send)

    sent_message = await msg.answer(
        text=text,
        reply_markup=cancel_kb(),
    )

    await msg.delete()

    await state.update_data(
        receiver_id=receiver_id,
        hashed_sender_id=get_hash(msg.from_user.id),
        msg_id_to_delete=sent_message.message_id,
        msg_chat_id_to_delete=sent_message.chat.id,
    )
