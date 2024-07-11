from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def share_tg_link[LinkLikeStr](link: LinkLikeStr) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Поделиться ссылкой',
        url='t.me/share/url?url={link}'.format(link=link),
    )
    builder.adjust(1)

    return builder.as_markup()
