import asyncio
import logging
from aiogram import Bot

from bot_telegram import config_file

logger = logging.getLogger(__name__)

bot = Bot(token=config_file['TOKEN_BOT'])


async def send_error_message(user_id: int, error_message: str):
    try:
        await bot.send_message(chat_id=user_id, text=f"Произошла ошибка: \n{error_message}")
        logger.info(f"Сообщение об ошибке отправлено пользователю с ID {user_id}")
    except Exception as e:
        logger.info(f"Не удалось отправить сообщение пользователю с ID {user_id}: {e}")


def notify_error(user_id: int, error_message: str):  # СИНХРОННАЯ !!!
    loop = asyncio.get_event_loop()

    # Если цикл событий уже запущен, используем asyncio.create_task для запуска корутины
    if loop.is_running():
        # Запускаем корутину send_error_message в фоновом режиме
        asyncio.create_task(send_error_message(user_id, error_message))
    else:
        # Если цикл не запущен (например, для тестов), запускаем новый цикл событий
        loop.run_until_complete(send_error_message(user_id, error_message))
