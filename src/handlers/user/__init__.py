from aiogram import Router, F
from aiogram.filters import CommandStart

from filters import ChatTypeFilter
from handlers.user.answer_back import answer_back
from handlers.user.cancel_inline import cancel
from handlers.user.start import start
from handlers.user.start_with_params import start_with_params
from handlers.user.text_to_send_state import get_text_to_send
from states import UserStates


def prepare_router() -> Router:
    router = Router()
    router.message.filter(ChatTypeFilter('private'))

    router.message.register(get_text_to_send, F.text, UserStates.get_text_to_send)
    router.message.register(start, F.text == '/start')
    router.message.register(start_with_params, CommandStart())
    router.callback_query.register(cancel, F.data == 'cancel')
    router.callback_query.register(answer_back, F.data.startswith('answer_back_'))

    return router
