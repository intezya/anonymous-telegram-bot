import logging

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from .keyboards import answer_back_keyboard, cancel_keyboard, share_tg_link_keyboard
from .states import States
from .utils.is_correct_id import is_correct_id

user_router = Router()


@user_router.message(F.text == "/start")
async def user_start(msg: Message, bot: Bot):
    bot_info = await bot.me()

    link = f"https://t.me/{bot_info.username}?start={msg.from_user.id}"

    await msg.answer(text=f"🔗 Вот твоя личная ссылка:\n\n"
                          f"{link}\n\n"
                          f"Опубликуй её в Telegram, TikTok, VK, Instagram "
                          f"и получай анонимные сообщения",
                     reply_markup=share_tg_link_keyboard(link))


@user_router.message(CommandStart())
async def user_start_with_params(msg: Message, command: CommandObject, state: FSMContext):
    args = command.args

    x = await is_correct_id(msg.from_user.id, args)
    kb = None

    match x:
        case ValueError():
            text = "❌ Некорректная ссылка! ❌"
        case False:
            text = "❌ Вы не можете написать сами себе! ❌"
        case KeyError():
            text = "❌ Такого пользователя не существует! ❌"
        case _:
            text = "Сейчас ты можешь отправить анонимное сообщение тому человеку, " \
                   "который опубликовал эту ссылку."
            kb = cancel_keyboard()
            await state.set_state(States.user_state)
            await state.update_data(receiver_id=x)

    await msg.answer(text=text,
                     reply_markup=kb)


@user_router.callback_query(F.data == "cancel")
async def user_cancel(callback: CallbackQuery, state: FSMContext, bot: Bot):
    logging.log(level=logging.DEBUG,
                msg="user_cancel handled")

    bot_info = await bot.me()
    link = f"https://t.me/{bot_info.username}?start={callback.from_user.id}"

    await callback.message.edit_text(text=f"⚙️ Вы отменили отправку сообщения!\n\n"
                                          f"🔗 Вот твоя личная ссылка:\n\n"
                                          f"{link}\n\n"
                                          f"Опубликуй её и получай анонимные сообщения",
                                     reply_markup=share_tg_link_keyboard(link))
    await state.clear()
    await state.update_data(sender_id="")


@user_router.message(States.user_state)
async def get_text_to_send(msg: Message, state: FSMContext, bot: Bot):
    state_data = await state.get_data()
    receiver_id = state_data.get("receiver_id")

    # TODO: remove try/except construction
    # (It will be removed when logic in .utils.is_correct_id will be implemented)
    try:
        await bot.copy_message(from_chat_id=msg.chat.id,
                               message_id=msg.message_id,
                               chat_id=receiver_id,
                               reply_markup=answer_back_keyboard(msg.from_user.id))
        text = "Сообщение отправлено!"
    except TelegramBadRequest:
        text = "❌ Пользователь не найден! ❌"

    await msg.answer(text=text)
    await state.clear()


@user_router.callback_query(F.data.startswith("answer-back-"))
async def answer_back(callback: CallbackQuery, state: FSMContext, bot: Bot):
    sender_id = callback.data.split("-")[2]

    await callback.message.answer(text="Отправьте Ваш ответ на анонимное сообщение",
                                  reply_markup=cancel_keyboard())
    await state.set_state(States.user_state)
    await state.update_data(receiver_id=sender_id)


@user_router.message()
async def user_echo(msg: Message, bot: Bot):
    await msg.send_copy(chat_id=msg.from_user.id)
