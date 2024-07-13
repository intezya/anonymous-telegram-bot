from aiogram.filters import CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.inline import cancel as cancel_kb
from other.constants import SUCCESSFUL_LINK_TEXT, USER_NOT_FOUND_TEXT, CANNOT_SEND_MESSAGE_YOURSELF
from other.get_hash import get_hash
from repositories.unitofwork import IUnitOfWork
from services.users import UsersService
from states import UserStates


async def start_with_params(  # noqa: WPS217
    msg: Message,
    command: CommandObject,
    state: FSMContext,
    uow: IUnitOfWork,
) -> None:
    user_from_db = await UsersService().get_user(uow, user_id=msg.from_user.id)
    if user_from_db is None:
        await UsersService().add_user(uow, msg.from_user.id)

    receiver_user = await UsersService().get_user(uow, hashed_id=command.args)

    await msg.delete()

    if receiver_user is None:
        await msg.answer(USER_NOT_FOUND_TEXT)
        return

    if receiver_user.id == msg.from_user.id:
        await msg.answer(CANNOT_SEND_MESSAGE_YOURSELF)
        return
    else:
        text = SUCCESSFUL_LINK_TEXT
        await state.set_state(UserStates.get_text_to_send)

    sent_message = await msg.answer(
        text=text,
        reply_markup=cancel_kb(),
    )

    await state.update_data(
        receiver_id=receiver_user.id,
        hashed_sender_id=get_hash(msg.from_user.id),
        msg_id_to_delete=sent_message.message_id,
        msg_chat_id_to_delete=sent_message.chat.id,
    )
