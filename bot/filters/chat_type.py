from aiogram.filters import BaseFilter
from aiogram.types import Message


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: str) -> None:
        self.chat_type = chat_type

    async def __call__(self, msg: Message, *args, **kwargs) -> bool:
        if isinstance(self.chat_type, str):
            return msg.chat.type == self.chat_type
        raise TypeError
