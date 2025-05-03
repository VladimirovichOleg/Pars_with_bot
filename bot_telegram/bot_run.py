import asyncio
from datetime import datetime
import logging
from aiogram import Bot, Dispatcher

from bot_telegram.env import config_file
from bot_telegram.heandlers.admin.admin_menu import admin_router
from bot_telegram.heandlers.user.user_menu import user_router


logger = logging.getLogger()
FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, filename=f"bot_run.log", filemode="w", format=FORMAT)


async def main():
    try:
        bot = Bot(token=config_file['TOKEN_BOT'])
        dp = Dispatcher()
        dp.include_routers(admin_router, user_router)
        logger.info("Bot is starts at %s", datetime.now())
        await bot.send_message(chat_id=config_file['ADMIN_OL'], text=f"Bot has been started")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Bot is NOT starts at {datetime.now()} ERROR - {e}")


if __name__ == '__main__':
    print("Bot has been started")
    asyncio.run(main())
