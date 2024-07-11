from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def answer_back(sender_id: int) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Ответить",
                   callback_data="answer_back_{0}".format(sender_id))
    builder.adjust(1)

    return builder.as_markup()
