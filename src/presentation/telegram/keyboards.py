from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def share_tg_link_keyboard(link: str) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Поделиться ссылкой",
                   url=f"t.me/share/url?url={link}")
    builder.adjust(1)

    return builder.as_markup()


def cancel_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Отменить отправку",
                   callback_data="cancel")
    builder.adjust(1)

    return builder.as_markup()


def answer_back_keyboard[SenderUserID](_id: SenderUserID) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(text="Ответить!",
                   callback_data=f"answer-back-{_id}")
    builder.adjust(1)

    return builder.as_markup()
