from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def send_more(receiver_id: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Отправить ещё',
        callback_data='send_more_{0}'.format(receiver_id),
    )
    builder.adjust(1)

    return builder.as_markup()
