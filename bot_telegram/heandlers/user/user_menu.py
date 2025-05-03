from aiogram import Router, F
from aiogram.types import Message

from sqlite_db.async_db_execute import AsyncDbExecute


user_router = Router()
find = AsyncDbExecute("tile_data")


@user_router.message(F.text)
async def find_product(message: Message):
    results = await find(message.text)
    if results:
        await find.add_req_for_db(message.from_user.id, results[0])
        for res in results:
            data = (f"{res[2]}\n"
                    f"Артикул: {res[3]}\n"
                    f"Ціна: {res[4]}{res[7]}\n"
                    f"Знижка: {res[5]}{res[7]}\n")
            if res[6] != 0.0:
                data = f"{data}Ціна без знижки: {res[6]}{res[7]}"
            await message.answer(text=data)
    else:
        await message.answer(text="Для пошуку введіть назву або артикул товару")


@user_router.message()
async def find_product(message: Message):
    await message.answer(text="Для пошуку введіть назву або артикул товару.")

