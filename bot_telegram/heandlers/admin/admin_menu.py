from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import logging

from bot_telegram import config_file, IsAdmin
from sqlite_db import AsyncDbExecute

logger = logging.getLogger(__name__)
admin_router = Router()

find = AsyncDbExecute("tile_data")

list_of_admins = [
    config_file['ADMIN_OL'],
    config_file['ADMIN_VLAD'],
    config_file['ADMIN_LU']
]


@admin_router.message(Command('start'))
async def start_bot_admin(message: Message):
    await message.answer(f"Вас вітає бот магазину керамічної плитки «КЕРАМАГ»,"
                         f" для пошуку введіть назву або артикул товару.\n")


@admin_router.message(Command('admin'), IsAdmin(list_of_admins))
async def admin_com(message: Message):
    await message.answer("Hello Admin")


@admin_router.message(F.text, IsAdmin(list_of_admins))
async def find_product(message: Message):
    results = await find(message.text)
    if results:
        await find.add_req_for_db(message.from_user.id, results[0])
        for res in results:
            data = (f"{res[12]}\n"
                    f"{res[2]}\n"
                    f"Артикул: {res[3]}\n"
                    f"Ціна: {res[4]}{res[7]}\n"
                    f"Знижка: {res[5]}{res[7]}\n"
                    )
            if res[6] != 0.0:
                data = (f"{data}Ціна без знижки: {res[6]}{res[7]}")
            await message.answer(text=data)
    else:
        await message.answer(text="Для пошуку введіть назву або артикул товару.")
