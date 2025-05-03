import aiosqlite
import logging

logger = logging.getLogger(__name__)


class AsyncDbExecute:
    # PATH_TO_DB = "/home/oleg/python_progect/keramag/sqlite_db/db_for_keramag.db"
    PATH_TO_DB = "/home/pars_with_teleg_bot/sqlite_db/db_for_keramag.db"  #  "." for LINUX, ".." for windows

    def __init__(self, name_table: str):
        self.name_table = name_table

    async def __call__(self, name_or_article_prod):
        result = await self.find_by_name_or_article(name_or_article_prod)
        return result

    async def find_by_name_or_article(self, name_or_article_prod):
        try:
            async with aiosqlite.connect(self.PATH_TO_DB) as con:
                query_ = f"SELECT * FROM {self.name_table} WHERE name LIKE ? OR article LIKE ?"
                async with con.execute(query_, (f'%{name_or_article_prod}%', f'%{name_or_article_prod}%')) as cursor:
                    result = await cursor.fetchmany(3)
                    if result:
                        return result
                    else:
                        return None
        except Exception as ex:
            print("ERROR DB")
            logger.error("Can`t open DataBase,  %s", ex)

    async def add_req_for_db(self, user_id: int, m_tuple: tuple):
        try:
            async with aiosqlite.connect(self.PATH_TO_DB) as con:
                query_ = (f"INSERT INTO users_requests (user_id, name, price, discount, article, country)"
                          f"VALUES (?, ?, ?, ?, ?, ?)")
                await con.execute(query_, (user_id, m_tuple[2], m_tuple[4], m_tuple[5], m_tuple[3], m_tuple[8],))
                await con.commit()
        except Exception as ex:
            logger.error("Can`t add requests to DB, error - %s", ex)
