import logging

from aiogram import Bot


async def on_startup(bot: Bot) -> None:
    bot_info = await bot.get_me()

    logging.log(level=logging.INFO,
                msg=f"Bot {bot_info.full_name} started!")

    await bot.delete_webhook(drop_pending_updates=True)
