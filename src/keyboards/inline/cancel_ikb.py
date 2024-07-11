from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Отменить отправку',
        callback_data='cancel',
    )
    builder.adjust(1)

    return builder.as_markup()
