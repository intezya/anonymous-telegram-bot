from aiogram import Bot, Dispatcher

from .on_startup import on_startup

# Routers import
from .user_handler import user_router


def register_all(dp: Dispatcher) -> None:
    """
    Register all routers and startup func to dispatcher
    :param dp:
    :return:
    """

    dp.include_routers(user_router, )
    dp.startup.register(on_startup)


async def start_all(bot: Bot, dp: Dispatcher) -> None:
    import logging
    logging.basicConfig(
        level=logging.DEBUG
    )
    register_all(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
