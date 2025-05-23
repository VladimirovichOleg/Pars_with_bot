from typing import List

from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):

    def __init__(self, user_ids: List[str]) -> None:
        self.user_ids = [int(id) for id in user_ids]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.user_ids
