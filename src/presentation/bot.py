import contextlib

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from src.infrastructure.config_loader import load_config
from src.presentation.telegram import start_all


async def main() -> None:
    bot_config = load_config().bot

    bot = Bot(token=bot_config.BOT_TOKEN,
              default=DefaultBotProperties(
                  parse_mode=ParseMode.HTML)
              )
    dp = Dispatcher()

    await start_all(bot, dp)


if __name__ == '__main__':
    import asyncio

    with contextlib.suppress(KeyboardInterrupt):
        asyncio.run(main())
