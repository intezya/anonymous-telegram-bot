import asyncio

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from handlers import user
from repositories.unitofwork import UnitOfWork


def setup_handlers(dp: Dispatcher) -> None:
    dp.include_routers(
        user.prepare_router(),
    )


async def setup_aiogram(dp: Dispatcher) -> None:
    setup_handlers(dp)


async def on_startup_polling(dispatcher: Dispatcher) -> None:
    await setup_aiogram(dispatcher)


async def on_shutdown_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    bot = Bot(
        token=settings.bot.token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    dp = Dispatcher(
        uow=UnitOfWork(),
    )

    dp.startup.register(on_startup_polling)
    dp.shutdown.register(on_shutdown_polling)

    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    main()
